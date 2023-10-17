d = {}
for i in input().split():
    d[i] = d.setdefault(i, 0) + 1

print(d)
