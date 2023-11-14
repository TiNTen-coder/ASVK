class Man:
    @property
    def age(self, start_age):
        pass
    @age.setter
    def age(self, val):
        if val <= 128:
            self._age = val
        else:
            print('too old!')
            raise ValueError
        return self._age

    @age.getter
    def age(self):
        if self._age == 42:
            print('secret value!')
            return -1
        return self._age

c = Man()
c.age = 52
print(c.age)
try:
    c.age = 255
except ValueError:
    pass
print(c.age)

