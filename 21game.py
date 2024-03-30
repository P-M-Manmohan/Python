import random
state=[]

def win():
    print("CONGRATULATIONS YOU WIN!!")
    exit()

def lose():
    print("YOU LOSE!!")
    exit()

def check():
    #print("current state ->",state)
    length=len(state)
    
    for i in range(1,length+1):
        if i!=state[i-1] or length>=21:
            return False
    return True

def comp():
    last=len(state)
    if last==20:
        win()
    elif last<18:
        num=random.randint(1,3)
        for i in range(1,num+1):
            state.append(last+i)
    else:
        for i in range(1,21-last):
            state.append(i+last)
    if check()==False:
        win()

def player():
    print("current state ->",state)
    num=int(input("how many numbers would you like to enter 1-3\n> "))
    if num<=3 and num>0:
        for i in range(1,num+1):
            state.append(int(input(f"input {i} > ")))
        check()
    else :
        print("Invalid input")
        lose()
    if check()==False:
        lose()
    
def start():
    print("1-play first?")
    print("2-play second?")
    play=int(input("> "))
    if play==1:
        while True:
            player()
            comp()
    else:
        while True:
            comp()
            player()
if __name__=="__main__":
    start()