# coding: utf-8     
from OpenCsv import * 
import ctypes    
from ctypes import *

        
def CalBaseline(data):
        Baseline=[]
        FloatArray2400 = c_float * 2400
        dll = ctypes.WinDLL('E:/5-HOLTER/MFCdllPlay/Release/MFCdllPlay.dll')      
        test = dll.test
        test.restype = c_int
        for order in range(len(data))[:-2400:240]:
            ia = FloatArray2400()        
            for i in range(2400):
                ia[i]=data[order+i]
            a=test(ia)
            Baseline.append(a)
        return Baseline
if __name__ == '__main__':   
    print 'Starting...' ,time.strftime('%H:%M:%S',time.localtime(time.time())), datetime.datetime.now().microsecond  
    path="E:/5-HOLTER/new/long.csv" 
    Time, FHR, MHR, EHG= OpenCsv(path)
    print 'Read over' ,time.strftime('%H:%M:%S',time.localtime(time.time())), datetime.datetime.now().microsecond  
    print CalBaseline(FHR)
    print "calculation over", time.strftime('%H:%M:%S',time.localtime(time.time())), datetime.datetime.now().microsecond  



   
    
    
    
