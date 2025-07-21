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
#now it will again cause race condition why sice the lock object for both object h1 and h2 is different so lock of t1 and t2 is different
from threading import Thread, Lock

class Hotel1:
    def __init__(self):
        self.lock = Lock()  # shared lock
    def food(self, task):
        self.lock.acquire()
        for i in range(5):
            print(f"{task} {i}")
        self.lock.release()


hotel = Hotel1() #here a single object is used to create t1 and t2 so the lock is shared

t1 = Thread(target=hotel.food, args=("Take the order from table:",))
t2 = Thread(target=hotel.food, args=("Serve the order to table:",))

t1.start()
t2.start()
