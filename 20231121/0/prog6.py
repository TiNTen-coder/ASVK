import struct
import random
import sys

s = "<f3si"

with open(sys.argv[1], "wb") as f:
    for i in range(10):
        b = random.randrange(255), random.randrange(255), random.randrange(255)
        n = random.randrange(1000000)
        f.write(struct.pack(s, random.random(), bytes(b), n))

