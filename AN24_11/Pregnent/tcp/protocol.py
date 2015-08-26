class Package():
    def __init__(self):
        self.head = '\x10\x02'
        self.tail = '\x10\x03'

class PatientInfo(Package):
    def __init__(self, _id_len='', _id='', _value=''):
        Package.__init__(self)
        self._id_len= _id_len
        self._id = _id
        self._value = _value
        self._cmd_p_info = self.cmd_patientinfo()
    def cmd_patientinfo(self):
        return '%s%s%s%s%s'%(self.head, self._id_len, self._id, self._value, self.tail)

class PatientData(Package):
    def __init__(self, _id_len='', _id='', _states='', _value=''):
        Package.__init__(self)
        self._id_len = _id_len 
        self._id = _id 
        self._states = _states
        self._value = _value
        self._cmd_p_data = self.cmd_patientdata()
    def cmd_patientdata(self):
        return '%s%s%s%s%s%s'%(self.head, self._id_len, self._id, self._states, self._value, self.tail)

class PatientOnline(Package):
    def __init__(self, _id_len='', _id='', _value=''):
        Package.__init__(self)
        self._id_len = _id_len
        self._id = _id
        self._value = _value
        self._cmd_p_online = self.cmd_patientonline()
    def cmd_patientonline(self):
        return '%s%s%s%s%s'%(self.head, self._id_len, self._id, self._value, self.tail)

class ServerOnline(Package):
    def __init__(self, _id_len='', _id='', _value=''):
        Package.__init__(self)
        self._id_len = _id_len
        self._id = _id
        self._value = _value
        self._cmd_s_online_rpy = self.cmd_serveronlinereply()
    def cmd_serveronlinereply(self):
        return '%s%s%s%s%s'%(self.head, self._id_len, self._id, self._value, self.tail)

if '__main__' == __name__:
    pd = PatientData('2', 'PD', '011','Hwerzd')
    
    print pd._cmd_p_data
