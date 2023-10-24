def walk2d():
    x = 0
    y = 0
    while True:
        dx, dy = yield (x, y) 
        x += dx
        y += dy
ite = iter(walk2d())
ite.send(None)
print(ite.send((2, 3)))
