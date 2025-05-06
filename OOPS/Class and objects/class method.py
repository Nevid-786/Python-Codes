#class method takes the first argument  the class 
class person:
    name='Nevid'
    def Instance_name(self,name):
        self.name=name
    @classmethod
    def cls_name(cls,name):
        cls.name=name
N=person()
print(N.name)   #object attribute "Nevid" by defualt as i there is no obj attribute then it takes the class attribute
print(person.name)#class attribute "Nevid"
N.Instance_name('Aman') #instance method that takes first argument the object
print(N.name)       #now object have its own attribute name "Aman"
print(person.name)  #even though the name attribute is changed to Aman its o/p is "Nevid"
N.cls_name('Nikhil')# as it donot change the class attribute but created a seprate attribut particularly for N object
print(person.name)   # now class attribute can only be change either explicitly or by class method