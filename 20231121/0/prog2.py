import sys


txt = ''
with open(sys.argv[1], "r") as f:
    txt = f.read()

for i in range(len(txt) // 3 + (len(txt) % 3 > 0)):
    print(txt[i], end='')
print()
