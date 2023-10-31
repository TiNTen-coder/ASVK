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


q = Rectangle(1, 2, 3, 4)
w = Rectangle(1, 2, 3, 4)
e = Rectangle(1, 2, 3, 4)
r = Rectangle(1, 2, 3, 4)
t = Rectangle(1, 2, 3, 4)
y = Rectangle(1, 2, 3, 4)
u = Rectangle(1, 2, 3, 4)
i = Rectangle(1, 2, 3, 4)
print(dir(i))
print(Rectangle.rectcnt)
