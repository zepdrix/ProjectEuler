import timeit, math

start = timeit.default_timer()

def is_prime(x):
	#determines if x is prime or not
	for i in range(2,x/2):
		if x % i == 0:
			return False
	return True

def prime_factors(x):
	#returns a list of factors of x
	i = 2
	list = []
	y = x
	while i <= (y):
		if x % i == 0:
			print i
			if is_prime(i):
				list.append(i)
				x = x/i
			else:
				i += 1
		else:
			i += 1
	return list

def create_product(x):
	#creates a dictionary of prime factors and the max number of occurrences in a single number, then multiplies them to return a smallest evenly divisible product
	dict = {}
	product = 1
	for i in range(2,x + 1):
		for prime in prime_factors(i):
			if prime in dict:
				while prime_factors(i).count(prime) > dict[prime]:
					dict[prime] += 1
			else:
				dict[prime] = prime_factors(i).count(prime)
	for j in dict:
		product *= j**dict[j]
	print dict, product
	

		
print create_product(20)


stop = timeit.default_timer()

print stop - start