from threading import Thread, Lock, current_thread
from random import choice

# Booking class to simulate seat reservation with thread safety
class booking:
    def __init__(self, a):
        self.l = Lock()              # Create a Lock object to prevent race conditions
        self.seat_avail = a          # Set initial available seats

    def book(self, need_seat):
        self.l.acquire()             # Lok acquired 
        print("Seat available:", self.seat_avail)
        
        if self.seat_avail >= need_seat:
            print(f"{need_seat} is allocated to {current_thread().name}")
            self.seat_avail -= need_seat
        else:
            print(f"No seat available: sorry {current_thread().name}")
        
        self.l.release()             # Lock relesed 

T = booking(1) #object of class booking

# Create two threads representing two people trying to book
t1 = Thread(target=T.book, name="Nevid", args=(1,))
t2 = Thread(target=T.book, name="Badal", args=(1,))


# Store threads in a list
threads = [t1, t2]

# Randomly pick and start each thread 
for i in range(2): 
    t_r = choice(threads)
    threads.remove(t_r)
    t_r.start()