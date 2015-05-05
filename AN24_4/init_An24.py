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
conn_value = 1
sock = None
def conn(bt_addr="00:80:98:0E:39:77"):
    global conn_value 
    global sock
    #BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
         
    sock.connect((bt_addr, port))
    conn_value = 0
    print '[ok] connection'

def start(sock):
    print 'start...'
    print '[waiting reply...]'
    print '[ok] ready to accept data '
    G = '\x10\x02G\x10\x03\x42\x1f'
    sock.send(G)
    return sock

import binascii
battry = None    #float
def battry(sock):
    print 'battry...'
    
    BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
    sock.send(BAT)
    battry_str = sock_recv(sock, 36, 36)
    battry = binascii.a2b_hex(battry_str[16:32])          #str
    battry = int_16(battry) * 0.01
    print 'battry: ', battry,'V',type(battry)
    #return battry
    '''
    hexbat = int_16(battry)
    test = int_16('4e')
    print 'battry:', battry,type(battry)
    print 'hexbat:', hexbat,type(hexbat)
    print 'test:', test,type(test)
    '''
import re
def check_signal(sock):
    IMP3 = '\x10\x02N02PCIM3\x10\x03\xee\xf9'
    sock.send(IMP3)
    print 'in check_signal'
    return sock_recv(sock, 24, 28)

def sock_recv(sock, *str_lens):
    mgroup=''
    pattern = re.compile(r'1002.*?1003', 
            re.DOTALL)
    lbuf = ''
    endstr = '1003'
    endpos = 0
    #print 'recv:',args[0],args[1],sock
    while len(mgroup)!=str_lens[0] and \
            len(mgroup)!=str_lens[1] :
        
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

def init_check(electrode_str):
    global check_value
    ELECTRODE_STR_LEN = 24
    BLACK_UNCONN_STR_LEN = 28
    rvalue =[0, 0, 0, 0, 0]   #BGWYO
    if len(electrode_str) == ELECTRODE_STR_LEN:
        if electrode_str[16:20] == 'f100':
            check_value = [0, 0, 0, 0, 0]
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
    #print 'rvalue:', rvalue
    return rvalue

#import time
def checking(sock):
    #init_check(check_signal(sock))          #not gui
    return  init_check(check_signal(sock)) #gui
    
    #global check_value
    '''
    while init_check(check_signal(sock)) != [0, 0, 0, 0, 0]:
        check_value = init_check(check_signal(sock))
        print '[not ok] check', check_value
        time.sleep(5)
    check_value = [0, 0, 0, 0, 0]
    print '[ok] check', check_value
    '''


check_value = [0, 0, 0, 0, 0]
def run_check(electrode_str):
    ELECTRODE_STR_LEN = 20
    global check_value
    if len(electrode_str) == ELECTRODE_STR_LEN:
        if electrode_str[14:16] == '31':  #1 green
            check_value[1] = 1
            #return rvalue 
        elif electrode_str[14:16] == '32': #2 white
            check_value[2] = 1
            #return 2
        elif electrode_str[14:16]== '33': #3 orange
            check_value[4] = 1 
            #return 3
        elif electrode_str[14:16] == '34': #4 yellow
            check_value[3] = 1 
            #return 4
        elif electrode_str[14:16] == '4c': #L clear electrode
            check_value[0] = 1 
            #return 5
        elif electrode_str[14:16] == '43': #C lead unplugged
            check_value[0] = 1 
            #return 6
    else:
        pass
    #return rvalue 

LOW_BATTRY = False
def low_battry(n_str):
    global LOW_BATTRY
    if n_str == '100202ANB1003':
        LOW_BATTRY =  True 
    else:
        LOW_BATTRY = False 

def int_16(x, base = 16):
	return int(x, base)



if __name__ == '__main__':
    scan_bluetooth()
