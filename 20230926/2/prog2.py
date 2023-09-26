a = list(eval(input()))
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] * a[i] % 100 < a[j] * a[j] % 100:
            a[i], a[j] = a[j], a[i]
print(a)
