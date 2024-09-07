import numpy as np

class board:
    Xset=np.array([0,0,0,0,0,0,0,0,0])
    Oset=np.array([0,0,0,0,0,0,0,0,0])
    turn=1
    
    def __init__(self):
        print("Board Created")

    def displayboard(self):

        zero= 'X' if self.Xset[0] else 'O' if self.Oset[0] else 1
        one= 'X' if self.Xset[1] else 'O' if self.Oset[1] else 2
        two= 'X' if self.Xset[2] else 'O' if self.Oset[2] else 3
        three= 'X' if self.Xset[3] else 'O' if self.Oset[3] else 4
        four= 'X' if self.Xset[4] else 'O' if self.Oset[4] else 5
        five= 'X' if self.Xset[5] else 'O' if self.Oset[5] else 6
        six= 'X' if self.Xset[6] else 'O' if self.Oset[6] else 7
        seven= 'X' if self.Xset[7] else 'O' if self.Oset[7] else 8
        eight= 'X' if self.Xset[8] else 'O' if self.Oset[8] else 9
        print()
        print(f" {zero} | {one} | {two} ")
        print("---|---|---")
        print(f" {three} | {four} | {five} ")
        print("---|---|---")
        print(f" {six} | {seven} | {eight} ")
        print()

    def move(self,choice):
        if(self.turn==1):
            if(self.Xset[choice-1]==1):
                print("This value is occupied")
            else:
                self.Xset[choice-1]=1
        else:
            if(self.Oset[choice-1]==1):
                print("This value is occupied")
            else:
                self.Oset[choice-1]=1

        self.turn=1-self.turn
    
    def check(self):
        Xwin=np.array([[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])
        Owin=np.array([[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]])
        sum=0
        for i in Xwin:
            sum=self.Xset[i[0]]+self.Xset[i[1]]+self.Xset[i[2]]
            if(sum==3):
                print("Xwin")
                return 1
        for i in Owin:
            sum=self.Oset[i[0]]+self.Oset[i[1]]+self.Oset[i[2]]
            if(sum==3):
                print("Owin")
                return 0
        for i in range(0,9):
            if((self.Xset[i] or self.Oset[i])):
                k=1
            else:
                k=0
                break
        if(k==1):
            print("TIE")
            return 10
        return -1
    

    

game=board()        
while(True):
    game.displayboard()
    if(game.turn==1):
        choice=int(input("X's Turn --> "))
    else:
        choice=int(input("O's Turn --> "))
    game.move(choice)
    turn=game.check()
    if(turn!=-1):       
        break
    
    
