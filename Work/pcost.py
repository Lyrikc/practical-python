# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
	total_cost = 0.0

	with open(filename,'rt') as f:
		next(f)
		for line in f:
			row = line.split(',')
			row[2] = row[2][0:len(row[2])-1]
			total_cost = total_cost+ int(row[1])* float(row[2])
	return total_cost;

	

#cost = portfolio_cost('Data/portfolio.csv');

#print(f'Total cost is {cost:0.2f}')	