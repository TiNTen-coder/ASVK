from math import *

def Calc(s, t, u):
    def h(z):
        x = (lambda x: eval(s))(z)
        y = (lambda x: eval(t))(z)
        return eval(u)
    return h
f = Calc(*eval(input()))
print(f(eval(input())))
