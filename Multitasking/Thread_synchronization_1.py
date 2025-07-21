#In thread multi tasking sometime the we get wrong result as both thread works at same time 
#we can use thread locks to prevent other thread to work on specific code untill the cureent thread executes it 
from threading import Thread,Lock
class Hotel:
    def __init__(self,t):
        self.t=t
        self.l=Lock() #make a lock object
    def food(self):
        self.l.acquire() #lock the code from here
        for i in range(5):
            print(f"{self.t} {i} \n")
        self.l.release() #release the thread for the next thread
h1=Hotel("Take the order from table: ")
h2=Hotel("serve the order to table:")
t1=Thread(target=h1.food)
t2=Thread(target=h2.food) 
t1.start()
t2.start()
