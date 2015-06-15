#!/usr/b in/env pytho n
#-*- coding: UTF-8 -*-
import bluetooth
from synclk.crc import machenPaket
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

    print 'the mount of AN24:', len(An24_menu)
    return An24_menu

def is_An24(bt_name):
    if 'AN24' in bt_name:
    #len(bt_name) < 4:
        #return False
    #if len(bt_name and 'AN24'):
        return True
    else:
        return False
def conn(bt_addr="00:80:98:0E:39:77"):
    #BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
    port = 1 
    print 'port:', port
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:    
        sock.connect((bt_addr, port))
    except :
        return False
    return sock 
    print '[ok] connection'
'''
def syn_clk(sock):
    UTIME =  machenPaket()
    sock.send(UTIME)
def inquire_time(sock):
    TIME = '\x10\x02N02PCTIME\x10\x03\x0b\x73'
    #DATE = '\x10\x02NO2PCDATE\x10\x03\xfb\x0a'
    sock.send(TIME)
def inquire_date(sock):
    DATE = '\x10\x02NO2PCDATE\x10\x03\xfb\x0a'
    sock.send(DATE)
'''
import time
def start(sock):
    print 'start...'
    print '[waiting reply...]'
    print '[ok] ready to accept data '
    G = '\x10\x02G\x10\x03\x42\x1f'
    DISN = '\x10\x02N02PCDISN\x10\x03\x58\xfb'
    #DISF = '\x10\x02N02PCDISF1111\x10\x03\xd3\xeb'
    #G = '\x10\x02N02PCUTIME\x09\x06\x0f\x14\x10\x1a\x1e\x10\x03\xc2\x10'
    #G = machenPaket()
    #TIME = '\x10\x02N02PCTIME\x10\x03\x0b\x73'
    #DATE  = '\x10\x02N02PCDATE\x10\x03\xfb\x0a'
    #print 'G', G
    sock.send(DISN)
    print '[ok] setting DISN'
    sock.send(G)

    #print '[ok] utime'
    #time.sleep(2)
    #sock.send(DATE)
    return sock

def stop(sock):
    print 'stop...'
    H = '\x10\x02H\x10\x03\x6e\x2e'
    sock.send(H)
    return sock

import binascii
#battry = None    #float
#LOW_BATTRY = False
def battry(sock):
    print 'battry...'
    
    BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
    try:
        sock.send(BAT)
        battry_str = sock_recv(sock, 36, 36)
        battry = binascii.a2b_hex(battry_str[16:32])          #str
        battry = int_16(battry) * 0.01
        print 'battry: ', battry,'V',type(battry)
        '''
        (4.2-3)/(battry-3) = 20/rest_time
        '''
        rest_time = ((20*battry)-60)/1.2
        return rest_time
    except AttributeError:
        print 'connect fail..., check your bluetooth'
    
    '''
    hexbat = int_16(battry)
    test = int_16('4e')
    print 'battry:', battry,type(battry)
    print 'hexbat:', hexbat,type(hexbat)
    print 'test:', test,type(test)
    '''
import threading
def thread_bat(sock):
    return threading.Thread(target=battry,args=(sock,)).start()

import re
def check_signal(sock):
    IMP3 = '\x10\x02N02PCIM3\x10\x03\xee\xf9'
    sock.send(IMP3)
    #print 'in check_signal'
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
    #print 'mgroup:', mgroup    
    return mgroup

#check_value = [0, 0, 0, 0, 0]
def init_check(electrode_str, run_chk):
    #global check_value
    ELECTRODE_STR_LEN = 24
    BLACK_UNCONN_STR_LEN = 28
    rvalue =[0, 0, 0, 0, 0]   #BGWYO
    if len(electrode_str) == ELECTRODE_STR_LEN:
        if electrode_str[16:20] == 'f100':
            run_chk = [0, 0, 0, 0, 0]
            return run_chk 
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
            rvalue[0] = 0 
    else:
        pass
    #print 'rvalue:', rvalue
    #check_value = rvalue
    return rvalue 

#import time
def checking(sock, run_chk):
    #init_check(check_signal(sock))          #not gui
    #return  init_check(check_signal(sock)) #gui
    return init_check(check_signal(sock), run_chk)
    #print 'init check result list:', result
    #return result 
    #global check_value
    '''
    while init_check(check_signal(sock)) != [0, 0, 0, 0, 0]:
        check_value = init_check(check_signal(sock))
        print '[not ok] check', check_value
        time.sleep(5)
    check_value = [0, 0, 0, 0, 0]
    print '[ok] check', check_value
    '''



def run_check(electrode_str, run_chk):
    ELECTRODE_STR_LEN = 20
    #global check_value
    #check_value = [0,0,0,0,0]
    #run_chk = [0,0,0,0,0]
    if len(electrode_str) == ELECTRODE_STR_LEN:
        
        if electrode_str[14:16] == '31':  #1 green
            run_chk[1] = 1
            run_chk[0] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[4] = 0
            #return rvalue 
        elif electrode_str[14:16] == '32': #2 white
            run_chk[2] = 1
            run_chk[0] = 0
            run_chk[1] = 0
            run_chk[3] = 0
            run_chk[4] = 0

            #return 2
        elif electrode_str[14:16]== '33': #3 orange
            run_chk[4] = 1 
            run_chk[0] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[1] = 0

            #return 3
        elif electrode_str[14:16] == '34': #4 yellow
            run_chk[3] = 1 
            run_chk[0] = 0
            run_chk[2] = 0
            run_chk[1] = 0
            run_chk[4] = 0

            #return 4

            
        elif electrode_str[14:16] == '4c': #L clear electrode
            run_chk[0] = 1 
            run_chk[1] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[4] = 0
            #return 5
        elif electrode_str[14:16] == '43': #C lead unplugged
            run_chk[0] = 1 
            run_chk[1] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[4] = 0

            #return 6
            
    else:
        pass
        
        #run_chk = [0,0,0,0,0] 
    return run_chk
    #while check_value != [0, 0, 0, 0, 0]:
         #checking(sock)
         
    #return check_value 

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
