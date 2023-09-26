matrix = []
n = 0
while elem := input():
    matrix.append(eval(elem))
    n += 1
if all([len(i) == n for i in matrix]):
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
for i in matrix:
    print(*i)
