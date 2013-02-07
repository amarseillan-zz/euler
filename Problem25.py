def n_digits(n):
	return len(str(n))
	
n_1 = 1
n = 1
i = 2
while( n_digits(n) < 1000 ):
	n, n_1 = n + n_1, n
	i = i + 1


print i
print n