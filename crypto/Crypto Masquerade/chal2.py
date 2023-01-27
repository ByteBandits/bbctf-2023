import base64
import random

from Crypto.Util import number
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# with open("seed.txt", "r") as f:
# SEED = int(f.read()) % (2**32)
BIT_L = 2**5
SEED = 0

with open("flag.txt", "r") as f:
    FLAG = f.read()


def secure_random(k):
    for _ in range(k - 1):
        random.randrange(0, 2**BIT_L)
        # print("random : ", random.randrange(0, 2**BIT_L))
    return random.randrange(0, 2**BIT_L)


def generate_secrets(k):
    random.seed(SEED)
    p = number.getPrime(BIT_L + 1)
    g = secure_random(k)
    a = secure_random(k)
    b = secure_random(k)
    return p, g, a, b


def main():
    # random.seed(SEED)
    k = int(input("Enter they security level :"))
    p, g, a, b = generate_secrets(k)

    A = pow(g, a, p)
    B = pow(g, b, p)

    # print(a,b)

    print("p :", p)
    print("g :", g)
    print("A :", A)
    print("B :", B)

    key = pow(A, b, p)
    print("key :", key)

    password = key.to_bytes((key.bit_length() + 7) // 8, "big")
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        length=32,
        salt=b"\x00" * 8,
        iterations=100000,
        backend=default_backend(),
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    token = f.encrypt(FLAG.encode("ascii"))

    print("message : ", token.decode())


if __name__ == "__main__":
    main()
