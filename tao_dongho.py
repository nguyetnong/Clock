import turtle
from datetime import datetime

class Clock():
    turtle_gio = turtle.Turtle()
    turtle_phut = turtle.Turtle()
    turtle_giay = turtle.Turtle()
    gio_cu = 0
    phut_cu = 0
    giay_cu = 0
    chieudaikimgio = 30
    chieudaikimphut = 50
    chieudaikimgiay = 70
    def __init__(self) :
        self.turtle_giay.speed(0)
        self.turtle_phut.speed(0)
        self.turtle_gio.speed(0)
        self.turtle_giay.hideturtle()

    def mat_dongho(self):
        turtle.penup()
        turtle.goto(0,-100)
        turtle.pendown()
        turtle.circle(100)
        turtle.speed(0)
        for i in range(60):
            turtle.penup()
            turtle.hideturtle()
            turtle.home()
            turtle.pendown()
            turtle.right(6*i)
            turtle.forward(95)

        turtle.home()
        turtle.penup()
        turtle.goto(0,-90)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.begin_fill()
        turtle.fillcolor("White")
        turtle.circle(90)
        turtle.end_fill()
        turtle.pencolor("black")

        for j in range(12):
            turtle.penup()
            turtle.hideturtle()
            turtle.home()
            turtle.pendown()
            turtle.pensize(2)
            turtle.right(30*j)
            turtle.forward(95)

        turtle.home()
        turtle.penup()
        turtle.goto(0,-85)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.begin_fill()
        turtle.fillcolor("White")
        turtle.circle(85)
        turtle.end_fill()
        turtle.hideturtle()
        #turtle.done()

    def kim_dongho(self,gio1,phut1,giay1):  
        if self.gio_cu != gio1:
            self.turtle_gio.clear()
            self.turtle_gio.penup()
            self.turtle_gio.home()
            self.turtle_gio.pendown()
            self.turtle_gio.left(90)
            goc_kimgio =gio1 * 360/12
            self.turtle_gio.right(goc_kimgio)
            self.turtle_gio.forward(self.chieudaikimgio)
            self.gio_cu = gio1

        if self.phut_cu != phut1:
            self.turtle_phut.clear()
            self.turtle_phut.penup()
            self.turtle_phut.home()
            self.turtle_phut.left(90)
            self.turtle_phut.pendown()
            goc_kimphut=phut1* 360/60
            self.turtle_phut.right(goc_kimphut)
            self.turtle_phut.forward(self.chieudaikimphut)
            self.phut_cu = phut1

        if self.giay_cu != giay1:
            self.turtle_giay.clear()
            self.turtle_giay.pencolor("red")
            self.turtle_giay.home()
            self.turtle_giay.penup()
            self.turtle_giay.left(90)
            self.turtle_giay.pendown()
            self.turtle_giay.pencolor("white")
            goc_kimgiay=giay1* 360/60
            self.turtle_giay.right(goc_kimgiay)
            self.turtle_giay.forward(self.chieudaikimgiay)
            self.giay_cu = giay1

    def dieukhien(self):
        while True:
            now = datetime.now()
            gio=now.hour
            phut=now.minute
            giay=now.second
            self.kim_dongho(gio,phut,giay)

        



        







matdh=Clock()
matdh.mat_dongho()
matdh.dieukhien()
    


        

