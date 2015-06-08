''' 
AN24    00:80:98:0E:39:77
pc      00:22:68:E2:18:6F
desktop 00:1f:81:00:08:30
I       \x10\x02I\x10\x03\x16\x2c

 '''
import thread
#import Queue
import bluetooth
import re
from bluetooth import *
#import sys
from __builtin__ import reload
#import types
from log import log
import init_An24
from tcp.client import upload_data
import bt_reconn
#reload(sys)
#sys.setdefaultencoding('utf-8')
print '[ok] set default coding:', sys.getdefaultencoding()
#apply to connect

#addr = "00:80:98:0E:39:77"

port = 1
#block I
I = '\x10\x02?I\x10\x03\x16\x2c'
#block G
G = '\x10\x02G\x10\x03\x42\x1f'
#block H
H = '\x10\x02H\x10\x03\x6e\x2e'

#BATtry's electric
BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
#N's IMP
IMP = '\x10\x02N02PCIMP\x10\x03\x2c\x2c'
#N's IMP2
IMP2 = '\x10\x02N02PCIM2\x10\x03\xd9\xc9'
#N's IMP3
IMP3 = '\x10\x02N02PCIM3\x10\x03\xee\xf9'
#N's TIME
TIME = '\x10\x02N02PCTIME\x10\x03\x0b\x73'
#N's DATE
DATE = '\x10\x02N02PCDATE\x10\x03\xfb\x0a'
#N's DISN
DISN = '\x10\x02N02PCDISN\x10\x03\x58\xfb'
#N's MODE
MODE = '\x10\x02N02PCMODE\x10\x03\x67\xe7'
RES = '\x10\x02N02PCRES\x10\x03\x18\xf4'
'''
#waiting receive
server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
#port2 = 2
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)
:w

client_sock,address = server_sock.accept()
print "Accepted connection from ",address
'''
#import chardet

#def parseData():


def format_data(data):
    '''Make data '''

    str_ret = data.replace('\x10','<DLE>')
    str_ret = str_Ret.replace('\x02','<STX>')
    str_ret = str_Ret.replace('\x03','<ETX>')
    str_ret = str_Ret.replace('\x04','<CRC>')
    #CRC=\x04
    return str_Ret

CBLOCK_STR_LEN = 76
NBLOCK_STR_LEN = 36
NBLOCK_SNR_TAG = '53'   # S
HEART_RATE_RESOLUTION = 0.25
TOTO_RESOLUTION = 0.5
SNR = 0.0
ELECTRODE_STR_LEN = 20
def data_parse(cblock_str, run_chk, low_battry):
    '''Compute the FHR MHR TOCO mother_mv 
    from C block'''
    mm = '10024d4d1003'                 # MM block
    low_battry = '10024e3032414eB1003'  #low battry
    event = 0
    FHR = []
    MHR = []
    TOCO = 0
    mother_mv = []
    data_one_sec = []
    #init_An24.run_check(cblock_str)
    if(len(cblock_str) == CBLOCK_STR_LEN):
        

        FHR_split = [10, 14, 18, 22, 26]
        MHR_split = [42, 46, 50, 54, 58]
        TOCO_split = [58, 60, 62, 64, 66]

        FHR_section = [
                cblock_str[FHR_split[0]:FHR_split[1]],
                cblock_str[FHR_split[1]:FHR_split[2]],
                cblock_str[FHR_split[2]:FHR_split[3]],
                cblock_str[FHR_split[3]:FHR_split[4]]
                ]
        MHR_section = [
                cblock_str[MHR_split[0]:MHR_split[1]],
                cblock_str[MHR_split[1]:MHR_split[2]],
                cblock_str[MHR_split[2]:MHR_split[3]],
                cblock_str[MHR_split[3]:MHR_split[4]]
                ]
        TOCO_section = [
                cblock_str[TOCO_split[0]:TOCO_split[1]],
                cblock_str[TOCO_split[1]:TOCO_split[2]],
                cblock_str[TOCO_split[2]:TOCO_split[3]],
                cblock_str[TOCO_split[3]:TOCO_split[4]]
                ]
                        
        FHR_section = [int_16(f) for f in FHR_section]
        MHR_section = [int_16(m) for m in MHR_section]
        TOCO_section = [int_16(t) for t in TOCO_section]
        ''' :
        for fh_s in xrange(0,4):
            FHR[fh_s] = round(int(FHR_section[fh_s]&
                                0x7FF) *HEART_RATE_RESOLUTION, 2)
        for mh_s in xrange(0,4):
            MHR[mh_s] = round(int(MHR[mh_s]&
                                0x7ff) * HEART_RATE_RESOLUTION, 2)
            mother_mv[mh_s] = int((MHR[mh_s]&0x1800) >> 11)

        '''
        for fh_s in FHR_section:
            fh = round(int(fh_s & 0x7FF) * HEART_RATE_RESOLUTION, 2)
            FHR.append(fh)

        for mh_s in MHR_section:
            mh =round(int(mh_s&0x7ff) * HEART_RATE_RESOLUTION, 2)
            m_mv = int((mh_s&0x1800) >> 11)
            mother_mv.append(m_mv)
            MHR.append(mh)
        
        for to_s in TOCO_section:
            TOCO = int(int(to_s) * TOTO_RESOLUTION)
        
        
        '''
        print 'FHR:', FHR
        print 'MHR:', MHR
        print 'TOCO:', TOCO
        print 'mother_mv:', mother_mv
        '''

    elif len(cblock_str) == NBLOCK_STR_LEN:
         FHR = [0, 0, 0, 0]
         MHR = [0, 0, 0, 0]
         mother_mv = [0, 0, 0, 0]
         '''Compute the SNR from N block'''
         if cblock_str[14:16] == NBLOCK_SNR_TAG:
             global SNR
             fetal_signal = int(cblock_str[16:24], 16)
             noise = int_16(cblock_str[24:32])          #int(cblock_str[24:32], 16)
             SNR_func = lambda x, y : round(x / float(y), 4)
             SNR = SNR_func(fetal_signal,
                           noise)

             #print 'SNR:', SNR
         else:
             pass
    elif len(cblock_str) == ELECTRODE_STR_LEN:
        FHR = [0, 0, 0, 0]
        MHR = [0, 0, 0, 0]
        mother_mv = [0, 0, 0, 0]
        run_chk = init_An24.run_check(cblock_str, run_chk)

    elif cblock_str == mm:          #event
        FHR = [0, 0, 0, 0]
        MHR = [0, 0, 0, 0]
        mother_mv = [0, 0, 0, 0]

        event = 1
        log('-!-!-!-!-event-!-!-!-!-', event)
         
    elif cblock_str == low_battry:
        FHR = [0, 0, 0, 0]
        MHR = [0, 0, 0, 0]
        mother_mv = [0, 0, 0, 0]
        #init_An24.LOW_BATTRY = True
        low_battry[0] = True

    else:
        FHR = [0, 0, 0, 0]
        MHR = [0, 0, 0, 0]
        mother_mv = [0, 0, 0, 0]

    data_one_sec.append([FHR[0], MHR[0], TOCO, mother_mv[0], SNR, event])
    data_one_sec.append([FHR[1], MHR[1], TOCO, mother_mv[1], SNR, event])
    data_one_sec.append([FHR[2], MHR[2], TOCO, mother_mv[2], SNR, event])
    data_one_sec.append([FHR[3], MHR[3], TOCO, mother_mv[3], SNR, event])
    print '------------------------------'
    log('data_one_sec:', data_one_sec)
    print '------------------------------'
    
    if FHR != [0, 0, 0, 0]:                             #rest run_chk
        run_chk[0] = 0
        run_chk[1] = 0
        run_chk[2] = 0
        run_chk[3] = 0
        run_chk[4] = 0
        
    log('run_chk', run_chk)
    #return FHR, MHR, TOCO, mother_mv, SNR, event
    #upload_data(data_one_sec)
    updata = ','.join(str(v) for v in FHR)
    print 'updata:', updata
    #upload_data(updata)
    return data_one_sec


#import time
#check_value = [0, 0, 0, 0, 0]

def data_recv_An24(sock, data_cache, run_chk, low_battry,stop, bt_addr):
    # ************
    #   connect An24(bd_addr) then recieve data from it
    # ************

    #sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
    #sock.connect((bd_addr, port))
    #sock = init_An24.conn(bd_addr)
    #print '[OK] connecting '
    #print 'prepare check...'
    #init_An24.checking(sock)
    '''
    while init_An24.checking(sock) != [0, 0, 0, 0, 0]:
        #check_value = init_check(check_signal(sock))
        check_value = init_An24.checking(sock)
        print '[not ok] check', check_value
        time.sleep(5)
    check_value = [0, 0, 0, 0, 0]
    print '[ok] check', check_value
    '''
    #print '[start...]'
    sock = init_An24.start(sock)
    
    #print '[waiting reply...]'
    #print '[ok] ready to accept data '

    #output = open('output.txt','a')
    pattern = re.compile(r'1002.*?1003', 
            re.DOTALL)
    lbuf = ''
    endstr = '1003'
    endpos = 0
    data_one_sec = []

    while 1:
        if stop == True:
            #sock ==init_An24.stop(sock)
            sock.close()
            close_data_thread()
        buf = sock.recv(65535)

        if not len(buf):
            #sock.close()
            '''
            sock = bt_reconn.reconnect(bt_addr, sock)
            buf = sock.recv(65535)
            '''
            break
    
        hexbuf = buf.encode('hex')
        lbuf = lbuf + hexbuf                #hex
        #lbuf = lbuf + buf                    #ascci for test
        #regbuf = pattern.findall(lbuf)

        for m in pattern.finditer(lbuf):
            print '------------------------------'
            log('source data:', m.group())
            print '------------------------------'
            #log('electrode:', init_An24.check_value)
            data_one_sec = data_parse(m.group(), run_chk, low_battry)
            stream_in_cache(data_one_sec, data_cache)
            #log( 'cache:', data_cache)
            #print stream_in_cache()
            #print type(data_all)      #tuple
            
            #print len(data_all)

            #print type(m.group())     # //str 
            #print len(m.group())      # //76
            #print m.group().isdigit()  #//False
            #print dir(m.group())
        '''
        if endstr in lbuf:
            endpos = lbuf.index(endstr) + 4 
         
        else:
            pass
        '''
        while endstr in lbuf:
            endpos = lbuf.index(endstr) +4
            lbuf = lbuf[endpos:]

        #lbuf = lbuf[endpos:]
        #print '***lbuf size***', len(lbuf) 

#import time
#data_cache = []
def stream_in_cache(data_slice, data_cache):
    '''
    local_time = time.localtime()
    date_str = time.strftime('%Y-%m-%d')
    time_str = time.strftime('%H:%M:%S')
    '''
    data_one_sec = data_slice
    
    for data_os in data_one_sec:
        data_cache.append(data_os)
    #print len(data_cache)

import threading
def start_data_thread(sock, data_cache, run_chk,low_battry,stop,bt_addr):
    '''Make a thread'''
    if stop == False:
        threading.Thread(target=data_recv_An24,
                args=(sock,data_cache,run_chk,low_battry,stop,bt_addr)
            ).start() 
    else:
        threading.Thread(target=data_recv_An24,
                args=(sock,data_cache,run_chk,low_battry,stop,bt_addr)
            ).stop()
def not_empty(s):
	return s and s.strip()

filter(not_empty,[''])

#int() can only convert string of number to int

def int_16(x, base = 16):
	return int(x, base)




def compute_addr(lbuf, qbuf):

    endpos = lbuf.index(endstr)
    lbuf.append(hexbuf)
    qbuf.put(hexbuf)
    while not qbuf.empty():
        print 'qbuf:', qbuf.get() 
    for m in pattern.finditer(hexbuf):
        print m.group()
    output.write(regbuf.encode('hex'))
    #print '[ok] query data type', chardet.detect(data)
    str1 = data.decode("ascii")
    print 'hexbuf:', hexbuf, str1
    print '-------------------------------'
    print 'endpos:', endpos
    print '-------------------------------'
    print 'lbuf:',lbuf
    print 'regbuf:', regbuf 
    print type(data)
   
if __name__ == '__main__':
    #print 'i can print'
    #sock = 
    init_An24.conn()
    bat = init_An24.battry(init_An24.sock)

    init_An24.checking(init_An24.sock)
    #print rvalue
    start_data_thread(init_An24.sock)
    #print 'there can go'

    #data_recv_An24(addr)
    #stream_in_cache()

   
#client_sock.close()
#server_sock.close()
    



