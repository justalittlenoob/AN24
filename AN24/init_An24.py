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
    G = '\x10\x02G\x10\x03\x42\x1f'
    BAT = '\x10\x02N02PCBAT\x10\x03\x53\xcf'
    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bt_addr, port))
    sock.send(G)
    return sock 
     
def check(electrode_str):
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



if __name__ == '__main__':
    scan_bluetooth()
