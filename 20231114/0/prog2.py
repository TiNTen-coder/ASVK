def multicall(times):
    def decorator(fun):
        def newfun(*args):
            for i in args:
                if not isinstance(i, times):
                    raise TypeError
            return True
        return newfun
    return decorator

@multicall(int)
def simplefun(a, b):
    return a * b

print(simplefun(4, 5))
