from threading import Thread,Lock,current_thread
from random import choice
class booking:
    def __init__(self,a):
        self.l=Lock()
        self.seat_avail=a
    def book(self,need_seat):
    
        self.l.acquire()
        print("Seat available:",self.seat_avail)
        if self.seat_avail>=need_seat:
            print(f"{need_seat} is allocated to {current_thread().name}")
            self.seat_avail-=need_seat
        else:
            print(f"No seat available: sorry {current_thread().name}")
        self.l.release()
T=booking(1)

t1=Thread(target=T.book,name="Nevid",args=(1,))
t2=Thread(target=T.book,name="Badal",args=(1,))
threads=[t1,t2]
for i in range(2):
    t_r=choice(threads)
    threads.remove(t_r)
    t_r.start()
    