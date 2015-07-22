class toServer():
    g = 'server'
    def __init__(self):
        self.toserver = 'toServer attr'
    def func1(self):
        print 'g:',self.g
    def func2(self, arg):
        print 'arg:%s' % arg

class AN24(toServer):
    g = 'an24'
    to = toServer
    print 'to:',isinstance(to,toServer)
    print type(to)
    def __init__(self):
        self.an24 = 'an24'
        toServer.__init__(self)
        print 'in AN24 call toserver attr %s' % self.toserver
    def f1(self):
        self.func1()
        print self.toserver
        print 'in AN24 f1 call toserver func2'
        self.func2('bye')

test = AN24()
test.f1()
print test.g
