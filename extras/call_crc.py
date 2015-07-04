import ctypes

dll = ctypes.CDLL("crcfuncs.dll")
dll.get_crc('\x10\x02N02PCUTIME3071520145300\x10\x03')

