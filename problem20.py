	
def fact(n):
	if n == 0:
		return 1
	return n * fact(n-1)
	
string = str(fact(100))
ans = 0
for c in string:
	ans = ans + int(c)
print ans