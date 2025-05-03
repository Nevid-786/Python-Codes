def minion_game(string):
    def counts(str,list):
        count=0
        end=start=0
      
   
        while end<len(string):
            if str==string[start:len(str)+end]:
                print(str)
                count+=1
            start+=1
            end+=1
        return count
        
 
    Vowels="AEIOU"
    kevin=0
    str=''
    k=0
    i=0
    while i <len(string):
        if string[i] in Vowels:
            k=i
            str=''
            while k<len(string):
                str=str+string[k]
                kevin+=counts(str,list)
                k+=1
        i+=1
    stuart=0
    str=''
    k=0
    i=0
    while i <len(string):
        if string[i] not in Vowels:
            k=i
            str=''
            while k<len(string):
                str=str+string[k]
                stuart+=counts(str,list)
                k+=1
        i+=1
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")
minion_game('BANANA')