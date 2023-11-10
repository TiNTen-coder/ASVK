class Undead(Exception):
    def __init__(self):
        pass

    def __str__(self):
        pass

class Skeleton(Undead):
    def __init__(self):
        pass

    def __str__(self):
        pass

class Zombie(Undead):
    def __init__(self):
        pass

    def __str__(self):
        pass

class Ghoul(Undead):
    def __init__(self):
        pass

    def __str__(self):
        pass

def necro(a):
    raises = {0: Skeleton, 1: Zombie, 2: Ghoul}
    raise raises[a % 3]

for i in range(*eval(input())):
    try:
        necro(i)
    except Skeleton:
        print('Skeleton')
    except Zombie:
        print('Zombie')
    except Undead:
        print('Generic Undead')


