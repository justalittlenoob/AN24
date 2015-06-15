import ctypes
def reconn(_count_pos):
    dll = ctypes.CDLL(r'D:\WorkSpace\Github\AN24_7\synclk\dll\crc.dll')
    frame = '\x10\x02N02PCR' + _count_pos + '\x10\x03'
    #crc_ = dll.generate_CRC(frame)
    crc = hex(dll.generate_CRC(frame))
    crc1 = crc[2:4].decode('hex')
    crc2 = crc[4:6].decode('hex')
    crc = frame + crc1 +crc2

    print 'crc:', crc, type(crc)
    print 'crc1:', crc1, type(crc1)
    print '\x5d' == crc1  #true

if '__main__' == __name__:
    reconn('00000001')
