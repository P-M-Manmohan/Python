import random

num=random.randrange(1000,10000)
temp=num
stnum=str(num)
temp=str(temp)
chances=5
state=[]
for i in temp:
    state.append("__")

def win():
    print("You won you are the mastermind")
    exit()

def check(guess,num):
    cor=0
    guess=str(guess)
    for i in range(4):
        if guess[i] ==num[i]:
            state[i]=guess[i]
    for i in guess:
        if i in num:
            cor+=1
    print(f"{cor} numbers where correct")
    if "__" not in state:
        win()

#print(num)
while chances>0:
    guess=int(input("Guess the 4 digit number:" ))
    if num == guess:
        win()
    else:
        check(guess,temp)
        for i in state:
            print(i,end=" ")
        print()
    chances-=1

if chances ==0:
    print("You Lose!!")
    print(f"The number was {num}")
    exit()