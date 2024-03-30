import random

def merge(mat,dir):
    if dir=='s':
        for i in range(2,-1,-1):
            for j in range(4):
                k=i
                l=j
                while mat[k][l]!=0 and k<3 and mat[k+1][l]==mat[k][l]:
                    mat[k+1][l]*=2
                    mat[k][l]=0
                    k+=1
        return mat
    elif dir=='w':
        for i in range(1,4):
            for j in range(4):
                k=i
                l=j
                while mat[k][l]!=0  and k>0 and mat[k-1][l]==mat[k][l]:
                    mat[k-1][l]*=2
                    mat[k][l]=0
                    k-=1
        return mat
    if dir=='a':
        for i in range(4):
            for j in range(1,4):
                k=i
                l=j
                while mat[k][l]!=0 and l>0 and mat[k][l-1]==mat[k][l]:
                    mat[k][l-1]*=2
                    mat[k][l]=0
                    l-=1
        return mat
    if dir=='d':
        for i in range(4):
            for j in range(2,-1,-1):
                k=i
                l=j
                while mat[k][l]!=0 and l<3 and mat[k][l+1]==mat[k][l]:
                    mat[k][l+1]*=2
                    mat[k][l]=0
                    l+=1
        return mat

def up(mat):
    for i in range(1,4):
        for j in range(4):
            k=i
            l=j
            while mat[k][l]!=0  and k>0 and mat[k-1][l]==0:
                mat[k-1][l]=mat[k][l]
                mat[k][l]=0
                k-=1
    mat=merge(mat,'w')
    return mat
            

def left(mat):
    for i in range(4):
        for j in range(1,4):
            k=i
            l=j
            while mat[k][l]!=0 and l>0 and mat[k][l-1]==0:
                mat[k][l-1]=mat[k][l]
                mat[k][l]=0
                l-=1
    mat=merge(mat,'a')
    return mat

def right(mat):
    for i in range(4):
        for j in range(2,-1,-1):
            k=i
            l=j
            while mat[k][l]!=0 and l<3 and mat[k][l+1]==0:
                mat[k][l+1]=mat[k][l]
                mat[k][l]=0
                l+=1
    mat=merge(mat,'d')
    return mat

def down(mat):
    temp=mat
    for i in range(2,-1,-1):
        for j in range(4):
            k=i
            l=j
            while mat[k][l]!=0 and k<3 and mat[k+1][l]==0:
                mat[k+1][l]=mat[k][l]
                mat[k][l]=0
                k+=1
    mat=merge(mat,'s')
    return mat 



def add_2(mat):
    r,c=random.randint(0,3),random.randint(0,3)
    while mat[r][c]!=0:
        r,c=random.randint(0,3),random.randint(0,3)
    
    mat[r][c]=2

def game_state(mat):
    for i in mat:
        for j in i:
            if j ==2048:
                return "WON"
    for i in mat:
        for j in i:
            if j==0:
                return "NOT OVER"
    for i in range(3):
        for j in range(3):
            if mat[i][j]==mat[i+1][j] or mat[i][j]==mat[i][j+1]:
                return "NOT OVER"
        
    return "OVER"

def start():
    print("W for up")
    print("A for left")
    print("D for right")
    print("S for down")

    mat=[]
    for i in range(4):
        mat.append([0]*4)
    add_2(mat)
    add_2(mat)
    while True:
        for i in mat:
            print(i)
        if game_state(mat)=="OVER":
            print("You lose")
            exit()
        elif game_state(mat)=="WON":
            print("Congratulations you win")
            exit()
        move=input("Move > ")
        if move.upper()=="W":
            mat= up(mat)
            mat=up(mat)
            add_2(mat)
        elif move.upper()=="A":
            left(mat)
            left(mat)
            add_2(mat)
        elif move.upper()=="D":
            right(mat)
            right(mat)
            add_2(mat)
        elif move.upper()=="S":
            down(mat)
            down(mat)
            add_2(mat)
        else:
            print("invalid input")


if __name__=="__main__":
    start()