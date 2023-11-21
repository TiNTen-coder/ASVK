import pickle

class SerCls:
    lst = []
    d = {}
    num = 1
    st = ''

    def __init__(self):
        self.lst = [1]
        self.d = {'a': 2}
        self.num = 2
        self.st = "QWER"

ser = SerCls()
s = pickle.dumps(ser)
print(s)
del ser
print(s)
ser = pickle.load(s)
print(ser)
