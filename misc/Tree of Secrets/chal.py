import heapq
import os
from base64 import b64encode
from collections import Counter
from shutil import make_archive

from bitarray import bitarray

with open("flag.txt", "r") as f:
    FLAG = f.read()


class node:
    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right
        self.huff = ""

    def __lt__(self, nxt):
        return self.freq < nxt.freq


def huffman_tree(s):
    cnt = Counter(s)
    nodes = []
    for x in cnt.items():
        heapq.heappush(nodes, node(*x))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = 0
        right.huff = 1

        newNode = node("#", left.freq + right.freq, left, right)
        heapq.heappush(nodes, newNode)

    return nodes[0]


def create_directory(root, path="./root"):

    os.makedirs(path, exist_ok=True)
    m = dict()

    if root.symbol != "#":
        os.system(f"touch {path}/{root.symbol}")
        m[root.symbol] = bitarray("".join(path.split("/")[2:]))
        return m

    if root.left:
        m.update(create_directory(root.left, f"{path}/0"))
    if root.right:
        m.update(create_directory(root.right, f"{path}/1"))

    return m


def main():
    data = b64encode(FLAG.encode("ascii")).decode()
    root = huffman_tree(data)
    table = create_directory(root)
    make_archive("root", "zip", "root")

    enc = bitarray()
    enc.encode(table, data)

    with open("message", "w") as f:
        f.write(enc.to01())


if __name__ == "__main__":
    main()
