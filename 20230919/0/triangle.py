a, b, c = eval(input())
print("Correct" if (a > 0) and (b > 0) and (c > 0) and (a < b + c) and (b < a + c) and (c < a + b) else "Incorrect")
