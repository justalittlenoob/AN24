import threading
import share
import time
def func_a(li):
    for i in range(100):
        li.append('a')
    print '----', li   
        #time.sleep(5)

def func_b(li):
    for i in range(100):
        li.append('b')
    print '!!!!', li
        #time.sleep(5)

def test():
    threading.Thread(target=func_a, args=(share.get_li(),)).start()
    threading.Thread(target=func_b, args=(share.get_li(),)).start()

if __name__ == '__main__':
    test()
