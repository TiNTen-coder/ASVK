class InvalidInput(Exception):
    def __init__(self):
        pass

    def __str__(self):
        pass


class BadTriangle(Exception):
    def __init__(self):
        pass
    def __str__(self):
        pass


def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
        assert type(x1) in {int, float}
        assert type(y1) in {int, float}
        assert type(x2) in {int, float}
        assert type(y2) in {int, float}
        assert type(x3) in {int, float}
        assert type(y3) in {int, float}

    except Exception as Ex:
        raise InvalidInput
    area = abs((x1 - x2) * (y1 - y3) - (x1 - x3) * (y1 - y2)) / 2
    if not area:
        raise BadTriangle
    return area


flag = True
while flag:
    try:
        ans = triangleSquare(input())
        flag = False
    except InvalidInput:
        print('Invalid input')
    except BadTriangle:
        print('Not a triangle')
else:
    print(f'{ans:.2f}')
