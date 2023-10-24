def fib(m, n):
    if n:
        a, b = 0, 1
        for i in range(n + m):
            a, b = b, a + b
            if i >= m:
                yield a

import sys
exec(sys.stdin.read())
