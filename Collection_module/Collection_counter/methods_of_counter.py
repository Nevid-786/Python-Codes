from collections import Counter
#lets create a list first:
fruits=['apple','banana','apple','apple','banana','banana',]
fruits_counter=Counter(fruits)
print(fruits_counter)                #Counter({'apple': 3, 'banana': 3})

#update() Method:its basically adds count to the previous elements or adds new element in counter
fruits_counter.update(['apple','banana','banana'])
print(fruits_counter)               #Counter({'banana': 5, 'apple': 4}) now the count of banana is increase by 2 and apple by 1

#subtract method(): it decreases the count 
fruits_counter.subtract(['apple','apple','banana'])
print(fruits_counter)               #Counter({'banana': 4, 'apple': 2}) Here the count of banana is decreased by 1 and apple by 2

#most_common(x):it retuns a list of tupple of most occured key value pair where x defines the how many pairs

print(fruits_counter.most_common(1))    #[('banana', 4)] here banana is occure most times and x=1 so only one pair
print(fruits_counter.most_common(2))    #[('banana', 4), ('apple', 2)] when x=2 here after banana apple has occured most times