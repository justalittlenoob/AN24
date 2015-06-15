import ctypes

dll = ctypes.CDLL("crcfuncs.dll")
dll.get_crc('\x10\x02N02PCR\x30\x30\x30\x30\x30\x30\x30\x31\x10\x03')

