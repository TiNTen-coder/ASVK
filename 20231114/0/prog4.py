class Decs:
    def __get__(self, obj, cls):
        print('GET', f'{repr(obj)}', f'{repr(cls)}')
        return obj._val

    def __set__(self, obj, val):
        print('SET', f'{repr(obj)}', f'{repr(val)}')
        obj._val = val
    
    def __delete__(self, obj):
        print('DELETE', f'{repr(obj)}')
        obj._value = None

class C:
    data = Decs()
    
    def __init__(self, name):
        self.ata = name

    def __str__(self):
        return f'<{self.data}>'

c = C(123)
print(dir(c))
c.data = 123
print(c.data)
