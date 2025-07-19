from threading import Thread,current_thread
#current_thread() returns thread object for example below it returns t
def disp():
    print(current_thread().name)# we can use .getName() instead of .name
t=Thread(target=disp)
t.start()

print(current_thread().name) # here current_thread returns the main thread object 

#now we can change the name of thread using setName("name") or .name attribute directly.

t.name="Child Thread" # or t.setName("Child Thread")

print(t.name)

#simmilarly rename main thread

current_thread().name="parent Thread"

print(current_thread().name)