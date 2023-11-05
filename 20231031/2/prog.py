class Triangle:
    def __init__(self, A, B, C):
        A = tuple(A)
        B = tuple(B)
        C = tuple(C)
        self.A = A
        self.B = B
        self.C = C
        self.x1 = A[0]
        self.y1 = A[1]
        self.x2 = B[0]
        self.y2 = B[1]
        self.x3 = C[0]
        self.y3 = C[1]

    def __abs__(self):
        if self.x1 == self.x2 == self.x3 or self.y1 == self.y2 == self.y3:
            return 0
        if self.A == self.B or self.A == self.C or self.B == self.C:
            return 0
        if (self.y3 - self.y1) * (self.x2 - self.x1) == (self.x3 - self.x1) * (self.y2 - self.y1):
            return 0
        return abs((self.x1 - self.x3) * (self.y2 - self.y3) - (self.x2 - self.x3) * (self.y1 - self.y3)) / 2

    def __bool__(self):
        return abs(self) != 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __eq__(self, other):
        return abs(self) == abs(other)

    def __contains__(self, item):
        if sorted([self.A, self.B, self.C]) == sorted([item.A, item.B, item.C]):
            return True
        if not item:
            return True
        if not self:
            return False
        return __class__.point_in_triangle(self, item.A) and __class__.point_in_triangle(self, item.B) and __class__.point_in_triangle(self, item.C)

    def point_in_triangle(self, point):
        return abs(self) == abs(Triangle(self.A, self.B, point)) + abs(
            Triangle(self.A, self.C, point)) + abs(Triangle(self.B, self.C, point))

    def point_on_line(self, point):
        first = (self.B[1] - self.A[1]) * (point[0] - self.A[0]) == (self.B[0] - self.A[0]) * (point[1] - self.A[1])
        second = (self.C[1] - self.A[1]) * (point[0] - self.A[0]) == (self.C[0] - self.A[0]) * (point[1] - self.A[1])
        third = (self.C[1] - self.B[1]) * (point[0] - self.B[0]) == (self.C[0] - self.B[0]) * (point[1] - self.B[1])
        return first or second or third

    def __and__(self, other):
        if not self or not other:
            return False

        if self in other:
            if __class__.point_on_line(other, self.A) or \
                    __class__.point_on_line(other, self.B) or \
                    __class__.point_on_line(other, self.C):
                return True
            return False

        if other in self:
            if __class__.point_on_line(self, other.A) or \
                    __class__.point_on_line(self, other.B) or \
                    __class__.point_on_line(self, other.C):
                return True
            return False

        if __class__.point_in_triangle(self, other.A) or \
            __class__.point_in_triangle(self, other.B) or \
            __class__.point_in_triangle(self, other.C) or \
            __class__.point_in_triangle(other, self.A) or \
            __class__.point_in_triangle(other, self.B) or \
            __class__.point_in_triangle(other, self.C):
            return True

        return __class__.intersection([self.A, self.B], [other.A, other.B]) or \
            __class__.intersection([self.A, self.B], [other.A, other.C]) or \
            __class__.intersection([self.A, self.B], [other.B, other.C]) or \
            __class__.intersection([self.A, self.C], [other.A, other.B]) or \
            __class__.intersection([self.A, self.C], [other.A, other.C]) or \
            __class__.intersection([self.A, self.C], [other.B, other.C]) or \
            __class__.intersection([self.B, self.C], [other.A, other.B]) or \
            __class__.intersection([self.B, self.C], [other.A, other.C]) or \
            __class__.intersection([self.B, self.C], [other.B, other.C])

    def intersection(line1, line2):
        def distance(x1, y1, x2, y2):
            return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)

        def line(p1, p2):
            A = (p1[1] - p2[1])
            B = (p2[0] - p1[0])
            C = (p1[0] * p2[1] - p2[0] * p1[1])
            return A, B, -C

        def inter(L1, L2):
            D = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x, y
            else:
                return False

        ans = inter(line(*line1), line(*line2))
        if isinstance(ans, bool):
            return ans
        x, y = ans
        return distance(line1[0][0], line1[0][1], line1[1][0], line1[1][1]) == distance(line1[0][0], line1[0][1], x, y) + distance(line1[1][0], line1[1][1], x, y) and \
            distance(line2[0][0], line2[0][1], line2[1][0], line2[1][1]) == distance(line2[0][0], line2[0][1], x, y) + distance(line2[1][0], line2[1][1], x, y)


import sys
exec(sys.stdin.read())
