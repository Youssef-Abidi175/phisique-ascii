import os
import time

class ball:
    def __init__(self,x,y):
        self.o="o"
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0

class display:
    def __init__(self,xd,yd):
        self.xd=2*xd+1
        self.yd=yd+1
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
        self.grid[int(p.y)][int(p.x)]=p.o

class phisique:
    def __init__(self,fx,fy):
        self.fx=fx
        self.g=0.1
        self.fy=fy+self.g
    def mouvement(self,b:ball):
        b.vx+=self.fx
        b.vy+=self.fy
        b.x+=b.vx
        b.y+=b.vy
    def MAJ_position(self,b:ball,d:display):
        self.mouvement(b)
        os.system("cls")
        d.ball_position(b)
        d.afficher_display()

    def collision(self,b:ball,d:display):
        if int(b.x)==d.xd-1 and b.vx>0:
            b.vx=-b.vx
        if int(b.y)==d.yd-1 and b.vy>0:
            b.vy=-b.vy


os.system("cls")
p=display(15,10)
b=ball(15,5)
p.ball_position(b)
p.afficher_display()
ph=phisique(0,0)
while True:
    t=100/60
    ph.collision(b,p)
    ph.mouvement(b)
