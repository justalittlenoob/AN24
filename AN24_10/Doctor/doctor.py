import socket
import ConfigParser
config = ConfigParser.ConfigParser()
config.read('conf.ini')
HOST = config.get('Server', 'HOST')
PORT = config.getint('Server', 'PORT')
print HOST,PORT
class DoctorClient():
    def __init__(self):
        self._sock = self.build_connection()
        #self._online = self.d_online()
        self.online_patient = self.get_online_p()
#----------------------------
    def build_connection(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except Exception, msg:
            print msg
            print '[Fail] creat socket[doctor]'
        else:
            print '[ok] creat socket[doctor]'
        try:
            s.connect((HOST, PORT))
        except Exception, msg:
            print msg
            print '[Fail] connect to server from doctor'
        else:
            print '[ok] connect to server'
        return s
#----------------------------
    def d_online(self):
        try:
            self._sock.send('DOR' + '\r\n')# DOR=Doctor Online Request
        except Exception, msg:
            print msg
            print '[Fail] send doctor online request'
            return 0 #fail
        else:
            print '[ok] send doctor online request'
        return 1   #success
#----------------------------
    def get_online_p(self):
        try:
            self._sock.send('GOP' + '\r\n')# GOP = Get Online Patients
        except Exception, msg:
            print msg
            print '[Fail] send get online patient request'
        else:
            print '[ok] send get online patient request'
        buf = self._sock.recv(65535) 
        online_patients = eval(buf)
        print 'online_patients:', online_patients
        print 'type of online_patientsd:', type(online_patients)
        return online_patients

if '__main__' == __name__:
    d = DoctorClient()
    print 'online patient:', d.online_patient
            
