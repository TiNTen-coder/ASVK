import struct
import random
import sys

b = b'abc'
n = random.randrange(1000000)
f = random.randrange()
for fmt, name in ('<f3si', sys.argv[1]), ('!3si', sys.argv[2]):
    with open(sys.argv[1], 'wb') as f:
        for i in range(10):
            f.write(struct.pack(fmt, random.random(), bytes(b), n))

