import string
import timeit

def ans(s):
    s = set(s)
    vowels = set('aeouyi')
    consonants = set(string.ascii_lowercase) - vowels
    return (len(s & vowels), len(s & consonants))   


s = input()
print(timeit.Timer('ans(s)', globals=globals()).autorange())
