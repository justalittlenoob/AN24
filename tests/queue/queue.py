import Queue

q = Queue.Queue(6)

a = Queue.LifoQueue()
print 'q.empty', q.empty()
for i in range(5):
    q.put(i)
q.put((1, 2, 3))
print 'q.full', q.full()
while not q.empty():
    print q.get()
print 'q.empty', q.empty() 
for i in range(5):
    a.put(i)
print a.get(0)
