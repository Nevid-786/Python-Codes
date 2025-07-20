#third way to create a thread without inheriting thread as parent
from threading import Thread,current_thread
class Mythead:
    def C_thread(self):
        print(current_thread().name)
t=Mythead()
        
T_object=Thread(target=t.C_thread)
T_object.start()