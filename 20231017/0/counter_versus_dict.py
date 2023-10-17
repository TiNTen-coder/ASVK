from collections import Counter
import timeit

def dct(s):
    d = {}
    for i in s.split():
        d[i] = d.setdefault(i, 0) + 1
    return d


def cnt(s):
    c = Counter(s.split())
    return c


s = input()
print("With dict()", timeit.Timer("dct(s)", globals=globals()).autorange())
print("With Counter()", timeit.Timer("cnt(s)", globals=globals()).autorange())
