def divisorQty( num ):
	count = 0
	for i in range(1, num+1):
		if num % i == 0:
			count = count + 1
	return count
		
def divisorQty2( num ):
	divisor = 2
	divisors = {}
	while num != 1:
		while (num % divisor) != 0 and (divisor <= num):
			divisor = divisor + 1
		if (num % divisor) == 0:
			num = num / divisor
			if not divisors.get(divisor):
				divisors[divisor] = 1
			else:
				divisors[divisor] = divisors[divisor] + 1
	result = 1
	for i in divisors.values():
		result = result * (i+1)
	return result



def triangleNumber( n ):
	return n*(n+1)/2 #12 x 13 /2 has divisorQty(12)-1. 
	
def problem12( divisors ):
	num = 1
	while divisors >= divisorQty2( triangleNumber( num ) ):
		num = num + 1
	return triangleNumber( num )
		
answer = problem12(500)
print answer
#print divisorQty2( answer )
#print divisorQty2( 5000000 )