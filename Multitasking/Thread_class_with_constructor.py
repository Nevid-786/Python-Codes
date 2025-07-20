from threading import Thread,current_thread

class Mythread(Thread):
    def __init__(self):
        Thread.__init__(self) #always call the constructor of parent class in child class
        print("child thread is started",current_thread().name) #child thread is started MainThread
    def run(self):
        print(current_thread().name)    
        
t=Mythread() #As the object is created __init__() gets called and execution is in main thread not child thread

t.start()    #thread starts and run() gets called #Thread-1