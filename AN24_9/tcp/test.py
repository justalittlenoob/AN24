import os
s = 'test'
path = '../history/%s.info' % s
if not os.listdir('../history/'):
    print 'null'
else: print 'file'


with open(path,'a+') as f:
    f.write('a')
print len(os.listdir('../history/'))
    
