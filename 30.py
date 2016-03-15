from random import randint

def find_number():
	#uses randint to force an answer
	list = []
	x1 = randint(0,9)
	x2 = randint(0,9)
	x3 = randint(0,9)
	x4 = randint(0,9)
	x0 = randint(0,9)
	x6 = randint(1,9)

	while x1**5 + x2**5 + x3**5 + x4**5 + x0**5 + x6**5 != x1*1000 + x2*100 + x3*10 + x4 + x0*10000 + x6*100000:
		x1 = randint(0,9)
		x2 = randint(0,9)
		x3 = randint(0,9)
		x4 = randint(0,9)
		x0 = randint(0,9)
		x6 = randint(1,9)
		"""
		if x1*1000 + x2*100 + x3*10 + x4 + x0*10000 not in list:
			list.append(x1*1000 + x2*100 + x3*10 + x4 + x0*10000)
			print list
		"""
	return x1*1000 + x2*100 + x3*10 + x4 + x0*10000 + x6*100000

print find_number()