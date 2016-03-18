import timeit, math

start = timeit.default_timer()

denoms = [1]

def series(x):
	#generates the series of repeating numbers: 1, k, 1, 1, 2k, 1, 1, 3k...etc 
	i = 1
	k = 2
	while i < x:
		if (i-1) % 3 == 0:
			denoms.append(k)
			k += 2
		else:
			denoms.append(1)
		i += 1
	return denoms

def conv_e(x):
	#returns the numerator for the xth convergent of the fraction e
	num = 1
	if x == 1:
		return 2
	else:
		list = series(x-1)
		list.insert(0, 2)
		print list
		den = list.pop()
		while len(list) > 0:
			num, den = den, num
			num += list.pop()*den
		return num
		
def sum_num(x):
	#returns the sum of the digits of x
	sum = 0
	for i in str(x):
		sum += int(i)
		
	return sum

print sum_num(conv_e(100))s

stop = timeit.default_timer()

print stop - start