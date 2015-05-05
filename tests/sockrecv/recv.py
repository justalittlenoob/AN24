import re
pattern = re.compile(r'1002.*?1003', re.DOTALL)
while 1:
    buff = sock.recv(65535)
    if not len(buff):
        break
    regbuf = pattern.findall(buff) 

