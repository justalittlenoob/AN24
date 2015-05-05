# coding: utf-8     
import time  
import datetime
import data

def OpenCsv():

    data.start_data_thread()
    cache = data.data_cache
    return cache
if __name__ == '__main__':   
    print 'Starting...' ,time.strftime('%H:%M:%S',time.localtime(time.time())),datetime.datetime.now().microsecond  
    path="E:/5-HOLTER/new/long.csv" 
    cache= OpenCsv(path)    
    print len(cache), cache[111]
    print "Read over",time.strftime('%H:%M:%S',time.localtime(time.time())),datetime.datetime.now().microsecond 
