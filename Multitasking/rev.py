from threading import Thread, Lock

class Hotel:
    def __init__(self, lock):
        self.lock = lock  # shared lock
    def food(self, task):
        self.lock.acquire()
        for i in range(5):
            print(f"{task} {i}")
        self.lock.release()

lock = Lock()
hotel = Hotel(lock)

t1 = Thread(target=hotel.food, args=("Take the order from table:",))
t2 = Thread(target=hotel.food, args=("Serve the order to table:",))

t1.start()
t2.start()
