import timeit

start = timeit.default_timer()

collatzs = {}

def collatz_chain(x):
#returns the number of terms in a collatz sequence for x
	i = 1
	d = x
	while x != 1:
		i += 1
		if x in collatzs:
			collatzs[d] = i + collatzs[x] - 2
			return i + collatzs[x] - 2
		elif x % 2 ==0:
			x = x / 2
		else:
			x = (3 * x) + 1
	
	collatzs[d] = i
	return i

def longest_collatz(number):
#returns the number with the longest collatz sequence along with the number of terms less than the input number
	longest = [1, 1]
	for x in xrange(number, 1, -1):
		if (3 * x) + 1 > number:
			if collatz_chain(x) > longest[1]:
				longest = [x, collatz_chain(x)]
	return longest
	
print longest_collatz(1000000)

stop = timeit.default_timer()

print stop - start