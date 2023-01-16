import base64


sample_string = "hello"
sample_string_bytes = sample_string.encode('ascii')
base64_bytes = base64.b64encode(sample_string_bytes)
base64_string = base64_bytes.decode("ascii")

print("encoded string: ", base64_string)
print("encoded string: ", base64_bytes)
print("encoded string: ", sample_string_bytes)