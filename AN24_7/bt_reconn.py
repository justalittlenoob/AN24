#!/user/b in/env python n
#-*- coding:UTF-8 -*-
import bluetooth
#from threading import timer
import time
def find_this_bt(bt_addr):
    
    nearby_devices = bluetooth.discover_devices(lookup_names=False)
    if bt_addr in nearby_devices:
        return True
    else:
        return False
    '''
    for bdaddr in nearby_devices:
        print 'bdaddr', bdaddr
        if bt_addr == bdaddr:
            return True
        else:
            return False 
            '''
def conn_this_bt(bt_addr, sock):
    sock.close()
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((bt_addr, port))
    except IOError ,msg:
        print 'False reason:', msg
        return False
    return sock 



def reconnect(bt_addr, sock):
    stat_find = find_this_bt(bt_addr)
    #print 'stat_find(origin)', stat_find
    while 1:
        print '[not] find device'
        time.sleep(5)
        stat_find = find_this_bt(bt_addr)
        #print 'stat_find(in while)', stat_find
        if True == stat_find:
            break
    print '[ok] find device'

    stat_conn = conn_this_bt(bt_addr, sock)
    while 1:
        print '[not] reconnection'
        time.sleep(1)
        stat_conn = conn_this_bt(bt_addr, sock)
        print 'stat_conn', stat_conn
        if False != stat_conn:
            break
    print '[ok]  reconnection'
    G = '\x10\x02G\x10\x03\x42\x1f'
    RES = '\x10\x02N02PCRES\x10\x03\x18\xf4'
    stat_conn.send(RES)
    stat_conn.send(G)
    print '[ok] ready recv data'
    
    return stat_conn 

