#This program creates a 2D vector class and a 3D vector class by using the methods of 2D vevtor class
class twoD:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def show(self):
        print(f"A={self.i}i+{self.j}j")
class threeD(twoD):                                 #twoD is inherited by threeD
    def __init__(self,i,j,k):
        super().__init__(i,j)                       #call the __init__ of twoD with super method
        self.k=k
    def show(self):
        print(f"B={self.i}i+{self.j}j+{self.k}k")
a=twoD(7,8)
b=threeD(5,6,8)
a.show()
b.show()