import timeit, math

start = timeit.default_timer()

def is_prime(x):
	#determines if x is prime or not
	for i in range(2,x/2):
		if x % i == 0:
			return False
	return True

def factors(x):
	#returns a list of factors of x
	i = 1
	list = []
	helper = 1
	while helper <= (x/2):
		if (x/helper) % i == 0:
			list.append(i)
			helper *= i
		i += 1
	return list

def find_largest(x):
	#finds largest prime in a list of integers
	x.sort()
	x.reverse()
	for i in x:
		if is_prime(i):
			return i
	
		
print find_largest(factors(600851475143))


stop = timeit.default_timer()

print stop - start