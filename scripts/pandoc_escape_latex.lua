function RawInline(el)
  if el.format == "latex" or el.format == "tex" then
    el.text = el.text:gsub("(\\part%s*{)(.-)(})", function(pre, title, post)
      return pre .. title:gsub("&", "\\&") .. post
    end)
    return el
  end
end
