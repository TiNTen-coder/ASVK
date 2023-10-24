import itertools

def repeater(seq, n):
    return itertools.chain.from_iterable([itertools.repeat(i, n) for i in seq])

print(list(repeater([1, 2, 3], 3)))
print(list(repeater('qwert', 5)))
