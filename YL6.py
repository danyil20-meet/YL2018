from turtle import *
import random
import math
colormode(255)

def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return(r, g ,b)
    
class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1 = Ball(6, 'green', 4)
ball2 = Ball(4, 'blue', 6)

bestlist = [ball1, ball2]

def check_collision(ball1, ball2):
    radii = ball1.radius+ball2.radius
    
    x1 = ball1.pos()[0]
    y1 = ball1.pos()[1]
    x2 = ball2.pos()[0]
    y2 = ball2.pos()[1]
    
    centers = math.sqrt(math.pow((x2-x1), 2) + math.pow((y2-y1), 2))
    if(radii >= centers):
        ball1.color(random_color())
        ball2.color(random_color())
        print("There is a collision!")
    else:
        print("There is no collision")

#check_collision(ball1, ball2)
ind = 0
num = 0

for i in range(len(bestlist)):
    for j in range(len(bestlist)):
        if bestlist[i]!=bestlist[j]:
            check_collision(bestlist[i], bestlist[j])

        
    

