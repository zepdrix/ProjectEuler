import timeit, math

start = timeit.default_timer()

def distinct_powers():
	#finds all the values of a**b for a and b between 1 and 101 and returns length of list of distinct values
	list = []
	for a in range(2,101):
		for b in range(2,101):
			if a**b in list:
				pass
			else:
				list.append(a**b)
	return len(list)

print distinct_powers()


stop = timeit.default_timer()

print stop - start