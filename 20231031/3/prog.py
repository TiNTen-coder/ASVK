import sys


class Maze:
    def __init__(self, n):
        self.n = n
        self.a = [['█'] * (2 * n + 1) for i in range(2 * n + 1)]
        for i in range(1, 2 * n + 1, 2):
            for j in range(1, 2 * n + 1, 2):
                self.a[i][j] = '·'
    
    def __setitem__(self, item, value):
        x0 = item[0]
        y1 = item[-1]
        y0, x1 = item[1].start, item[1].stop
        if x0 == x1:
            for i in range(2 * min(y0, y1) + 1, 2 * max(y0, y1) + 2):
                self.a[i][2 * x0 + 1] = value
        elif y0 == y1:
            for i in range(2 * min(x0, x1) + 1, 2 * max(x0, x1) + 2):
                self.a[2 * y0 + 1][i] = value

    def __getitem__(self, item):
        a = []
        for i, j in enumerate(self.a):
            a.append([])
            for j in j:
                a[i].append(j)
        def req(x, y, ans_x, ans_y):
            a[y][x] = '█'
            res_1 = False
            res_2 = False
            res_3 = False
            res_4 = False
            if x == ans_x and y == ans_y:
                return True
            if a[y + 1][x] == '·': 
                res_1 = req(x, y + 1, ans_x, ans_y)
            if a[y - 1][x] == '·':
                res_2 = req(x, y - 1, ans_x, ans_y)
            if a[y][x + 1] == '·':
                res_3 = req(x + 1, y, ans_x, ans_y)
            if a[y][x - 1] == '·':
                res_4 = req(x - 1, y, ans_x, ans_y)
            return res_1 or res_2 or res_3 or res_4
        x0 = item[0]
        y1 = item[-1]
        y0, x1 = item[1].start, item[1].stop
        if self.a[2 * y0 + 1][2 * x0 + 1] == '█' or self.a[2 * y1 + 1][2 * x1 + 1] == '█':
            return False
        return req(2 * x0 + 1, 2 * y0 + 1, 2 * x1 + 1, 2 * y1 + 1)

    def __str__(self):
        return '\n'.join(list(map(lambda x: ''.join(x), self.a)))

sys.setrecursionlimit(5000000)
import sys
exec(sys.stdin.read())
