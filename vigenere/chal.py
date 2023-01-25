from string import ascii_lowercase, digits
from random import choices
from hashlib import md5

with open("flag.txt", "r") as f:
    FLAG = f.read()

alphabets = ascii_lowercase + digits + "_{}"
key = "".join(choices(alphabets, k=10))


def pos(ch):
    return alphabets.find(ch)


def encrypt(text, key):
    k, n, l = len(key), len(text), len(alphabets)
    return "".join([alphabets[(pos(text[i]) + pos(key[i % k])) % l] for i in range(n)])


print("c :", encrypt(FLAG, key))
print("hash :", md5(FLAG.encode("ascii")).hexdigest())


# alphabets = "abcdefghijklmnopqrstuvwxyz0123456789_{}"
# print(alphabets)
# key = "d83jk1fyjs"

# k :
# c : LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ
# c = "ig3piomvwfactgk3}fagot0vossega4btwof8x"

# 17382b1a9caad37bd127f2a7984ccbb9
