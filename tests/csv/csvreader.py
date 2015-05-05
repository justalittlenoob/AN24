import csv

with open('csv.csv', 'rb') as f:
	data = list(csv.reader(f))
for line in range(1, len(data)):
	print data[line]
