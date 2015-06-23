from OpenCsv import *
import threading
import time
import random
class data():
    path="./long.csv"
    allCache = OpenCsv(path)
    endCount = 0
    run = True
    Cache = []
    def get_data(self):
        while self.run:
            self.endCount +=4
            self.Cache = self.allCache[0:self.endCount]
            time.sleep(1)
            print self.Cache[-1]
            if self.endCount >=10000:
                self.run =False
        
if __name__ == "__main__":
    data = data()
    t = threading.Thread(target = data.get_data)
    t.start()    
#    tj = 1
#    count =1
#    while tj:
#        print data.Cache[-1]
#        time.sleep(1)
#        if count>=100:
#            tj =0
    t.join()
