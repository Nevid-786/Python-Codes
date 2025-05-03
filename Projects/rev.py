def minion_game(string):
    vowels = "AEIOU"
    kevin = 0
    stuart = 0

    for i in range(len(string)):
        # Total substrings starting at position i
        score = len(string) - i
        if string[i] in vowels:
            print(len(string))
            print(score)
            kevin += score
        else:
           
            stuart += score

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


minion_game('BANANA')