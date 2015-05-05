import re
pattern = re.compile(r'1002.*?1003',re.DOTALL)
with open('output.txt') as f:
	file = f.read()
	f.close()
print pattern.findall(file)



