from itertools import islice, count, cycle, repeat

def slide(seq, n):
    if type(seq) in {count, cycle, repeat}:
        end_point = -1
    else:
        end_point = len(seq)
    counter = 0
    while end_point:
        yield from islice(seq, counter, counter + n)
        end_point -= 1
        counter += 1


import sys
exec(sys.stdin.read())
