from pyDes import *

message = "0123456701234567"
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5) #ecb CBC

cipher = k.encrypt(message)
print("Length of cipher text:", len(cipher))
print("Length of plain text:", len(message))
print("Encrypted:",cipher[0:0])
print("Encrypted:",cipher[8:16])
print("Encrypted:",cipher[16:])
message = k.decrypt(cipher)
print("Decrypted:",message)