while (n := input()):
    if isinstance(eval(n), int) and not eval(n) & 1:
        print(n)
