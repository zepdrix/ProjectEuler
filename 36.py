import timeit, math

start = timeit.default_timer()

def is_palindrome(x):
	#returns True if base 10 integer x is a palindrome and x in base 2 is also a palindrome. else false
	pal = ""

	for i in str(x):
		pal = i + pal
		
	if int(pal) == int(x):
		pal = ""
		for j in bin(x)[2:]:
			pal = j + pal
		
		if pal == bin(x)[2:]:
			return True
			
	return False


def find_sum(x):
	#finds the sum of all numbers less than x that are palindromes in base 10 and base 2 
	i = 1
	sum = 0
	for num in range(1,x):
	
		if is_palindrome(num):
		
			sum += num
	return sum
	
print find_sum(1000000)

stop = timeit.default_timer()

print stop - start