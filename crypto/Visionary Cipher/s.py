alphabets = "abcdefghijklmnopqrstuvwxyz0123456789_{}"
c = "ig3piomvwfactgk3}fagot0vossega4btwof8x"
key = '?' * 10
flag = "flag{" + (len(c) - len("flag{}")) * '?' + "}"
md5_hash = "17382b1a9caad37bd127f2a7984ccbb9"

print("charset:", alphabets)
print("ciphertext:", c)
print("key:", key)
print("flag:", flag)
print("md5(flag):", md5_hash)
