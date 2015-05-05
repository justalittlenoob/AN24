def convert(s, nRows):  
    if nRows == 1:  
        return s  
    step = nRows * 2 - 2  
    # first row  
    ret = s[::step]  
    print 'first lin:', ret
    for i in range(1, nRows - 1):  
        for j in range(i, len(s), step): 
            print 'j',j
            print 's[j]', s[j]
            print 'befor+,ret:', ret
            ret += s[j]  
            print 'after+,ret:', ret
            print 'ret:', ret
            if j + (step - i * 2) < len(s):  
                ret += s[j + (step - i * 2)]
                print '<len, ret:', ret
    # last row  
    ret += s[nRows - 1::step]  
    return ret  
if __name__ =='__main__':
    convert("PAYPALISHIRING", 3)
