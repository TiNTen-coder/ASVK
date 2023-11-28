match input().split():
    case ['a']:
        print('A!')
    case ['a', var]:
        print('AAAA', var)
    case [*vars, 'A']:
        print(vars, 'A!!!')
    case _:
        print('WAT')


