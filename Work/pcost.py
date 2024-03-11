# pcost.py
#
# Exercise 1.27
total_cost = 0.0

with open('Data/portfolio.csv','rt') as f:
	next(f)
	for line in f:
		row = line.split(',')
		row[2] = row[2][0:len(row[2])-1]
		total_cost = total_cost+ int(row[1])* float(row[2])

print(f'Total cost is {total_cost:0.2f}')		

