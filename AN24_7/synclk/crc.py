import ctypes
from time import *

# Functinon to Call: machenPaket, append time and crc to the data payload to create the integrated frame
# 1 input , string : the data payload
# 1 output, string : the integrated frame , including data payload + time + crc
from binascii import a2b_hex, b2a_hex
def machenPaket():

	#Get the object which contain the crc function in C
	dll = ctypes.CDLL(r'D:\WorkSpace\Github\AN24_7\synclk\dll\crc.dll')
	data = 'N02PCUTIME'
	#Get the current time in year,month,day,hour,minute,second
        '''
        lt = localtime()
        print 'localtime:', lt
        year = int(strftime('%Y', lt))
        yearl = hex(year)
        #yearh = hex(year & 0x0100)
        print 'yearl:', yearl
        #print 'yearh:', yearh

        month = strftime('%m', lt)
        print 'month:', month
        day = strftime('%d', lt)
        print 'day:', day
        hour = strftime('%H', lt)
        print 'hour:', hour
        minute = strftime('%M', lt)
        print 'minute:', minute
        second = strftime('%S', lt)
        print 'second:', second

        '''
	year=strftime("%Y",localtime())
	yearl=Cstringform(int(year[2:4]))
	yearm=Cstringform(int(year[0:2]))
	month=Cstringform(int(strftime("%m",localtime())))
	day=Cstringform(int(strftime("%d",localtime())))
	hour=Cstringform(int(strftime("%H",localtime())))
	minute=Cstringform(int(strftime("%M",localtime())))
	second=Cstringform(int(strftime("%S",localtime())))
	
	#append time to the payload, generate crc,  append crc to it, and return the whole frame

	frame='\x10\x02'+ data+day+month+yearl+yearm+hour+minute+second + '\x10\x03'
        #G = '\x10\x02G\x10\x03'
	crc=hex(dll.generate_CRC(frame)) #crc format: 0x**** ,desired format \x**\x**
        #crc_test= hex(dll.generate_CRC(G))
	#str = frame + '\\x' + crc[2:4] + '\\x' + crc[4:6]
        str = frame 
        hex_str = b2a_hex(str) + crc[2:4] + crc[4:6]
        print 'hex_str:', hex_str,type(hex_str)
        print 'G:crc', crc,type(crc)
        return hex_str



#This function converts the original format(0x* when the value<16, 0x** otherwise) 
#to the format into \x**
def Cstringform(data):

	temp=hex(data)
	
	if data < 16:
		data = '0'+temp[2]
	else:
		data = temp[2:4]
	#str_hex = '\\' + 'x' + data
        str_hex = data
        #return b2a_hex(str_hex)
	return str_hex
if __name__ == '__main__':
    machenPaket()
