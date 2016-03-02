import timeit, math

start = timeit.default_timer()

sum = 0

for x in str(math.factorial(100)):
	sum += int(x)

print sum

stop = timeit.default_timer()

print stop - start