from math import ceil
from fractions import Fraction

s = input()
rows = 0
gas = 0
liquid = 0
columns = len(s) - 2
while (s := input()) != '#' * (columns + 2):
    rows += 1
    gas += s[1] == '.'
    liquid += s[1] == '~'
new_liquid_line = ceil(Fraction(str(liquid) + '/' + str(liquid + gas)) * columns)
print('#' * (rows + 2))
for i in range(columns):
    print(end='#')
    if columns - i <= new_liquid_line:
        print('~' * rows + '#')
    else:
        print('.' * rows + '#')
print('#' * (rows + 2))
pretty_print = 2 + len(str(max(liquid, gas) * columns)) + len(str((liquid + gas) * columns))
if liquid < gas:
    dots = '.' * 20
    ans = str(gas * columns) + '/' + str((liquid + gas) * columns)
    print(f'{dots}{ans:>{pretty_print}}')
    tildas = '~' * round(20 * Fraction(str(liquid) + '/' + str(gas)))
    ans = str(liquid * columns) + '/' + str((liquid + gas) * columns)
    print(f'{tildas}{ans:>{pretty_print + 20 - len(tildas)}}')
else:
    dots = '.' * round(20 * Fraction(str(gas) + '/' + str(liquid)))
    ans = str(gas * columns) + '/' + str((liquid + gas) * columns)
    print(f'{dots}{ans:>{pretty_print + 20 - len(dots)}}')
    tildas = '~' * 20
    ans = str(liquid * columns) + '/' + str((liquid + gas) * columns)
    print(f'{tildas}{ans:>{pretty_print}}')

