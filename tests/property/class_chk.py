#import func_chk
class chk(object):
    def __init__(self):
        chk.run_chk = [0,0,0,0,0]

def change_(data):
    print 'in change_'
    data[0] = 1
    data[1] = 1
    data[2] = 1
    data[3] = 1
    data[4] = 1
    #data.append(1)
    

if __name__ == '__main__':
    chk = chk()
    print 'origin:', chk.run_chk
    change_(chk.run_chk) 
    print 'after:', chk.run_chk

