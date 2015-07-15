from functools import wraps

def hello(fn):
    if fn.__name__ == 'foo_1':
        port =1
    else:
        port =2
    @wraps(fn)
    def wrapper():

        print 'in',port
        fn()
        print 'out',port
    return wrapper

@hello
def foo_1():
    print 'foo1'
@hello
def foo_2():
    print 'foo2'
foo_1()
foo_2()
