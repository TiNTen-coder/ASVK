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

print(Rectangle(1, 1, 2, 2) == Rectangle(2, 2, 3, 3))
print(Rectangle(1, 2, 3, 4) < Rectangle(10, 20, 30, 40))
