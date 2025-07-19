#creating thread without using thread class
#first impost threading module

from threading import Thread

#create a function that will be run by the thread

def disp(a,b):
    print(f"Thread is running {a},{b}")
    
#Now create a thread object.
T_object=Thread(target=disp,args=(10,20))

#start the thread
T_object.start()
