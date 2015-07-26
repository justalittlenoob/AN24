import random
def wr_data(data):
    with open('data.data', 'a+') as f:
        f.writelines('%s\n' % data)
def rd_data():
    with open('data.data', 'r') as f:
        lines = f.readlines()
        for line in lines:
            print  line
            

for i in range(1,5):
    wr_data(str(random.randint(1,10))+' '+str(random.randint(10,20))
            +' '+ str(random.randint(20,30)))
    

rd_data()

