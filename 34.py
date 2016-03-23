import timeit, math

start = timeit.default_timer()

from math import factorial


def fact_sum(n):
	#returns True if n == the sum of the factorials of its digits
	sum = 0
	for digit in str(n):
		sum += factorial(int(digit))
	if sum == n:
		return True
	return False	
	
def fact_sum_check(n):
	#returns a list of all n between (and including) 3 and n if fact_sum(n) returns True
	#the upper bound must be 7 digits because 9! = 362880 so it would be impossible for the sum of x digits to be an x digit number where x > 7
	list = []
	for x in range(3,n+1):
		if fact_sum(x):
			list.append(x)
	return list

print fact_sum_check(9999999)

stop = timeit.default_timer()

print stop - start