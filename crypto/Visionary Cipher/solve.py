from pwn import *
from itertools import product
from hashlib import md5
from string import ascii_lowercase, digits

alphabets = ascii_lowercase + digits + "_{}"

io = remote("localhost", 1234)
r = io.recv().decode().strip().split("\n")
io.close()

c = r[0].split(":")[1].strip()
md5_hash = r[1].split(":")[1].strip()

flag = "flag{" + (len(c) - len("flag{}")) * "?" + "}"
key = "?" * 10
n, k, l = len(c), len(key), len(alphabets)

flag = list(flag)
key = list(key)


def pos(ch):
    return alphabets.find(ch)


def decrypt(text, key):
    k, n, l = len(key), len(text), len(alphabets)
    return "".join([alphabets[(pos(text[i]) - pos(key[i % k])) % l] for i in range(n)])


# partial key
for i in list(range(5)) + [n - 1]:
    key[i % k] = alphabets[(pos(c[i]) - pos(flag[i])) % l]

for s in product(alphabets, repeat=4):
    i = 0
    _key = key[:]

    for ch in range(k):
        if _key[ch] == "?":
            _key[ch] = s[i]
            i += 1

    _flag = decrypt(c, "".join(_key))

    if md5(_flag.encode()).hexdigest() == md5_hash:
        print(_flag)
        break
