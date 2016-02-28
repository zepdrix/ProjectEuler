from math import sqrt

def factor(number):
	i = 1
	f = 0
	factors = []
	for i in xrange(1, number + 1):
		if number % i == 0:
			f += 1
			factors.append(i)
		i += 1
	return factors

def isprime(number):
	prime = True
	x = 2
	while x <= int(sqrt(number)):
		if number % x == 0:
			prime = False
			break
		else:
			x += 1
	return prime
			
def largestprimefactor(number):
	list = factor(number)
	primes = []
	for x in list:
		if isprime(x):
			primes.append(x)
	primes.sort()
	return primes[-1]
	
print largestprimefactor(600851475143 )