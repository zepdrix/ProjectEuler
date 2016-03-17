#very straight forward problem, find the sum, find the last 10 digits
i = 1
sum = 0
while i < 1001:
	sum += i**i
	i += 1
	
sum_str = str(sum)

print sum_str[len(sum_str)-11:]