import json

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

def wr_json(obj):
    with open('data.info','w+') as f:
        f.write(json.dumps(obj.__dict__, sort_keys=True, indent=4))

def rd_json(_file):
    with open(_file,'r') as f:
        dic = json.loads(f.read())
    return dic
    
p = Patient('S201325016','zpf','27','1','2','424243adf','9483','1')
#p = [[1,2,3],'a','b']
print rd_json('data.info')
print '---------'
print type(rd_json('data.info'))
