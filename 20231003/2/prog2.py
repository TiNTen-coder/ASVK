def subtract(a, b):
    if isinstance(a, tuple) or isinstance(b, list):
        ans = []
        for i in a:
            if i not in b:
                ans.append(i)
        return type(a)(ans)
    return a - b

print(subtract(*eval(input())))
