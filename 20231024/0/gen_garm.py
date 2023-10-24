def garm(n):
    a = 0
    for i in range(1, n + 1):
        a += 1 / (i * i)
        yield a

print(list(garm(int(input()))))
