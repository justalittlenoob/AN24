# coding: utf-8     
#import csv
import time  
import datetime
import data
def OpenCsv():
    #file=open(path,'r')
    #reader=csv.reader(file)
    
    data.start_data_thread()
    cache = data.data_cache
    '''
    for line in reader:
        if line[0]!='Time':
            data=[5, 5, 5, 5, 5, 5]
            data[0]=float(line[2]) #FHR
            data[1]=float(line[1]) #MHR
            data[2]=int(line[5])   #EHG
            data[3]=int(line[3])   #MMov
            data[4]=float(0)       #SNR
            data[5]=int(line[4])   #Event
            cache.append(data)
            '''
    return cache        
    #file.close()
        
if __name__ == '__main__':   
    print 'Starting...' ,time.strftime('%H:%M:%S',time.localtime(time.time())),datetime.datetime.now().microsecond  
    path="E:/5-HOLTER/new/long.csv" 
    cache= OpenCsv(path)    
    print len(cache), cache[111]
    print "Read over",time.strftime('%H:%M:%S',time.localtime(time.time())),datetime.datetime.now().microsecond 
