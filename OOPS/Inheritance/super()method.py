#let say both parent and child class have methods with same name then we know 
# if we call the method using object of child class then method of child class is called not parent's
class Father:
   
    def show(self):
        print('Method of Parent class')
        
class Son(Father):

    def show(self):                     #both parent and child have same name method show()
        print('Method of Child class')
        

'''if i create an object of son class then  show() od son class will be called'''
Nevid=Son()
Nevid.show()
#output: Method of Child class

# now Then is thier not any method to access the method of parent using object of child 
# In this case we use Super() method
class Father:
   
    def show(self):
        print('Method of Parent class')
        
class Son(Father):

    def show(self):                     #both parent and child have same name method show()
        super().show()                  #now super method willcall the show() method of parent class
        
        print('Method of Child class')
        

'''if i create an object of son class then  show() od son class will be called'''
Nevid=Son()
Nevid.show()

'''O/P:Method of Parent class
       Method of Child class'''
#similiarly we can call the __init__ of parent class using super() method