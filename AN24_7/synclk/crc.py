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
        
        lt = localtime()
        print 'localtime:', lt
        year = int(strftime('%Y', lt))
        year_str =str(year)
        yearl = chr(int(year_str[0:2]))
        yearm = chr(int(year_str[2]+year_str[3]))
        #yearh = hex(year & 0x0100)
        print 'yearl:', yearl
        print 'yearm:', yearm

        month = chr(int(strftime('%m', lt)))
        print 'month:', month
        day = chr(int(strftime('%d', lt)))
        print 'day:', day
        hour = chr(int(strftime('%H', lt)))
        print 'hour:', hour
        minute = chr(int(strftime('%m', lt)))
        print 'minute:', minute
        second = chr(int(strftime('%S', lt)))
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
	'''
	#append time to the payload, generate crc,  append crc to it, and return the whole frame

	frame='\x10\x02'+ data+day+month+yearl+yearm+hour+minute+second + '\x10\x03'
        #G = '\x10\x02G\x10\x03'
	crc=hex(dll.generate_CRC(frame)) #crc format: 0x**** ,desired format \x**\x**
        #crc_test= hex(dll.generate_CRC(G))
	utime = frame +  crc[2:4].decode('hex')  + crc[4:6].decode('hex')
        print 'utime:', utime
        return utime
        '''
        str_ = frame 
        hex_str = b2a_hex(str_) + crc[2:4] + crc[4:6]
        print 'hex_str:', hex_str,type(hex_str)
        print 'G:crc', crc,type(crc)
        return hex_str
        '''


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
