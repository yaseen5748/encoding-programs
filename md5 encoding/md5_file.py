import hashlib
with open("sample.txt","rb") as f:
    bytes = f.read()
print("Bytes read from the file:",bytes)
result = hashlib.md5(bytes)
print("Hash Value: ",result)
print("The hexadecimal equivalent: ")
print(result.hexdigest())