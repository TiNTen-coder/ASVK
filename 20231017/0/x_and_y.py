import sys
expr, (a, b) = sys.argv[1], eval(' '.join(sys.argv[2:]))
print(eval(expr, {'x': a, 'y': b}))
print(eval(expr, {'x': b, 'x': a}))
