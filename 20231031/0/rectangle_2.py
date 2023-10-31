class Rectangle():
    rectcnt = 0
    def __init__(self, x1, y1, x2, y2):
        Rectangle.rectcnt += 1
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f"({self.x1},{self.y1})({self.x1},{self.y2})({self.x2},{self.y2})({self.x2},{self.y1})"


Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
Rectangle(1, 2, 3, 4)
print(Rectangle.rectcnt)
