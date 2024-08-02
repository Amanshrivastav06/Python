#2. The game() function in a program lets a user play a game and returns the score as an integer.
#  You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score.
#  You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.]
from random import randint
def game():
    print("you are the playing the game: ")
    score = randint(1,50)
    #Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score is {score}")
    if(score > hiscore):
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score
game()
          

