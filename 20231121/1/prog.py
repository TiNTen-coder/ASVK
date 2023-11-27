import sys
from functools import reduce

first = sys.stdin.buffer.read(1)
n = first[0]
s = sys.stdin.buffer.read()
w = []
index = 0
new_index = 0
length = len(s)
for i in range(min(n, length)):
    index = max(new_index, i * length // n)
    new_index = max(index + 1, (i + 1) * length // n)
    w.append(s[index:new_index])
sys.stdout.buffer.write(bytes([first[0]] + list(reduce(lambda x, y: x + y, list(map(lambda x: list(x), sorted(w)))))))
