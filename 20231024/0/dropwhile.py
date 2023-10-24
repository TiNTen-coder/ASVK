from itertools import *


def cusm():
    s = 0
    for i in count(1):
        yield (s := s + 1 / (i * i))

ite = dropwhile(lambda x: x < 1.6, cusm())
print(*list(next(ite) for i in range(10)), sep='\n')
