limit = 20


steper = {}
prime1 = 31
prime2 = 19
steper[limit*prime1+limit*prime2] = 1

def step( i, j ):
	if (i*prime1+j*prime2) in steper:
		return steper[i*prime1+j*prime2]
	if i > limit or j > limit:
		return 0
	else:
		if i == limit and j == limit:
			return 1
		else:
			steper[ (i+1)*prime1+j*prime2 ] = step( i+1, j )
			steper[ i*prime1+(j+1)*prime2 ] = step( i, j+1 )
			return steper[ (i+1)*prime1+j*prime2 ] + steper[ i*prime1+(j+1)*prime2 ]
			
	
	
	
	
print step( 0, 0 )