#This program uses operator overloading to add to Complex numbers
class Complex:
    def __init__(self,real,imaginary):
        self.real=real          
        self.imaginary=imaginary
    def show(self):
        print(f"{self.real}+{self.imaginary}i")
    def __add__(self,other):                            #here self=A,other=B has passed by C=A+B,
        new_real=self.real+other.real                   #real part of A is added to real part of B    
        new_imaginary=self.imaginary+other.imaginary    #imaginary part of A is added to imaginary part of B 
        return Complex(new_real,new_imaginary)
A=Complex(5,3) #A=5+3i
B=Complex(4,2) #B=4+2i
C=A+B          # its basicalyy calling __add__() and passing two objects A and B as C=A.__add__(B) as dunder function and creating a object C=complex(New_real,New_imaginary)
A.show()       # every dunder function has there unique operators like for __add__() its '+' and For __sub__ its '-'
B.show()        
C.show()
        