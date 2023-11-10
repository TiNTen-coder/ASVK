import collections


class DivStr(collections.UserString):
    def __init__(self, data = ''):
        super().__init__(data)

    def __floordiv__(self, other):
        count = len(self) // other
        for i in range(other):
            yield self.__class__(self[i * count:(i + 1) * count])
    
    def __mod__(self, other):
        count = len(self) % other
        return self.__class__(self[-count:]) if count else self.__class__('')

import sys
exec(sys.stdin.read())
