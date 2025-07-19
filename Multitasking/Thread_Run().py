from threading import Thread
""""run(): it basicall runs and terminates the thread autamitcally without calling when a thread i created by
inheriting Thread as parent class"""
class Mythread(Thread):
    def run(self):
        print("child thread is started")
t=Mythread()
t.start() #just start the thread run( )is already called,thread autmatically is terminated when it comes out of run()