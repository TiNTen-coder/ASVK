from itertools import product
print(*sorted(filter(lambda x: x.count('TOR') == 2, list(map(lambda y: ''.join(y), product(list('TOR'), repeat=int(input())))))), sep=', ')
