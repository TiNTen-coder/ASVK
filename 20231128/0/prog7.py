from inspect import get_annotations

class A:
    param: int
    def __init__(self, new_param: int):
        if isinstance(new_param, get_annotations(A)['param']):
            self.param = new_param
        else:
            raise TypeError

print(A(1))
print(A('1'))
