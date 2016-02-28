def if_palindrome(x):
#returns True if x is a palindrome, otherwise returns False
	backwards = ""
	for i in str(x):
		backwards = i + backwards
	if backwards == str(x):
		return True
	else:
		return False

palindromes = []

for x in range(100, 1000):
	for y in range(100, 1000):
		if if_palindrome(x * y) == True:
			palindromes.append(x * y)

palindromes.sort()

print palindromes[-1]