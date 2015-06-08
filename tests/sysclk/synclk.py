def int_16(x, base = 16):
    return int(x, base)

def date(tmp):
    tmp = int(int_16(tmp))
    day = int(tmp & 0x1F)
    month = int((tmp>>5) &0x0F)
    year = int((tmp>>9) & 0xFFF)
    print 'day:', day
    print 'month:', month
    print 'year:', year
def time(tmp):
    tmp = int(int_16(tmp))
    hour = int((tmp>>12) & 0x1F)
    minute = int((tmp>>6) & 0x3F)
    second = int(tmp & 0x3F)
    print 'hour:', hour
    print 'minte:', minute
    print 'second:', second
if __name__ == '__main__':
    date('030304642454338')
    time('3030314634423334')
