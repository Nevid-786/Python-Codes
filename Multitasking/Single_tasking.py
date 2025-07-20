#Single tasking refers to execution of multiple tasks by single Thread

from threading import Thread

class Myclass:
    def solve_Question(self):
        self.Q1()
        self.Q2()
        self.Q3()
    def Q1(s):
        print("Q1 solved")
    def Q2(s):
        print("Q2 solved")
    def Q3(s):
        print("Q3 solved")
t=Myclass()
        
T=Thread(target=t.solve_Question())
T.start()