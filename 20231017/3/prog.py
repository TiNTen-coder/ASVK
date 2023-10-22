from collections import Counter


w = int(input())
d = Counter()
while s := input():
    s = s.lower()
    s = ''.join(map(lambda x: ' ' * (not x.isalpha()) + x * x.isalpha(), list(s)))
    d += Counter(s.split())
ans = []
first = -1
for i, j in d.most_common():
    if len(i) == w:
        if first in {-1, j}:
            first = j
            ans.append(i)
print(*sorted(ans))
