class Num:
    a = set()

    def __set_name__(self, owner, name):
        self.new_name = '__' + name

    def __get__(self, obj, cls):
        if str(obj) in self.a:
            return obj.__dict__[self.new_name]
        return 0

    def __set__(self, obj, val):
        if 'real' in dir(val):
            obj.__dict__[self.new_name] = val.real
        else:
            obj.__dict__[self.new_name] = len(val)
        self.a.add(str(obj))

    def __delete__(self, obj):
        pass


import sys
exec(sys.stdin.read())

