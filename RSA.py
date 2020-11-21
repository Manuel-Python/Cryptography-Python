import math
import random


def is_prime(p):
    for i in range(2,int(math.sqrt(p))): #math.isqrt(p) python 3.8>
        if p % i == 0:
            return False
    return True

def get_prime(size):
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p

def lcm(a, b):
    return a*b//math.gcd(a, b)

def get_e(lamda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False

def get_d(e, lamda_n):
    for d in range(2,lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False


def factor(n):
    for p in range(2,n):
        if n % p == 0:
            return p, n//p


#key generation done by Alice(secret)
#step 1: generate 2 distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated primes",p,q)

#step 2: compute n = p*q
n = p*q
print("Modulus n:",n)

#step 3: Compute lamda(n)
lambda_n = lcm(p-1, q-1)
print("lamda n",lambda_n)

#step 4:
e = get_e(lambda_n)
print("public exponent",e)


#step 5
d = get_d(e, lambda_n)
print("Secret exponent",d)

# Done with key generation
print("Public key (e,n):",e,n)
print("Private key:", d)


#this is Bob wanting to send a message
m = 117
c = m**e % n
print("Bob sends",c)

#this is Alice decrypting the cypher
m = c**d % n
print("Alice message", m)
print()
#This is Eve
print("Eve sees the following:")
print("     Public key (e, n)", e, n)
print("     Encrypted cipher", c)

p,q = factor(n)
print("Eve: Factors",p,q)

lambda_n = lcm(p-1, q-1)
print("Eve: Lamda n", lambda_n)
d = get_d(e, lambda_n)
print("Eve: Secret exponent", d)

m = c**d % n
print("Eve: message",m)

print()
#This is Bob not being careful
print("This is Bob not being careful")
message = "Alice is awesome"

for m_c in message:
    c = ord(m_c)**e % n
    print(c," ",end='')
print()


