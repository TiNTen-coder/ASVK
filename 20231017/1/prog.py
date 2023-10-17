s = input().lower()
d = set()
for i in range(1, len(s)):
    if s[i - 1].isalpha() and s[i].isalpha():
        d.add(s[i - 1] + s[i])
print(len(d))

