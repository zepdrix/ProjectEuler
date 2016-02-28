sum_square = 0

square_sum = 0

x = 1

def sum_square(x):
	sum = 0
	for i in range(1, x + 1):
		sum += i*i
	return sum

def square_sum(x):
	square = 0
	for i in range(1, x + 1):
		square += i
	return square * square
	
print square_sum(100) - sum_square(100)