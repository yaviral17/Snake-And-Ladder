import random
import time

#global variables
snakes={27:5,40:3,43:18,54:31,66:45,76:58,89:53,99:41}
ladders={4:25,13:46,33:49,50:69,42:63,62:81,74:92}
board=[]


#functions
def clearScreen():
    print('\n'*50)

def checkSnakeAndLadder(p):
    if p in ladders.keys():
        return ladders[p]
    elif p in snakes.keys():
        return snakes[p]
    else:
        return -1

def PlayerMovement(steps,P):
    if P[0]+steps>99:
        return P
    if len(board[P[0]])==4:
        if P[1]=='P1':
            board[P[0]]='P2'
        else:
            board[P[0]]='P1'
    else:
        board[P[0]]='*' 
    
    if checkSnakeAndLadder(P[0]+1+steps)+1:
        P[0]=checkSnakeAndLadder(P[0]+1+steps)-1
    else:
        P[0]=P[0]+steps
    
    if len(board[P[0]])==2:
        board[P[0]]=board[P[0]]+P[1]
    else:
        board[P[0]]=P[1]
    return P



def rolldice(p,c=0):
    dice=random.randint(1,6)
    if c:
        displayBorad()
        print(p+" chance :\n")
        print("Computer is rolling the dice : ")
        time.sleep(2)
        print("Computer dice gives ",dice)
    else:  
        displayBorad()
        print(p+" chance :\n")
        print("\nPress Enter to roll the dice :")
        input()
        print("Your dice gives ",dice)
        print("Press Enter to continue : ")
        input()
    return dice

def playerVScomputer():
    P1=[0,'P1']
    P2=[0,'P2']
    clearScreen()
    f=True
    print("You are P1 and Computer is AI ")
    while True:
        if f:
            steps=rolldice(P1[1],1)
            if steps!=6 and P1[0]==0:
                print("Your dice must give 6 for the first step , now over to Computer : ")
                f=False
                continue
            P1=PlayerMovement(steps,P1)
            if P1[0]==99:
                print("\nPlayer 1 Wins !!!")
                input()
                exit()
            f=False
        else:
            
            steps=rolldice(P2[1])
            if steps!=6 and P2[0]==0:
                print("Your dice must give 6 for the first step , now over to Player 1 : ")
                f=True
                continue
            P2=PlayerMovement(steps,P2)
            if P2[0]==99:
                print("\nComputer Wins !!!")
                input()
                exit()
            f=True
        displayBorad()
        print("Player 1 is at : ",P1[0]+1)
        print("Player 2 is at : ",P2[0]+1)
        clearScreen()
    

def playerVSplayer():
    P1=[0,'P1']
    P2=[0,'P2']
    clearScreen()
    f=True
    print("You are P1 i.e Player 1 and Computer is P2 i.e Player 2 ")
    while True:
        if f:
            steps=rolldice(P1[1])
            if steps!=6 and P1[0]==0:
                print("Your dice must give 6 for the first step , now over to Player 2 : ")
                f=False
                continue
            P1=PlayerMovement(steps,P1)
            displayBorad()
            if P1[0]==99:
                print("\nPlayer 1 Wins !!!")
                input()
                exit()
            f=False
        else:
            
            steps=rolldice(P2[1])
            if steps!=6 and P2[0]==0:
                print("Your dice must give 6 for the first step , now over to Player 1 : ")
                f=True
                continue
            P2=PlayerMovement(steps,P2)
            displayBorad()
            if P2[0]==99:
                print("\nPlayer 2 Wins !!!")
                input()
                exit()
            f=True
        displayBorad()
        print("Player 1 is at : ",P1[0]+1)
        print("Player 2 is at : ",P2[0]+1)
        input("Press Enter to continue : ")
        clearScreen()


def displayBorad():
    if board==[]:
        for i in range(100):
            board.append('*')
        board[0]='P1P2'
        f=True
        for i in [[90,99],[80,89],[70,79],[60,69],[50,59],[40,49],[30,39],[20,29],[10,19],[0,9]]:
                if f:
                    for g in range(i[1],i[0]-1,-1):
                        if len(board[g]):
                            print(board[g],end="     ")
                        elif len(board[g])==4:
                            print(board[g],end="  ")
                        else:
                            print(board[g],end='      ')
                        
                    print('\n\n')
                    f=False
                else:
                    for g in range(i[0],i[1]+1):
                        if len(board[g]):
                            print(board[g],end="     ")
                        elif len(board[g])==4:
                            print(board[g],end="  ")
                        else:
                            print(board[g],end='      ')
                    print('\n\n')
                    f=True
        
    else:
        f=True
        for i in [[90,99],[80,89],[70,79],[60,69],[50,59],[40,49],[30,39],[20,29],[10,19],[0,9]]:
                if f:
                    for g in range(i[1],i[0]-1,-1):
                        if board[g]=='P1' or board[g]=='P2':
                            print(board[g],end="    ")
                        elif board[g]=='P1P2':
                            print(board[g],end="   ")
                        else:
                            print(board[g],end='      ')
                        
                    print('\n\n')
                    f=False
                else:
                    for g in range(i[0],i[1]+1):
                        if board[g]=='P1' or board[g]=='P2':
                            print(board[g],end="    ")
                        elif board[g]=='P1P2':
                            print(board[g],end="   ")
                        else:
                            print(board[g],end='      ')
                    print('\n\n')
                    f=True
    s=snakes.keys()
    l=ladders.keys()
    print("\nSnakes are at position : ",s,"\nLadders are at positions : ",l)



#           main function

if __name__=="__main__":
    while True:
        clearScreen()
        ch=int(input("1: Enter 1 to play player1 vs player2\n2: Enter 2 to play player vs computer\n3: Enter 0 to exit \n>>> "))
        if ch==1:
            playerVSplayer()
        elif ch==2:
            playerVScomputer()
        elif ch==0:
            print("Bye...")
            exit()
        else:
            print("Invalid input, Try again!!")
