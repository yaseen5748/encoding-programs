import html
a_string = "<body>"

encoded_string = html.escape(a_string)

print(encoded_string)


b_string = "&lt;body&gt"

decoded_string = html.unescape(b_string)

print(decoded_string)
