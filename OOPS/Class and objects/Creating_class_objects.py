# You can create a class using class keyword followed by name of the class
class Students:
    marks=100           #class atributes ,avalible to all objects
    roll_no=27
    age=19
    def show(self):
        print(self.marks,self.roll_no,self.age)
Nevid=Students()        #object created nevid of student class
Nevid.show()            #instance method called using object
Students.show(Nevid)    #instance method called using class by passing object