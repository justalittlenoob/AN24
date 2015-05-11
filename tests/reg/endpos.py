lbuf = 'asd1002asdf1002sadf1003asd1002asd1003as100'
endstr = '1003'
endpos = 0
finalpos = 0
print lbuf
while endstr in lbuf:
    endpos = lbuf.index(endstr) + 4
    lbuf = lbuf[endpos:]
    print 'endpos:', endpos
    print 'lbuf:', lbuf



'''
for endstr in lbuf:
    endpos = lbuf.index(endstr) + 4
        
    print 'endpos:', endpos
    print 'lbuf:', lbuf
lbuf = lbuf[endpos:]
'''
finalpos = endpos
print 'finalpos:', finalpos
