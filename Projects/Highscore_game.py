import random
def game():
    print("You are playing the game...")
    score=random.randint(1,100)
    
    # fetch the previos score
    f=open("hiscore.txt","w")
    f.write("0")
    with open("hiscore.txt") as f:
        hiscore=f.read()
        if(hiscore!=""):#check if there is a previous hi score
            hiscore=int(hiscore)
        else:
            hiscore=0#if no then take it as 0
    print(f"your score: {score}")
    #updtae if the latest score is greater as hiscore
    if(score>hiscore):
        with open("hiscore.txt","w") as f:
                f.write(str(score))
    clear=(input("To clear the the high score stored press enter:"))
    if(clear==""):
        with open("hiscore.txt","w") as f:
            f.write("")
    
    return score
print("Press any key to get a random score:")
start=input()
game()
    