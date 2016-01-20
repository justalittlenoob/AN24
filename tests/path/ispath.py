import os

path='D:/WorkSpace/Github/tests/path/test'
ispath = os.path.exists(path)
if ispath == True:
    print 'path exist'
    pass
else:
    print 'make dir'
    os.mkdir(path)


