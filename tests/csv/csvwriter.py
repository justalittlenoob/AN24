import csv
f = open('csv.csv', 'ab+')
try:
	writer = csv.writer(f)
	row= [1,2,3,4,5,6]
	writer.writerow(row)
	f.seek(2)
finally:
	f.close()
