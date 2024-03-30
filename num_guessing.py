import random
import math

lower=int(input("Enter lower bound:"))
upper=int(input("Enter upper bound:"))
#user inputs range

ran=random.randint(lower,upper)
#random number is selected
chances=round(math.log(upper-lower+1,2))
#This formula ensures that the game gives a fair number of chances to every range
while chances > 0:#checks if user is out of turns
    print(f"{chances} tries left")#printing leftover tries
    guess=int(input(f"Enter a random number between {lower}-{upper}: "))
    if guess>ran:#if guessd too high
        print("Too high")
    elif guess<ran:#if guessed to low
        print("Too low")
    else:#if won
        print("You win")
        exit()
    chances-=1#decriment the number of tries left
if chances==0:
    print(f"You lose the number was {ran}")