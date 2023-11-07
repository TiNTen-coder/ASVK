class A:
    def __init__(self, var):
        self.var = var

    def __add__(self, other):
        return self.__class__(self.var + other)

class B(A):
    def __str__(self):
        return f"<{self.var}>"


a = B(12)
print(a)
print(a + 1)
