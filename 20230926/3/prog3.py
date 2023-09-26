a = [list(eval(input()))]
n = len(a[0])
for i in range(1, n):
    a.append(list(eval(input())))
b = []
for i in range(n):
    b.append(list(eval(input())))
c = []
for i in range(n):
    c.append([])
    for j in range(n):
        ans = 0
        for k in range(n):
            ans += a[i][k] * b[k][j]
        c[i].append(ans)
for i in c:
    print(*i, sep=',')
