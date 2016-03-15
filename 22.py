file = open("names.txt").read()
#read all the names in the file
names = []
name = ""
alph = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for x in file:
	#create a list of all the names in the file
	if x.isalpha():
		name += x
	elif name != "":
		names.append(name)
		name = ""
		
names.sort()
#put the list in alphabetical order

def namescore(name):
#calculates the score of name by adding the places of the letters together
	score = 0
	for x in name:
		score += alph.index(x)
	return score
		
def total_namescore(names):
	#adds the scores of the names multiplied by their place in the list
	total_score = 0
	for i in range(len(names)):
		total_score += namescore(names[i])*(i + 1)
	return total_score
			

print total_namescore(names)