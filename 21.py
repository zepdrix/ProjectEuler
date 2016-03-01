def factor(number):
#returns the proper divisors of number in a list
	i = 1
	f = 0
	factors = []
	for i in xrange(1, (number/2) + 1):
		if number % i == 0:
			f += 1
			factors.append(i)
		i += 1
	return factors
	
def is_amicable(a):
#returns true if a is an amicable number
	b = sum(factor(a))
	if sum(factor(b)) == a and a != b:
		return True
	else:
		return False

amicable = []
		
for x in xrange(1, 10000):
	if is_amicable(x):
		amicable.append(x)
		
print sum(amicable)