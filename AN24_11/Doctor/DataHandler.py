import socket
import re
import threading
from DoctorClient import DoctorClient, HOST, PORT
CBLOCK_STR_LEN = 76
COUNT_STR_LEN = 54    #count block
NBLOCK_STR_LEN = 36
NBLOCK_SNR_TAG = '53'   # S
HEART_RATE_RESOLUTION = 0.25
TOTO_RESOLUTION = 0.5
SNR = 0.0
ELECTRODE_STR_LEN = 20

class DataHandler():
    def __init__(self):
        self._sock = self.creat_link()
        self.info = {}
        self.note = []
        self.data = []
        self.run_chk = [0,0,0,0,0]
        self.low_battry = [False]
        self._count_pos = ['0']
#-----------------------
    def creat_link(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception, msg:
            print msg
            print '[Fail] creat link socket'
        else:
            print '[ok] creat link socket'
        try:
            s.connect((HOST,PORT))
        except Exception, msg:
            print msg
            print '[Fail] link to server(DataHandle)'
        else:
            print '[ok] link to server(DataHandle)'
        return s

#---------------------------
    def download_thread(self,_uuid):
        threading.Thread(target=self.download,
                        args=(_uuid,)
                        ).start()
#---------------------------
    def download(self, _uuid):
        try:
            self._sock.send('DCPD' + _uuid + '\r\n')#DCPD=Download Current Patient Data
        except Exception, msg:
            print msg
            print '[Fail] send download current patient data request'
        else:
            print '[ok] send download current patient data request'
        lbuf = ''
        endstr ='1003'
        '''
        count = 0 #test syn info
        num = 0   #test syn info
        '''
        while 1:
            pattern = re.compile(r'1002.*?1003', re.DOTALL)
            buf = self._sock.recv(65535)
            #print '------buf:', buf

            if buf[:5] == 'CINFO':
                self.info = eval(buf[5:])
                print 'CINFO:', self.info

            else:
                lbuf = lbuf + buf
                for m in pattern.finditer(lbuf):
                    #print '[raw data:]', m.group()
                    if m.group()[4:9] == 'CNOTE':
                        print 'm[cnote]', m.group()
                        note = eval(m.group()[9:-4])
                        self.note.append(note)
                        print 'CNOTE:', self.note
                    else:
                        self.handle_data(m.group())
                while endstr in lbuf:
                    endpos = lbuf.index(endstr) + 4 
                    lbuf = lbuf[endpos:] 

#----------------------------
##---------------------------
    def syn_info(self, patient_info, _uuid):
        self.info = patient_info.__dict__
        self._sock.send('UUID'+ _uuid +'SYNI' + str(patient_info.__dict__) + '\r\n')#SYNI=SYN Info
        print 'syn_info,UUID:', _uuid
        print 'syn_info,patient_info:', str(patient_info.__dict__)
##---------------------------
    def handle_data(self, cblock_str):
        mm = '10024d4d1003'                 # MM block
        low_battry = '10024e3032414eB1003'  #low battry
        event = 0
        FHR = []
        MHR = []
        TOCO = 0
        mother_mv = []
        data_one_sec = []
        #init_An24.run_check(cblock_str)
        if (len(cblock_str) == COUNT_STR_LEN) and ('41' == cblock_str[14:16]):
                self._count_pos[0] = cblock_str[16:32]
                #print '_count_pos:', self._count_pos
                return 

        if(len(cblock_str) == CBLOCK_STR_LEN):
        

            FHR_split = [10, 14, 18, 22, 26]
            MHR_split = [42, 46, 50, 54, 58]
            TOCO_split = [58, 60, 62, 64, 66]

            FHR_section = [
                    cblock_str[FHR_split[0]:FHR_split[1]],
                    cblock_str[FHR_split[1]:FHR_split[2]],
                    cblock_str[FHR_split[2]:FHR_split[3]],
                    cblock_str[FHR_split[3]:FHR_split[4]]
                    ]
            MHR_section = [
                    cblock_str[MHR_split[0]:MHR_split[1]],
                    cblock_str[MHR_split[1]:MHR_split[2]],
                    cblock_str[MHR_split[2]:MHR_split[3]],
                    cblock_str[MHR_split[3]:MHR_split[4]]
                    ]
            TOCO_section = [
                    cblock_str[TOCO_split[0]:TOCO_split[1]],
                    cblock_str[TOCO_split[1]:TOCO_split[2]],
                    cblock_str[TOCO_split[2]:TOCO_split[3]],
                    cblock_str[TOCO_split[3]:TOCO_split[4]]
                    ]
                        
            FHR_section = [int_16(f) for f in FHR_section]
            MHR_section = [int_16(m) for m in MHR_section]
            TOCO_section = [int_16(t) for t in TOCO_section]
            ''' :
            for fh_s in xrange(0,4):
                FHR[fh_s] = round(int(FHR_section[fh_s]&
                                    0x7FF) *HEART_RATE_RESOLUTION, 2)
            for mh_s in xrange(0,4):
                MHR[mh_s] = round(int(MHR[mh_s]&
                                    0x7ff) * HEART_RATE_RESOLUTION, 2)
            mother_mv[mh_s] = int((MHR[mh_s]&0x1800) >> 11)

            '''
            for fh_s in FHR_section:
                fh = round(int(fh_s & 0x7FF) * HEART_RATE_RESOLUTION, 2)
                FHR.append(fh)

            for mh_s in MHR_section:
                mh =round(int(mh_s&0x7ff) * HEART_RATE_RESOLUTION, 2)
                m_mv = int((mh_s&0x1800) >> 11)
                mother_mv.append(m_mv)
                MHR.append(mh)
        
            for to_s in TOCO_section:
                TOCO = int(int(to_s) * TOTO_RESOLUTION)
        
        
       
        elif len(cblock_str) == NBLOCK_STR_LEN:
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]
            '''Compute the SNR from N block'''
            if cblock_str[14:16] == NBLOCK_SNR_TAG:
                global SNR
                fetal_signal = int(cblock_str[16:24], 16)
                noise = int_16(cblock_str[24:32])          #int(cblock_str[24:32], 16)
                SNR_func = lambda x, y : round(x / float(y), 4)
                SNR = SNR_func(fetal_signal,
                            noise)
             
                #print 'SNR:', SNR
            else:
                pass
            return 
        elif len(cblock_str) == ELECTRODE_STR_LEN:
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]
            self.run_chk = run_check(cblock_str, self.run_chk)

        elif cblock_str == mm:          #event
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]

            event = 1
            print '-!-!-!-!-event-!-!-!-!-', event
         
        elif cblock_str == low_battry:
            #FHR = [0, 0, 0, 0]
            #MHR = [0, 0, 0, 0]
            #mother_mv = [0, 0, 0, 0]
            #init_An24.LOW_BATTRY = True
            self.low_battry[0] = True
            return

        else:
            return
            '''
            FHR = [0, 0, 0, 0]
            MHR = [0, 0, 0, 0]
            mother_mv = [0, 0, 0, 0]
            '''

        data_one_sec.append([FHR[0], MHR[0], TOCO, mother_mv[0], SNR, event])
        data_one_sec.append([FHR[1], MHR[1], TOCO, mother_mv[1], SNR, 0])
        data_one_sec.append([FHR[2], MHR[2], TOCO, mother_mv[2], SNR, 0])
        data_one_sec.append([FHR[3], MHR[3], TOCO, mother_mv[3], SNR, 0])
        if FHR != [0, 0, 0, 0]:                             #rest run_chk
            self.run_chk[0] = 0
            self.run_chk[1] = 0
            self.run_chk[2] = 0
            self.run_chk[3] = 0
            self.run_chk[4] = 0
        #print 'run_chk:', self.run_chk
        #print 'data_one_sec:', data_one_sec
        for data_os in data_one_sec:
            self.data.append(data_os)

         
def int_16(x, base = 16):
	return int(x, base)    

def run_check(electrode_str, run_chk):
    if len(electrode_str) == ELECTRODE_STR_LEN:
        
        if electrode_str[14:16] == '31':  #1 green
            run_chk[1] = 1
            run_chk[0] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[4] = 0
            #return rvalue 
        elif electrode_str[14:16] == '32': #2 white
            run_chk[2] = 1
            run_chk[0] = 0
            run_chk[1] = 0
            run_chk[3] = 0
            run_chk[4] = 0

            #return 2
        elif electrode_str[14:16]== '33': #3 orange
            run_chk[4] = 1 
            run_chk[0] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[1] = 0

            #return 3
        elif electrode_str[14:16] == '34': #4 yellow
            run_chk[3] = 1 
            run_chk[0] = 0
            run_chk[2] = 0
            run_chk[1] = 0
            run_chk[4] = 0

            #return 4

            
        elif electrode_str[14:16] == '4c': #L clear electrode
            run_chk[0] = 1 
            run_chk[1] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[4] = 0
            #return 5
        elif electrode_str[14:16] == '43': #C lead unplugged
            run_chk[0] = 1 
            run_chk[1] = 0
            run_chk[2] = 0
            run_chk[3] = 0
            run_chk[4] = 0

            #return 6
            
    else:
        pass
    return run_chk


class Patient():
    def __init__(self, p='', n='', a=0, w=0, o='', h='', b='', g='' ):
        self.person_num=p
        self.name = n
        self.age = a
        self.weeks = w
        self.outpatient_num = o
        self.hospitalization_num = h
        self.bed_num = b
        self.guardianship_num = g


if '__main__' == __name__:
    dh = DataHandler()
    dc = DoctorClient()
    #print 'online_patient.items[0][0]', dc.online_patient.items[0][0]
    dh.download('a88c3ea1-3ffc-11e5-a6fb-1078d2f63bb4')



