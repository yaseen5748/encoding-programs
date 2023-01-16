import hashlib

str2hash = "GeeksforGeeks"

result = hashlib.md5(str2hash.encode())

print(result.hexdigest())