# -*- coding:utf-8 -*-

class Patient():
    def __init__(self):
        self.person_num =''
        self.name = ''
        self.age = 0
        self.weeks = 0
        self.outpatient_num = ''
        self.hospitalization_num = ''
        self.bed_num = ''
        self.guardianship_num = ''
        
if __name__ == '__main__':
    a = Patient()
    print a.age
