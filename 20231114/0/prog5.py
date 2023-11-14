class C:
    @property
    def field(self):
        return 'QQ'

    @field.setter
    def field(self, value):
        self._val = value

c = C()
c.field = 123123123
