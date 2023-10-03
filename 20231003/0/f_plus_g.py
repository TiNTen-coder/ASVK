def func(f, g):
    def h(x):
        return f(x) + g(x)
    return h

print(func(lambda x: x * 3, lambda y: y ** 2)(2))
