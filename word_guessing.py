import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
#list of words

choice  = random.choice(words)#random word is chosen
size=len(choice)
word=[]#empty list to hold user guesses
print("GUESS THE WORD:-")
for i in range(size):
    word.append("__")#initial user guesses are blank
guesses=5

def check(guess,word,list):#function to check how correct user input is
    length=len(list)
    if guess== word:
        print("You win!!")
        exit()
    elif length==len(guess):
        for i in range(length):
            if guess[i]==word[i]:#checks if each letter is correct and replaces the dash with the letter
                list[i]=word[i]
    print("Almost, Guess again")
    return list

while guesses>0:
    for i in word:
        print(i,end=" ")
    print(" ")
    print(f"{guesses} tries left")
    guess=input("guess:")
    word = check(guess, choice,word)
    guesses-=1
if guesses==0:
    print("You lost come again")