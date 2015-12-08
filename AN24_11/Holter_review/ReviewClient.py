from OpenCsv import *
import threading
class ReviewClient (object):
    def __init__(self):
        self.his_patient = {}
        self.his_note = []
        self.his_data = []
        
    def get_his_p(self, _number,_person_num, _time_begin, _time_end, _name):
        print 'premeters are:', _number,_person_num, _time_begin, _time_end, _name
        self.his_patient = {( _name, 'hospitallization_num', 'age', 'outpatient_num', _person_num, 'weeks',
 'guardianship_num', 'bed_num', _time_begin, _time_end):'11223344', ('name', 'hospitallization_num', 'age', 'outpatient_num', 'person_num', 'weeks',
 'guardianship_num', 'bed_num', '2015-11-22 21:14:30', '2015-11-22 21:14:30'):'11223345'}
    
    
    def get_data(self):
        self.path="./long.csv"
        self.allCache = OpenCsv(self.path)
        self.his_data = self.allCache

    def review(self, _uuid):
#        self.run = True
#        t = threading.Thread(target = self.get_data)
#        t.start()
        self.get_data()
