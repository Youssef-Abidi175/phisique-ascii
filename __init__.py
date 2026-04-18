import os

class ball:
    def __init__(self,x,y):
        self.o="o"
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0

class phisique:
    def __init__(self,fx,fy):
        pass

class display:
    def __init__(self,xd,yd):
        self.xd=2*xd
        self.yd=yd
        self.grid=[[" "for i in range(self.xd)]for i in range(self.yd)]

    def afficher_display(self):
        result=""
        print("+", end="")
        print("-"*self.xd, end="")
        print("+")
        for ligne in self.grid:
            print("|", end="")
            for colone in ligne:
                print(colone, end="")
            print("|")
        print("+", end="")
        print("-"*self.xd, end="")
        print("+")
        return result

    def ball_position(self,p:ball):
        self.grid[p.y][p.x]=p.o



p=display(10,10)
b=ball(19,9)
p.ball_position(b)
p.afficher_display()