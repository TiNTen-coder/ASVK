n = int(input())
summary = n
while (summary < 22) and (n > 0):	
	n = int(input())
	summary += n
else:
	if summary > 21:
		print(summary)
	else:
		print(n)
