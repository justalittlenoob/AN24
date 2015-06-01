#!/user/b in/env python n
#-*- coding:UTF-8 -*-
import bluetooth
from threading import timer
import time
def find_this_bt(bt_addr):
    nearby_devices = bluetooth.discover_devices()
    for bdaddr in nearby_devices:
        if bt_addr == bdaddr:
            return True
        else:
            return False
def conn_this_bt(bt_addr):
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        sock.connect((bt_addr, port))
    except:
        return False
    return sock
def reconnect(bt_addr):
    stat_find = find_this_bt(bt_addr)
    while not stat_find:
        stat_find = find_this_bt(bt_addr)
        if True == stat_find:
            break

    stat_conn = conn_this_bt(bt_addr)

    return True

