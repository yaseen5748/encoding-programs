import hashlib

m = hashlib.sha1()
m.update(b"The quick brown fox jumps over the lazy dog")
print(m.hexdigest())
