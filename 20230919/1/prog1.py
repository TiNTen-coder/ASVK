n = int(input())
print('A ', end='')
if not n & 1 and not n % 25:
	print('+ ', end='')
else:
	print('- ', end='')
print('B ', end='')
if n & 1 and not n % 25:
	print('+ ', end='')
else:
	print('- ', end='')
print('C ', end='')
if not n & 3:
	print('+')
else:
	print('-')
