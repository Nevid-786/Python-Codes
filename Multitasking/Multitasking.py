
#Different task performed by multiple threads
from threading import Thread
class Hotel:
    def __init__(self,t):
        self.t=t
    def food(self):
        for i in range(5):
            print(f"{self.t} {i} \n")
h1=Hotel("Take the order from table: ")
h2=Hotel("serve the order to table:")
t1=Thread(target=h1.food)
t2=Thread(target=h2.food)
t1.start()
t2.start()
