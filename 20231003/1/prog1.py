def Pareto(*args):
    if type(args[0]) == int:
        return args
    ans = []
    for i in range(len(args)):
        flag = True
        for j in range(len(args)):
            if i != j and (args[i][0] < args[j][0] and args[i][1] <= args[j][1]) or (args[i][0] <= args[j][0] and args[i][1] < args[j][1]):
                flag = False
        if flag:
            ans.append(args[i])

    return tuple(ans)

print(tuple(Pareto(*eval(input()))))
