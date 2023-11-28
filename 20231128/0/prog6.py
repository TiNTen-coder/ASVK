a, b, c = input().split()

while s := input():
    match s:
        case [a, *other] if 'yes' in other:
            print(1)
        case [b]:
            print(2)
        case [c, *_, b]:
            print(3)
