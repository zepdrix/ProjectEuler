def is_palindrome(x):
#returns True if x is a palindrome, otherwise returns False
	backwards = ""
	for i in str(x):
		backwards = i + backwards
	if backwards == str(x):
		return True
	else:
		return False

def sum_palindrome(x):
#returns the sum of x and its palindrome
	backwards = ""
	for i in str(x):
		backwards = i + backwards
	return int(backwards) + x

def is_lychrel(x):
#returns True if x returns a palindrome within 50 iterations, otherwise returns False
	i = 0
	while i < 50:
		x = sum_palindrome(x)
		if is_palindrome(x):
			return False
		else:
			i += 1
	if i == 50:
		return True
			
lychrels = []

for x in range(1, 10000):
	if is_lychrel(x):
		lychrels.append(x)

print len(lychrels), lychrels