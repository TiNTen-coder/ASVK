a = eval(input())
for i in a:
    if i & 1:
        print(i)
        break
else:
    print(a[-1])
