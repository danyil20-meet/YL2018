from turtle import *
import random
colormode(255)

def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return(r, g ,b)

class Square(Turtle):

    def __init__(self, size):

        self.size = size

        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(size)
        self.color(random_color())

square1 = Square(5)

