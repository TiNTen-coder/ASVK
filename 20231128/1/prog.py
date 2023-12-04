class dump(type):
    def __new__(cls, name, parents, namespace):
        def method(func_name):
            def wrapper(self, *args, **kwargs):
                print(f'{func_name.__name__}: {args}, {kwargs}')
                return func_name(self, *args, **kwargs)

            return wrapper

        for i in namespace.keys():
            if callable(namespace[i]):
                namespace[i] = method(namespace[i])
        return super().__new__(cls, name, parents, namespace)

import sys
exec(sys.stdin.read())
