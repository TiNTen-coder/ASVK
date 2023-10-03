def Pareto(*args):
    ans = []
    for i in range(len(args)):
        flag = True
        for j in range(len(args)):
            if i != j and (args[i][0] < args[j][0] and args[i][1] <= args[j][1]) or (args[i][0] <= args[j][0] and args[i][1] < args[j][1]):
                flag = False
        if flag:
            ans.append(args[i])

    return tuple(ans)


print(Pareto((32, 38), (10, 14), (19, 44), (31, 31), (17, 33), (53, 6), (48, 9), (6, 38), (30, 49), (52, 30), (7, 30), (45, 45), (21, 51), (7, 49), (11, 23)))

print(Pareto((1,2), (3,4), (2,2), (4,3), (7,0), (1,8)))

