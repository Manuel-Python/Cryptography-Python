import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self): #Linear congruential generator
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256

def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

def transmit(cipher, likely):
    b = []
    for c in cipher:
        if random.randrange(0, likely) == 0:
            c = c ^ 2**random.randrange(0,8)
        b.append(c)
    return bytes(b)

def modification(cipher):
    mod = [0]*len(cipher)
    mod[10] = ord(' ') ^ ord('1')
    mod[11] = ord(' ') ^ ord('0')
    mod[12] = ord('1') ^ ord('0')
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

def modify(cipher):
    mod = [0]*len(cipher)
    mod[9] = 1
    return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])

def get_key(message, cipher):
    return bytes([message[i] ^ cipher[i] for i in range(len(cipher))])

def crack(key_stream, cipher):
    length = min(len(key_stream), len(cipher))
    return bytes([key_stream[i] ^ cipher[i] for i in range(length)])

def brute_force(plain, cipher):
    for k in range(2**31):
        bf_key = KeyStream(k)
        for i in range(len(plain)):
            xor_value = plain[i] ^ cipher[i]
            if xor_value != bf_key.get_key_byte():
                break
        else:
            return k
        #return False




#key = KeyStream(10)
key = KeyStream
# for i in range(10):
#     print(key.get_key_byte())
#message = "Hello World! I am here to declair that I am going to take over".encode()
#message = "Send Bob:   10$".encode()
eves_message = "This is eve's most valued secrets of all her life.".encode()
message = eves_message
print(message)
cipher = encrypt(key,message)
print(cipher)

#cipher = transmit(cipher, 5)
#cipher = modification(cipher)

key = KeyStream(10)
message = encrypt(key,cipher)
print(message)

eves_key_stream = get_key(eves_message, cipher)

#Alice again
secret_key = random.randrange(0, 2**20)
print("Secret key",secret_key)
header = "MESSAGE: "
message = "Hi Bob, lets plan our world domination".encode()
key = KeyStream(secret_key)
cipher = encrypt(key,message)
print(cipher)

#Bob again
key = KeyStream(10)
message = encrypt(key,cipher)
print(message)

#Eve again
print("This is Eve")
#print(crack(eves_key_stream,cipher))
bf_key = brute_force(header.encode(),cipher)
print("Eve's brute force key:",bf_key)
key = KeyStream(bf_key)
message = encrypt(key,cipher)
print(message)

# from pyDes import *
#
#
# def modify(cipher):
#     # insert code here
#     mod = [0]*len(cipher)
#     mod[9] = 1
#     return bytes([mod[i] ^ cipher[i] for i in range(len(cipher))])
#
#
# message = "Give Bob:    10$ and send them to him"
# key = "DESCRYPT"
# iv = bytes([0]*8)
# k = des(key, CBC, iv, pad=None, padmode=PAD_PKCS5)
#
#
# # Alice sending the encrypted message
# cipher = k.encrypt(message)
# print("Length of plain text:", len(message))
# print("Length of cipher text:", len(cipher))
# print("Encrypted:", cipher)
#
# # Bob modifying the cipher text
# cipher = modify(cipher)
#
# # this is the bank decrypting the message
# message = k.decrypt(cipher)
# print("Decrypted", cipher)
#
#
