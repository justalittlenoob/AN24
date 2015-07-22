import os
PATH = '../history/'
FILE_INFO = '../history/%s.info'
FILE_DATA = '../history/%s.data' 
has_history = None
def check_local():
        if not os.listdir(PATH):
            has_history = 0   # empty florder,no history
        else:
            has_history = 1
        return has_history
print check_local()
