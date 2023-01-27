from pwn import *
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

io = remote("localhost", 1234)
r = io.recv().decode().strip().split("\n")
io.close()

p = int(r[0].split(":")[1])
g = int(r[1].split(":")[1])
message = r[-1].split(":")[1].strip()

password = g.to_bytes((g.bit_length() + 7) // 8, "big")
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=b"\x00" * 8,
    iterations=100000,
    backend=default_backend(),
)
key = base64.urlsafe_b64encode(kdf.derive(password))
f = Fernet(key)
token = f.decrypt(message)

print(token.decode())
