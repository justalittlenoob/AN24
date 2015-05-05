'''
#method 1
while 1:
  a = int(raw_input("enter a number:"))
  if a > 0:
    print -a 
  else :
    print a
#method 2
'''
'''
while 1:
  a = input("enter a number:")
  if a > 0:
    print -a 
  else :
    print a
'''
import unittest
class UUTest(unittest.TestCase):
	def testmethod(self):
		self.assertEqual(1,2)

unittest.main()
