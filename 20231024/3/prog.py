from itertools import product
print(*sorted(list(set(filter(lambda x: x.count('TOR') == 2, list(map(lambda y: ''.join(y), product(list('TOR'), repeat=abs(int(input()))))))))), sep=', ')
