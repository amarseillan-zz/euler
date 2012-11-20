def collatz( n ):
	it = 1
	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		it = it + 1
	return it
	
def f_max( n, m ):
	if n > m:
		return n
	return m

def problem14( n ):
	max, maxn = 0,0
	for i in range(1, n):
		aux = collatz(i)
		if aux > max:
			max = aux
			maxn = i
		if i % 100000 == 0:
			print i/100000
	return maxn
	
print problem14(1000000)