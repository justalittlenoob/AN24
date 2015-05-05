from ctypes import *
from time import *

# Functinon to Call: machenPaket, append time and crc to the data payload to create the integrated frame
# 1 input , string : the data payload
# 1 output, string : the integrated frame , including data payload + time + crc
def machenPaket(data):

	#Get the object which contain the crc function in C
	dll = CDLL('.\\dll\\crc.dll')
	
	#Get the current time in year,month,day,hour,minute,second
	year=strftime("%Y",localtime())
	yearl=Cstringform(int(year[2:4]))
	yearm=Cstringform(int(year[0:2]))
	month=Cstringform(int(strftime("%m",localtime())))
	day=Cstringform(int(strftime("%d",localtime())))
	hour=Cstringform(int(strftime("%H",localtime())))
	minute=Cstringform(int(strftime("%M",localtime())))
	second=Cstringform(int(strftime("%S",localtime())))
	
	#append time to the payload, generate crc,  append crc to it, and return the whole frame
	frame=data+day+month+yearl+yearm+hour+minute+second
	crc=hex(dll.generate_CRC(frame)) #crc format: 0x**** ,desired format \x**\x**
	return frame + '\\x' + crc[2:4] + '\\x' + crc[4:6]



#This function converts the original format(0x* when the value<16, 0x** otherwise) 
#to the format into \x**
def Cstringform(data):

	temp=hex(data)
	
	if data < 16:
		data = '0'+temp[2]
	else:
		data = temp[2:4]
	
	return '\\'+ 'x'+ data
