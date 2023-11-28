class Doubeleton(type):
    _instance = [None, None]
    def __call__(cls, *args, **kw):
        res = cls._instance.pop(0)
        if cls._instance is None:    
            cls._instance = super().__call__(*args, **kw)
        cls._instance.append(res)
        return cls._instance

class S(metaclass=Doubeleton):
    pass
print(S(), S(), S(), S())
#print(s)
#print(t)
#print(q)
#print(w)
#s.newfield = 100500
#print(f"{s.newfield=}, {t.newfield=}")
#print(f"{s is t=}")
