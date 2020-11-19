from operator import xor
from codecs import *
# initializing string

raw = input('enter a message to encrypt:')
encoded = raw.encode("utf-8")
decoded = encoded.decode("utf-8")
print(ord(encoded))
print(encoded)
print(decoded)


"""xor1 = int.from_bytes(encoded, byteorder='little')
encrypted = xor1 ^ 11
decrypted = encrypted ^ 11
print(xor1)
print(encrypted)
print(decrypted)"""







