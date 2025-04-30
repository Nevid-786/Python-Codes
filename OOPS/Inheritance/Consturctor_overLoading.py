class Father:
    def __init__(self):
        print('Father class constructor')
        
class Son(Father):
    def __init__(self):
        print('Son class Constructor')
#now both son(child class) and Father(parent class ) has their own init constructor 
Nevid=Son()
'''if i create an object of son class will the father Constructor be called?
    No the init of child class takes preference above parent'''
#output: Son class Constructor
