def genf(f):
    def newfun(*args):
        try:
            assert (type(i) == int for i in args)
        except Exception:
            raise TypeError
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@genf
def fun(a,b):
    return a * 2 + b

print(fun(2, 3))

