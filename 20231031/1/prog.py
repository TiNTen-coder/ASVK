class Omnibus:
    _global_dict = {}

    def __init__(self):
        self._local_set = set()

    def __getattribute__(self, item):
        if item in {"_local_set", '__dict__', '_global_dict'}:
            return object.__getattribute__(self, item)
        if item[0] != '_':
            return object.__getattribute__(self, "_global_dict")[item]

    def __setattr__(self, key, value):
        if key == "_local_set":
            self.__dict__["_local_set"] = set()
        if key[0] != '_' and key not in self._local_set:
            self._local_set.add(key)
            self._global_dict[key] = self._global_dict.setdefault(key, 0) + 1

    def __delattr__(self, item):
        if item in self._local_set:
            self._global_dict[item] -= 1
            self._local_set.remove(item)

import sys
exec(sys.stdin.read())
