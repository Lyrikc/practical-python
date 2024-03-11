# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
	total_cost = 0.0
	skip = False

	with open(filename,'rt') as f:
		next(f)

		for line in f:
			row = line.split(',')
			try:
				row[1] = int(row[1])
			except ValueError:
				print("Couldn't parse amount of the shares from here:", line)
				skip = True
			try:
				row[2] = float(row[2][0:len(row[2])-1])
			except ValueError:
				print("Couldn't parse price of the shares from here:", line)
				skip = True

			if skip == True:
				skip = False
			else:
				total_cost = total_cost + row[1] * row[2]




	return total_cost;

	

#cost = portfolio_cost('Data/portfolio.csv');

#print(f'Total cost is {cost:0.2f}')	