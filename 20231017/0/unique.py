import string
s = set(input())
vowels = set('aeouyi')
consonants = set(string.ascii_lowercase) - vowels
print(f"Гласных букв: {len(s & vowels)}.\nСогласных букв: {len(s & consonants)}.")
