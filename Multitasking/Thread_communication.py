#thread communication is way in which one thread controls the execution of one or more other threads
#methods:
#1.Event class :Communication between two threads only
from threading import*
from time import sleep
def light_switch():
    sleep(2)
    print("Green Light on:")
    e.set() # it unlocks e.wait()
    sleep(6) #for 6 second t2 will execute 
    print("Red Light:")
    e.clear() #it locks the e.wait() in t2
def Traffic():
    e.wait() # it locks the thread t2 untill t1 exectues e.set()
    while e.is_set(): #is_set() returns True when e.set() is executed and false when e.clear exectued
        print("You can Go....")
        sleep(0.5)
e=Event()
t1=Thread(target=light_switch)
t2=Thread(target=Traffic)
t1.start()
t2.start()

