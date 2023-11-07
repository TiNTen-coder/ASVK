def div_ab(a, b):
    return a / b

lst = eval(input())
for i, j in lst:
    try:
        print(div_ab(i, j))
    except ZeroDivisionError:
        print('inf')
