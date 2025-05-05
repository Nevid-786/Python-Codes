class Defence_Force:
    Moto='Be united'  #class attribute
    def __init__(self,name,gun,area):  
        self.Name=name
        self.B=self.Army(gun,area)  #creting Object of inner class inside outer class
        
    def show(self):         #class Method
        print(self.Name)
    class Army:
        Moto_army='Be strong'   #class attribute
        def __init__(self,Gun,Area):
            self.Gun=Gun
            self.Area=Area
        def show(self):         #class Method
            print(self.Gun,self.Area)

D=Defence_Force('Nevid','AK479','Land')      #object of outer class with argument ,Here the @nd and 3rd argu.
                                             #are attributes of object B of inner class created using init of outer class
A=Defence_Force.Army('AK47','Land')    # creating object of inner class outside Outer class with argument


D.show()                                        #are attributes of object B of inner class created using init of outer class
A.show()  #access object of army created outside outer class
D.B.show() ##access object of army created inside in __init__of outer class                 

print(A.Area)             
