import urllib.parse

query = "Think and wonder, wonder and think."

encoded_query = urllib.parse.quote_plus(query)

print("Original Query:",  query)
print("Encoded query: ", encoded_query)