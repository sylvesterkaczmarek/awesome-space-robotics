#!/usr/bin/env python3
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = REPO_ROOT / "src"

URL_RE = re.compile(r"\[.*?\]\((https?://[^\s)]+)\)")

TIMEOUT = 10
MAX_WORKERS = 10
RETRIES = 2
RETRY_DELAY = 3
USER_AGENT = "Mozilla/5.0 (compatible; awesome-space-robotics-link-checker/1.0; +https://github.com/snt-spacer/awesome-space-robotics)"

SOFT_FAIL_CODES = {400, 403, 429, 503}


def extract_urls() -> list[tuple[str, int, str]]:
    results: list[tuple[str, int, str]] = []
    for md_file in sorted(SRC_DIR.rglob("*.md")):
        rel_path = str(md_file.relative_to(REPO_ROOT))
        for line_num, line in enumerate(
            md_file.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for match in URL_RE.finditer(line):
                results.append((rel_path, line_num, match.group(1)))
    return results


def _request(url: str, method: str) -> int:
    req = Request(url, method=method, headers={"User-Agent": USER_AGENT})
    resp = urlopen(req, timeout=TIMEOUT)
    status = resp.status
    resp.close()
    return status


def check_url(url: str) -> tuple[str, str, str]:
    for attempt in range(RETRIES):
        try:
            _request(url, "HEAD")
            return (url, "ok", "")
        except HTTPError as e:
            if e.code == 405:
                try:
                    _request(url, "GET")
                    return (url, "ok", "")
                except HTTPError as e2:
                    code = e2.code
                except (URLError, TimeoutError, OSError) as e2:
                    if attempt < RETRIES - 1:
                        time.sleep(RETRY_DELAY)
                        continue
                    return (url, "warning", str(e2))
            else:
                code = e.code

            if code in SOFT_FAIL_CODES:
                if attempt < RETRIES - 1:
                    time.sleep(RETRY_DELAY)
                    continue
                return (url, "warning", f"HTTP {code}")
            return (url, "error", f"HTTP {code}")
        except (URLError, TimeoutError, OSError) as e:
            if attempt < RETRIES - 1:
                time.sleep(RETRY_DELAY)
                continue
            return (url, "warning", str(e))

    return (url, "warning", "max retries exceeded")


def main() -> int:
    entries = extract_urls()
    if not entries:
        return 0

    unique_urls = sorted(set(url for _, _, url in entries))
    url_locations: dict[str, list[tuple[str, int]]] = {}
    for filepath, line_num, url in entries:
        url_locations.setdefault(url, []).append((filepath, line_num))

    print(f"Checking {len(unique_urls)} unique URLs...")

    results: dict[str, tuple[str, str]] = {}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(check_url, url): url for url in unique_urls}
        for future in as_completed(futures):
            url, status, detail = future.result()
            results[url] = (status, detail)

    errors: list[tuple[str, int, str, str]] = []
    warnings: list[tuple[str, int, str, str]] = []
    for url in unique_urls:
        status, detail = results[url]
        if status == "error":
            for filepath, line_num in url_locations[url]:
                errors.append((filepath, line_num, url, detail))
        elif status == "warning":
            for filepath, line_num in url_locations[url]:
                warnings.append((filepath, line_num, url, detail))

    if warnings:
        warnings.sort()
        print(f"\n{len(warnings)} URL(s) returned warnings (may be transient):\n")
        for filepath, line_num, url, detail in warnings:
            print(f"  {filepath}:{line_num}  {url}")
            print(f"    {detail}\n")

    if errors:
        errors.sort()
        print(f"{len(errors)} broken URL(s) found:\n")
        for filepath, line_num, url, detail in errors:
            print(f"  {filepath}:{line_num}  {url}")
            print(f"    {detail}\n")
        return 1

    print("All URLs are reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
