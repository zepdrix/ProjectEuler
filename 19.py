import timeit, math

start = timeit.default_timer()


r_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

l_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


print int(sum(l_year) / 7), sum(l_year) % 7
#from this we know that Jan 1st 1901 was a Tuesday

def count_sundays():
	#creates a list with the kind of year it was between 1901 and 2000 then cycles through the days and adds 1 to sundays if it was a sunday on the 1st
	x = 1901
	year_list = []
	while x < 2001:
		if x % 100 == 0:
			if x % 4 == 0:
				year_list.append(1)
		elif x % 4 ==0 and not x % 100 == 0:
			year_list.append(1)
		else:
			year_list.append(0)
		x += 1
	i = 1
	
	weekday_counter = 2
	sundays = 0
	for year in year_list:
		if year == 0:
			for month in r_year:
				i = 1
				while i <= month:
					if i == 1 and weekday_counter %  7 == 0:
						sundays += 1
					i += 1
					weekday_counter += 1
		else:
			for month in l_year:
				i = 1
				while i <= month:
					if i == 1 and weekday_counter %  7 == 0:
						sundays += 1
					i += 1
					weekday_counter += 1
	return sundays

print count_sundays()

stop = timeit.default_timer()

print stop - start