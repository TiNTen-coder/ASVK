class S:
    __slots__ = ['x']

class R:
    __init__(self, val)


s = S()
r = R()
r.x = 100500
s.x = 100500
import sys
print(sys.getsizeof(r))
print(sys.getsizeof(s))

