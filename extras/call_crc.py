import ctypes

dll = ctypes.CDLL("crcfuncs.dll")
dll.get_crc('\x10\x02G\x10\x03')

