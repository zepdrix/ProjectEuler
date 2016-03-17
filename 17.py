dict = {
		1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
		20: "twenty",
		30: "thirty",
		40: "forty",
		50: "fifty",
		60: "sixty",
		70: "seventy",
		80: "eighty",
		90: "ninety",
		}
			
def letter_count_tens(n):
	#references dict and returns the letter count for all int n < 100
	i = str(n)
	sum = 0	
	if len(i) == 2:
		if n <= 20 or n % 10 == 0:
			sum = len(dict[n])
		else:
			sum = len(dict[int(i[0])*10]) + len(dict[int(i[1])])

	elif len(i) == 1:
		#just look up the value from the dictionary
		sum = len(dict[n])
	
	return sum
	
	
def letter_count(n):
	#references dict and returns letter count for all int n < 1000
	i = str(n)
	sum = 0
	if len(i) == 3:
		j = int(i[1:3])
		if n % 100 == 0:
			sum = len(dict[int(i[0])]) + 7
		else:
			sum = len(dict[int(i[0])]) + 7 + 3 + letter_count_tens(j)
	else:
		sum = letter_count_tens(n)
		
	return sum
	
def letter_sum(n):
	#sums all letter counts for integers up to and including n
	i = 1
	sum = 0
	while i <= n:
		print i,": ", letter_count(i)
		sum += letter_count(i)
		i += 1
	return sum 
		
print letter_sum(999) + 11
#add 11 for one thousand
