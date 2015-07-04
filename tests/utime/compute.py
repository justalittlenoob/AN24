def int_16(x, base=16):
    return int(x, base)

def _date(tmp):
    tmp = int_16(tmp.decode('hex'))
    day = tmp & 0x1F
    month = (tmp>>5) & 0x0F
    year = (tmp>>9) & 0xFFF
    return (year, month, day)

def _time(tmp):
    tmp = int_16(tmp.decode('hex'))
    hour = (tmp>>12) & 0x1F
    minute = (tmp>>6) & 0x3F
    second = tmp & 0x3F
    return (hour, minute, second)

if '__main__' == __name__:
    print _date('3030304642454533')
    print _time('3030314630324133')



