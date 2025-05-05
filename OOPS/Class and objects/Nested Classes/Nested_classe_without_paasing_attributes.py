#Having a class inside another class
class Defence_Force:
    Moto='Be united'  #class attribute
    def __init__(self):  
        self.Name='Nevid'
        self.B=self.Army()   #creting Object of inner class inside outer class
        
    def show(self):         #class Method
        print(self.Name)
    class Army:
        Moto_army='Be strong'   #class attribute
        def __init__(self):
            self.Gun='AK47'
            self.Area="Land"
        def show(self):         #class Method
            print(self.Gun)

D=Defence_Force()         #object of outer class
D.show()                  #calling method of outer class using object
A=Defence_Force.Army()    # creating object of inner class outside Outer class

Defence_Force.Army.show(A)# access method using class
A.show()                  # access method using object

print(A.Area)              #Access instance attribute of inner class using object
print(Defence_Force.Moto)  #Access class attribute of outer class
print(Defence_Force.Army.Moto_army) #Access class attribute of Inner clas