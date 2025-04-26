#creating counter from list,tupple:
from collections import Counter 
list=['apple','banana','seb','apple','apple','apple','banana','banana','banana',]
list_counter=Counter(list)
print(list_counter)                 #Counter({'apple': 4, 'banana': 4, 'seb': 1})

#creating counter from string:
string='SSSSSSGGGGGHHHHHHjjj'
string2='Nevid is a smart boy.'
str1_counter=Counter(string)        #Counter({'S': 6, 'H': 6, 'G': 5, 'j': 3})
str2_counter=Counter(string2)       #Counter({' ': 4, 'i': 2, 's': 2, 'a': 2, 'N': 1, 'e': 1, 'v': 1, 'd': 1, 'm': 1, 'r': 1, 't': 1, 'b': 1, 'o': 1, 'y': 1, '.': 1})
print(str1_counter)                 
print(str2_counter)

#creating from dictionary:

dict={
    'Apple':4,
    'Banana':5
}
dict_counter=Counter(dict)
print(dict_counter)  #Counter({'Banana': 5, 'Apple': 4})