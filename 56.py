import timeit, math

start = timeit.default_timer()

def digit_sum(x):
	#returns the sum of all digits in x
	sum = 0
	for n in str(x):
		sum += int(n)
	return sum

def digit_sum_return():
	#returns the maximum digital sum of the form a**b where a, b < 100
	max = 0
	for a in range(2,100):
		for b in range(2,100):
			if digit_sum(a**b) > max:
				max = digit_sum(a**b)
	return max

print digit_sum_return()


stop = timeit.default_timer()

print stop - start