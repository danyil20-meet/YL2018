from turtle import *
import turtle
import time
import random

turtle.register_shape("player.gif")
turtle.register_shape('cloud.gif')

class Player (Turtle):
    def __init__(self, x, y):
        Turtle. __init__(self)
        
        self.shape("player.gif")
        
        self.x = x
        self.y = y

        self.velocity_x = 0
        self.max_velocity_x = 10
        self.dy = 30
        self.is_jumping = False
        
        self.penup()
        self.goto(self.x, self.y)

    def move(self):
        self.x = self.x + self.velocity_x
        self.y = self.y - 2
        
        if (self.x <= -400):
            self.hideturtle()
            self.x = 390
            self.showturtle()
        elif (self.x >= 400):
            self.hideturtle()
            self.x = -390
            self.showturtle()
            
        self.goto(self.x, self.y)

        if (self.is_jumping):
            self.is_jumping = False
            self.velocity_x = 0
            for i in range (30):
                self.y += 3
                time.sleep(0.01)
                self.x += self.velocity_x
                self.goto (self.x, self.y)
    
clouds = []

class Cloud(Turtle):
    def __init__(self, x_velosity, x, y, is_starting):
        Turtle.__init__(self)
        self.shape('cloud.gif')
        self.penup()
        self.speed(100)

        self.y = y
        self.x = x
        self.is_starting = is_starting
        
        self.x_velosity = x_velosity
        self.is_jumping = False

        if(self.is_starting):
            self.goto(0,y)
        else:
            self.goto(random.randint(-400,400), y)
        
        self.x = self.pos()[0]
        self.y = self.pos()[1]
        
        clouds.append(self)

    def jump(self):
        if (self.is_jumping):
            for x in range (5):
                self.y -= 40
                self.goto (self.x, self.y)

                    

        
