import data
#import threading
addr = "00:80:98:0E:39:77"
print '0000000000'
'''
threading.Thread(target=data.data_recv_An24,
            args=(addr,)
            ).start()
'''
data.start_data_thread()
print '1111'
data_cache = data.data_cache
import time
while 1:
    time.sleep(1)
    print data_cache
print '2222'

