import timeit, math

start = timeit.default_timer()

def irrational(n):
	#keeps adding digits to Champernowne's constant until it is at least n digits long
	a = 1
	i = 0
	length = 9
	b = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	constant = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
	while length <= n:
		if i == 10:
			i = 0
			a += 1
		constant.append(str(a))
		constant.append(b[i])
		length += len(str(a)) + 1
		i += 1
		
	return constant
	
j = "".join(irrational(1000000))
print int(j[0])*int(j[9])*int(j[99])*int(j[999])*int(j[9999])*int(j[99999])*int(j[999999])
stop = timeit.default_timer()

print stop - start