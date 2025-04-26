#using Counter we can perform some arithmatics aperation
from collections import Counter
fruits1=['apple','banana','apple','apple','banana','banana',]
counter1=Counter(fruits1)
print(counter1)             #Counter({'apple': 3, 'banana': 3})


fruits2=['apple','banana','apple']
counter2=Counter(fruits2)    # Counter({'apple': 2, 'banana': 1})
print(counter2)

#Aruthmatic addition(+):
print(counter1+counter2) #Counter({'apple': 5, 'banana': 4})

#Arithmatic substraction(-):
print(counter1-counter2) #Counter({'banana': 2, 'apple': 1})

#when a Counter has -Ve values then after performing any +,- opration the -Ve items are removed 

counter=Counter(a=2,b=-1)   #Counter({'a': 2, 'b': -1}) have -ve counts
print(counter)
print(Counter())            #empty counter
counter+=Counter()          #Now an plus operation is done with a empty Counter you can do -= also 
print(counter)              #Counter({'a': 2}) removed -Ve counts