import ctypes

dll = ctypes.CDLL("crcfuncs.dll")
dll.get_crc('\x10\x02?GOT\x10\x03')

