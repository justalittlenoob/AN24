import ctypes

dll = ctypes.CDLL("crcfuncs.dll")
dll.get_crc('\x10\x02N02PCDEL\x10\x03')

