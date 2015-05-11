import re
endstr = '1003'
endpos =0
pattern = re.compile(r'1002.*?1003',re.DOTALL)
with open('output2.txt') as f:
	file = f.read()
	f.close()
print pattern.findall(file)


