from string import ascii_lowercase


class Alpha:
    __slots__ = list(ascii_lowercase)

    def __init__(self, *args, **kwargs):
        for i, j in kwargs.items():
            setattr(self, i, j)

    def __str__(self):
        ans = []
        for i in __class__.__slots__:
            if hasattr(self, i):
                ans += [f'{i}: {getattr(self, i)}']
        return ', '.join(ans)


class AlphaQ:
    __d = {}
    example = set(ascii_lowercase)

    def __init__(self, *args, **kwargs):
        for i, j in kwargs.items():
            if i not in self.example:
                raise AttributeError
            self.__d[i] = j

    def __str__(self):
        ans = []
        for i in sorted(self.example):
            if hasattr(self, i):
                ans += [f'{i}: {self.__d[i]}']
        return ', '.join(ans)

    def __setattr__(self, key, value):
        if key not in self.example:
            raise AttributeError
        self.__d[key] = value

    def __getattr__(self, item):
        if item in self.__d:
            return self.__d[item]
        raise AttributeError

import sys
exec(sys.stdin.read())

