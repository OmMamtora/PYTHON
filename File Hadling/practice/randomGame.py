# The game() function in a program lets a user play a game and returns the score as an 
# integer. You need to read a file "Hi-score.tit' which is either blank or contains the 
# previous Hi-score. You need to write a program to update the Hi-score whenever the game() 
# function breaks the Hi-score.

import random

def game():
    print("Your are playing the game..")

    score = random.randint(1,50)

    # fetch the hi-score
    with open(":/Python/File Hadling/practice/hi-score.txt") as f:
        hiScore = f.read()
        if(hiScore != ""):
            hiScore = int(hiScore)
        else:
            hiScore = 0
    print(f"Your score is {score}")
    if(score>hiScore or hiScore == ""):
        with open("F:/Python/File Hadling/practice/hi-score.txt","w") as f:
            f.write(str(score))
    return score

game()
