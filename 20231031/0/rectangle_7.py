class Rectangle():
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        Rectangle.rectcnt += 1
        setattr(self, f'rect_{Rectangle.rectcnt}', 0)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"
    
    def __lt__(self, other):
        return (self.y2 - self.y1) * (self.x2 - self.x1) < (other.y2 - other.y1) * (other.x2 - other.x1)
    
    def __eq__(self, other):
         return (self.y2 - self.y1) * (self.x2 - self.x1) == (other.y2 - other.y1) * (other.x2 - other.x1)
    

    def __mul__(self, other):
        return Rectangle(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
    
    def __rmul__(self, other):
        return Rectangle(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
    
    def __getitem__(self, key):
        return ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1))[key]
    
    def __bool__(self):
        return ((self.y2 - self.y1) * (self.x2 - self.x1)) != 0

    def __del__(self):
        print(f"Deleting {str(self)}")
        self.__class__.rectcnt -= 1

r1 = Rectangle(1, 2, 3, 4)
print(Rectangle.rectcnt)
if r1:
    print(True)
else:
    print(False)
del r1
print(Rectangle.rectcnt)
r2 = Rectangle(1, 1, 1, 1)
if r2:
    print(True)
else:
    print(False)
