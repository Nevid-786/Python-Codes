class Students:
    marks=100           #class atributes ,avalible to all objects
    def __init__(self): # constructor automatically called when an object is created no need to call
        
        self.roll_no=27 # instance attributse,Object's own Attributes
        self.age=19
        print(self.marks,self.roll_no,self.age)
   
Nevid=Students()        #object created nevid of student class
#o/p:100 27 19