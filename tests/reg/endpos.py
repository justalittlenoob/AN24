lbuf = '10024e3032414e443030304642453342100370b51002430000400040004000400000000000000000004000400040004000000000004160081003d4681002430000400040004000400000000000000000004000400040004000000000004160081003d46810024e3032414e41303030303030303120303030303030363410039'
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
