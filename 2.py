fib1 = 1
fib0 = 1
fib2 = 0
sum = 0

while fib2 < 4000000:
	fib2 = fib0 + fib1
	fib0, fib1 = fib1, fib2
	if fib2 % 2 == 0:
		sum += fib2

print sum