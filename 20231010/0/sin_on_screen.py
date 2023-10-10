from math import sin


def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A


N = 30
W, H = 60, 20
A, B = -5, 5
ans = [['.'] * W for i in range(H)]
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = sin(x)
    w = scale(-1, 1, H - 1, 0, y)
    ans[int(w)][i] = '*'
    #print(int(w) * ' ', '*')

print('\n'.join(["".join(i) for i in ans]))
