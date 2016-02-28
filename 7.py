def find_prime(x):
#returns the xth prime
	primes = [2]
	num = 3
	pos = 0
	while len(primes) < x:
		if num % primes[pos] == 0:
			num += 2
			pos = 0
		else:
			if pos != len(primes) - 1:
				pos += 1
			else:
				primes.append(num)
				pos = 0
				num += 2
		 
	return primes[-1]
	
print find_prime(100)