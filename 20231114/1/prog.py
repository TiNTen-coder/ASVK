def objcount(cls):
    class Dec(cls):
        cls.counter = 0

        def __init__(self, *args, **kwargs):
            if '__init__' in dir(cls):
                super().__init__(*args, **kwargs)
            self.__class__.counter += 1

        def __del__(self):
            if '__del__' in dir(cls):
                super().__del__()
            self.__class__.counter -= 1

    return Dec

import sys
exec(sys.stdin.read())
