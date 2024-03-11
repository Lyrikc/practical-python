# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
	total_cost = 0.0

	with open(filename,'rt') as f:
		rows = csv.reader(f)
		headers = next(rows)

		for row in rows:
			try:
				row[1] = int(row[1])
			except ValueError:
				print("Couldn't parse amount of the shares from here:", row)
				continue
			try:
				row[2] = float(row[2])
			except ValueError:
				print("Couldn't parse price of the shares from here:", row)
				continue

			total_cost = total_cost + row[1] * row[2]

	return total_cost;

if len(sys.argv) == 2:
	filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost:', cost)

#cost = portfolio_cost('Data/portfolio.csv');

#print(f'Total cost is {cost:0.2f}')	