import timeit, math

start = timeit.default_timer()
#summing the numbers on the diagonals is the same as adding every 2 numbers to 1, followed by every 4 numbers, followed by every 6 numbers, etc.
def find_spiral_sum(x):
	#returns the sum of all numbers on the diagonals of an x by x number spiral
	end = x * x
	sum = 1
	counter = 1
	distance = 0
	
	while counter <= end:
		distance += 2
		i = 1
		while i < 5:
			if counter >= end:
				return sum
			counter += distance
			sum += counter
			print "counter:",counter
			print "sum:", sum
			i += 1
	return sum
	
print find_spiral_sum(1001)
	
stop = timeit.default_timer()

print stop - start