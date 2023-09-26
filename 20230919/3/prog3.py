def digits_sum(n):
	ans = 0
	while n:
		ans += n % 10
		n //= 10
	return ans

n = int(input())
for i in range(n, n + 3):
	for j in range(n, n + 3):
		if digits_sum(i * j) == 6:
			s = ":=)"
		else:
			s = i * j
		print(f'{i} * {j} = {s}', end = ' ')
	print()
