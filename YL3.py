import turtle

'''
turtle.fd(100)
turtle.right(144)
turtle.fd(100)
turtle.right(144)
turtle.fd(100)
turtle.right(144)
turtle.fd(100)
turtle.right(144)
turtle.fd(100)
'''

'''
turtle.shape("square")
turtle.stamp()
turtle.shape("arrow")
turtle.fd(10)
turtle.stamp()
'''


colors = ["red", "blue",  "green", "orange", "brown", "purple"]

turtle.speed(500000)

for i in range(500):
    turtle.pencolor(colors[i%6])
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(50)
    turtle.home()
    turtle.right(i)
