while (n := input()):
	if isinstance(eval(n), int):
		if not eval(n) & 1:
			print(n)
		elif eval(n) == 13:
			break
else:
	print('Congrats!')
