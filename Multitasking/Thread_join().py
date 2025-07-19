#join()is used to hold the execution of main thread untill the child thread get executed completely
from threading import Thread

class Mythread(Thread):
    def run(self):
        for i in range(5):
            print(f"child thread {i}")
        
t=Mythread()
t.start()
for i in range(5):
    print(f"Main Thread {i}")
'''without join() output of both thread is random for each execution
child thread 0
Main Thread 0
child thread 1
Main Thread 1
child thread 2
Main Thread 2
Main Thread 3
Main Thread 4
child thread 3
child thread 4
'''
class Mythread(Thread):
    def run(self):
        for i in range(5):
            print(f"child thread {i}")
        
t=Mythread()
t.start()
t.join() #just adding join()
for i in range(5):
    print(f"Main Thread {i}")
'''here you can see that chid thread is first completely executed'
child thread 0
child thread 1
child thread 2
child thread 3
child thread 4
Main Thread 0
Main Thread 1
Main Thread 2
Main Thread 3
Main Thread 4
'''