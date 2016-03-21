import timeit, math

start = timeit.default_timer()

def inc_simp():
	#returns a list of tuples of all fractions that satisfy the problem, excludes the "trivial" results
	d = 12
	list = []
	while d < 100:
		for n in range(10, d):
			if str(n)[0] == str(d)[0] and str(n)[1] != "0" and str(d)[1] != "0":
				if float(str(n)[1])/int(str(d)[1]) == float(n)/d:
					list.append((n,d))
			if str(n)[0] == str(d)[1] and str(n)[1] != "0" and str(d)[0] != "0":
				if float(str(n)[1])/int(str(d)[0]) == float(n)/d:
					list.append((n,d))
			if str(n)[1] == str(d)[1] and str(n)[0] != "0" and str(d)[0] != "0" and str(n)[1] != "0" and str(d)[1] != "0":
				if float(str(n)[0])/int(str(d)[0]) == float(n)/d:
					list.append((n,d))
			if str(n)[1] == str(d)[0] and str(n)[0] != "0" and str(d)[1] != "0":
				if float(str(n)[0])/int(str(d)[1]) == float(n)/d:
					list.append((n,d))	
		d += 1
	return list

def simplify(a, b, c, d, e, f, g, h):
	#partially simplifies the fraction (a*b*c*d)/(e*f*g*h)
	n = a*b*c*d
	d = e*f*g*h
	print n, d
	for i in range(1, d/2 + 1):
		if n % i == 0 and d % i == 0:
			n /= i
			d /= i
			
	return n, d


print inc_simp()
print simplify(16,26,19,49,64,65,95,98)	
stop = timeit.default_timer()

print stop - start