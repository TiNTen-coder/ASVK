class final(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError(f"More than one parent")
        print('Parent created')
        return super().__new__(metacls, name, parents, namespace)
class E(metaclass=final): pass
#class C: pass
#class A(C, E): pass
