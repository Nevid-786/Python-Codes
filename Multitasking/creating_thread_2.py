#creating thread with using thread class
from threading import Thread
#create a child class that inherits Thread as Parent class
class Mythread(Thread):
    def run(self):
        print("child thread is started")
t=Mythread()
t.start()
"""
in this method you can't create user define methodsin child class like show(self) only run()
and __Init__ even though you can create funcion outside child class and call it inside fir example
def disp():
    print("Call disp inside Child thread")
class Mythread(Thread):
    def run(self):
        disp()
t=Mythread()
t.start()
def disp():
    print("Call disp inside Child thread")
"""
