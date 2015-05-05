import data
from threading import Timer
import time
wr_tag = 0
def wr_to_file(data_cache):
    global wr_tag 
    ISOTIMEFORMAT='%Y-%m-%d %X'
    filename = time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
    with open(filename, 'ab+') as f:
        f.write(data[wr_tag:])
        wr_tag = len(data_cache) 
        f.close()

def to_file():
    t = Timer(1, wr_to_file, data.data_cache)
    t.start()
if __name__ == '__main__':
    to_file()

    

