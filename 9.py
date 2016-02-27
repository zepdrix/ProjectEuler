from random import randint

def largest(a, b):
	if a > b:
		return a
	else: return b
	
def smallest(a, b):
	if a > b:
		return b
	else:
		return a

def middle(a, b, c):
	if a <= b:
		if a >= c:
			return a
	if a <= c:
		if a >= b:
			return a
	if b <= c:
		if b >= a:
			return b
	if b <= a:
		if b >= c:
			return b
	else: 
		return c
		
def pyth(number):

	x = randint(0, number)
	y = randint(0, 1000 - x)
	z = int(1000 - x - y)
	
	a = int(smallest(smallest(x, y), z))
	b = int(middle(x, y, z))
	c = int(largest(largest(x, y), z))	
	
	while (a * a) + (b * b) != (c * c):
		
		x = randint(0, number)
		y = randint(0, 1000 - x)
		z = int(1000 - x - y)
		
		a = int(smallest(smallest(x, y), z))
		b = int(middle(x, y, z))
		c = int(largest(largest(x, y), z))
		
	print "a =",a ,",b =", b, ",c =", c,",a * b * c =", a* b* c

print pyth(300)
	