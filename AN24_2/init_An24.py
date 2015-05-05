#!/usr/b in/env pytho n
#-*- coding: UTF-8 -*-
import bluetooth

def scan_bluetooth():
    print("performing inquiry...")
    An24_menu = {}
    nearby_devices = bluetooth.discover_devices(lookup_names = True)
    print type(nearby_devices)
    #print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        if is_An24(name):
            An24_menu[name] = addr
            
            #print("  %s - %s" % (addr, name)) 
        else:
            pass
    
    for (ad, na) in An24_menu.items():
        print ad, na

    print len(An24_menu)
    return An24_menu

def is_An24(bt_name):
    if 'AN24' in bt_name:
    #len(bt_name) < 4:
        #return False
    #if len(bt_name and 'AN24'):
        return True
    else:
        return False

def conn(bt_addr):
    
    #BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
    port = 1
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    
        sock.connect((bt_addr, port))
    #sock.send(G)
    except:
        #print '!!!!!'
        return 1
    return sock 

def start(sock):
    G = '\x10\x02G\x10\x03\x42\x1f'
    sock.send(G)
    return sock
import re
def check_signal(sock):
    IMP3 = '\x10\x02N02PCIM3\x10\x03\xee\xf9'
    sock.send(IMP3)
    pattern = re.compile(r'1002.*?1003', 
            re.DOTALL)
    lbuf = ''
    endstr = '1003'
    endpos = 0
    mgroup=''
    while len(mgroup)!=24 and len(mgroup)!=28 :
        buf = sock.recv(65535)

        if not len(buf):
            break
    
        hexbuf = buf.encode('hex')
        lbuf = lbuf + hexbuf
        #regbuf = pattern.findall(lbuf)

        for m in pattern.finditer(lbuf):
            mgroup = m.group()
            #print m.group()
            #log( 'source data:', m.group())
        if endstr in lbuf:
            endpos = lbuf.index(endstr) + 4 
         
        else:
            pass
    
        lbuf = lbuf[endpos:]
    print 'mgroup:', mgroup    
    return mgroup

#import time
#check_value = [0, 0, 0, 0, 0]
def checking(sock):
    return init_check(check_signal(sock))
    '''
    global check_value
    
    while init_check(check_signal(sock)) != [0, 0, 0, 0, 0]:
        check_value = init_check(check_signal(sock))
        print '[not ok] check', check_value
        time.sleep(5)
    check_value = [0, 0, 0, 0, 0]
    print '[ok] check', check_value
    '''
def init_check(electrode_str):
    ELECTRODE_STR_LEN = 24
    BLACK_UNCONN_STR_LEN = 28
    rvalue =[0, 0, 0, 0, 0]   #BGWYO
    if len(electrode_str) == ELECTRODE_STR_LEN:
        if electrode_str[16:20] == 'f100':
            return rvalue
        elif int_16(electrode_str[16:18])&0x01==0x01:   #Green
            if int_16(electrode_str[18:20])&0x01==0x00:
                rvalue[1] = 2       #?                   
            elif int_16(electrode_str[18:20])&0x01==0x01:
                rvalue[1] = 1       #X
            else:
                pass
        elif int_16(electrode_str[16:18])&0x02==0x02:   #White
            if int_16(electrode_str[18:20])&0x01==0x00:
                rvalue[2] = 2
            elif int_16(electrode_str[18:20])&0x02==0x02:
                rvalue[2] = 1
            else:
                pass

        elif int_16(electrode_str[16:18])&0x04==0x04:   #Orange
            if int_16(electrode_str[18:20])&0x01==0x00:
                rvalue[4] = 2
            elif int_16(electrode_str[18:20])&0x04==0x04:
                rvalue[4] = 1
            else:
                pass
        elif int_16(electrode_str[16:18])&0x08==0x08:   # Yellow
            if int_16(electrode_str[18:20])&0x01==0x00:
                rvalue[3] = 2
            elif int_16(electrode_str[18:20])&0x08==0x08:
                rvalue[3] = 1
            else:
                pass
        elif int_16(electrode_str[16:18])&0x10==0x10:   #Black
            if int_16(electrode_str[18:20])&0x01==0x00:
                rvalue[0] = 2
            elif int_16(electrode_str[18:20])&0x10==0x10:
                rvalue[0] = 1
            else:
                pass
        else:
            pass
    elif len(electrode_str) == BLACK_UNCONN_STR_LEN:   #Black
        if electrode_str == '10024e3032414e69101010101003':
            rvalue[0] = 1
        else:
            pass
    else:
        pass
    return rvalue
 
                        


def run_check(electrode_str):
    ELECTRODE_STR_LEN = 20
    rvalue = 0
    if len(electrode_str) == ELECTRODE_STR_LEN:
        if electrode_str[14:16] == '31':  #1 green
            rvalue = 1
            #return rvalue 
        elif electrode_str[14:16] == '32': #2 white
            rvalue = 2
            #return 2
        elif electrode_str[14:16]== '33': #3 orange
            rvalue = 3
            #return 3
        elif electrode_str[14:16] == '34': #4 yellow
            rvalue = 4
            #return 4
        elif electrode_str[14:16] == '4c': #L clear electrode
            rvalue = 5
            #return 5
        elif electrode_str[14:16] == '43': #C lead unplugged
            rvalue = 6
            #return 6
    else:
        pass
    return rvalue 

def int_16(x, base = 16):
	return int(x, base)



if __name__ == '__main__':
    scan_bluetooth()
