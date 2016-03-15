def character_check(num):
	#returns the number of digits in num
	return len(str(num))
	
def fib_len(n):
	#keeps adding terms to a Fibonacci sequence until the last number in the sequence has n digits
	fibs = [1, 1]
	while character_check(fibs[-1]) != n:
		fibs.append(fibs[-2]+fibs[-1])
	return len(fibs)
	
print fib_len(1000)