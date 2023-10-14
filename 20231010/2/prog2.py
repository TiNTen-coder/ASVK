from math import *
from fractions import Fraction


def scale(a, b, A, B, x):
    return (x - a) * (B - A) / (b - a) + A


W, H, A, B, func = input().split()
W = int(W) * 2
H = int(H)
A = int(A)
B = int(B)
ans = [[' '] * W for i in range(H)]
maximum = -inf
minimum = inf
x = 0
for j in range(A, B + 1):
    x = j
    try:
        res = eval(func)
    except ZeroDivisionError:
        x = 0.00000000001
        res = eval(func)
    if res > maximum:
        maximum = res
    if res < minimum:
        minimum = res
for i in range(W):
    x = scale(0, W - 1, A, B, i)
    y = eval(func)
    w = scale(floor(Fraction(str(minimum))), ceil(Fraction(str(maximum))), H - 1, 0, y)
    try:
        ans[int(w)][i] = '*'
    except IndexError:
        pass

print('\n'.join(["".join(i) for i in ans]))

