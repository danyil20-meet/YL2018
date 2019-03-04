import turtle
from turtle import Turtle,Screen
from classes import *

#player functions
def game(x,y):

    clean(x,y)
    
    turtle.tracer(1,0)
    turtle.bgcolor('pink')

    running = True

    num_of_clouds = 10
    score_counter = 0

    player_width = 80
    player_height = 72
    cloud_width = 100
    cloud_height = 50

    y = 0                                                                                           #CREATING CLOUDS
    for i in range(num_of_clouds):
            i = Cloud(0, 0, y, False)
            y += 60

    player = Player(0,0)                                                                            #PLAYER+STARTING+TEXT CLOUDS
    starting_cloud = Cloud(0, 0, -100, True)

    text = turtle.Turtle()                          
    text.hideturtle()
    text.penup()
    text.color('white')

    def jump():                                                                                     #PLAYER MOVING FUNCTIONS
        print ("UP KEY IS PRESSED!")
        player.is_jumping = True
        
    turtle.onkeypress(jump, "Up")

    def left():
        print("LEFT KEY IS PRESSED!")
        
        if (player.velocity_x > 0):
            player.velocity_x = -1
        elif (player.velocity_x > -player.max_velocity_x):
            player.velocity_x = player.velocity_x - 1
            
    turtle.onkeypress(left, "Left")

    def right():
        print("RIGHT KEY IS PRESSED!")
        
        if (player.velocity_x < 0):
            player.velocity_x = 1
        elif (player.velocity_x < player.max_velocity_x):
            player.velocity_x = player.velocity_x + 1
            
    turtle.onkeypress(right, "Right")
    turtle.listen()

    def check_collision():
        for i in clouds:
            is_between = (player.x + player_width / 2 > i.x - cloud_width / 2) and (player.x - player_width / 2 < i.x + cloud_width / 2)
            dy = (player.y - player_height / 2) - (i.y + cloud_height / 2)
            
            if is_between and dy < 3 and dy > 0:
                print("COLLISION!")
                for i in clouds:
                        i.is_jumping = True
                        
                return True
            
        return False

    while (running):
            if (player.pos()[1] < -350):                                                            #DYING
                    text.goto(0,0)
                    text.color('red')
                    text.write("GAME OVER" , font=("Ravie", 65,"italic"), align="center")
                    time.sleep(3)
                    quit()
                    
            y = 0
            for i in clouds:                                                                        #CREATING NEW CLOUD AFTER PREVIOUS ONE GOT Y<-350
                    if(i.pos()[1] < - 350):
                            i.hideturtle()
                            clouds.remove(i)
                            new_cloud = Cloud(0, 0, y, False)
                            y += 60

            player.move()
            
            if check_collision():                                                                   #AUTOMATIC JUMPING ON THE CLOUD + SCORE CHANGES
                    score_counter += 1
                    
                    text.goto(360, -370)
                    text.clear()
                    text.write(str(score_counter) , font=("Ravie", 40,"italic"), align="center")
                    
                    jump()
                    
                    for i in clouds:
                            i.jump()
                            
            time.sleep(0.01)
    

#player_page
def ask_name_player1(x,y):
    name = input("First players name: ")

    game_name = turtle.Turtle()
    game_name.hideturtle()
    game_name.penup()
    game_name.goto(x+260, y-10) 
    game_name.pendown()
    game_name.write(name, font=("Ravie",25,"normal"), align="center")
    
def ask_name_player2(x,y):
    name = input("Second players name:")

    game_name = turtle.Turtle()
    game_name.hideturtle()
    game_name.penup()
    game_name.goto(x+260, y-20)
    game_name.pendown()
    game_name.write(name, font=("Ravie",25,"normal"), align="center") 

def player_page(x,y):
    screen = turtle.Screen()
    screen.clear()
    
    turtle.register_shape('start_button.gif')
    turtle.register_shape('p1.gif')
    turtle.register_shape('p2.gif')

    screen = turtle.Screen()
    screen.bgpic("background.gif")

    game_name = turtle.Turtle()
    game_name.hideturtle()
    game_name.penup()
    game_name.color('white')
    game_name.goto(20,250)
    game_name.write("Clouds.Jump" , font=("Ravie", 50,"italic"), align="center")

    player1 = turtle.Turtle()
    player1.hideturtle()
    player1.penup()
    player1.shape('p1.gif')
    player1.showturtle()
    player1.goto(-20, 20)
    player1.onclick(ask_name_player1)

    player2 = turtle.Turtle()
    player2.hideturtle()
    player2.penup()
    player2.shape('p2.gif')
    player2.showturtle()
    player2.goto(-20, -120)
    player2.onclick(ask_name_player2)

    ready = turtle.Turtle()
    ready.hideturtle()
    ready.penup()
    ready.shape('start_button.gif')
    ready.showturtle()
    ready.goto(-20, -300)
    ready.onclick(game)
    
#starting_page   
def clean(x,y):
    screen = turtle.Screen()
    screen.clear()

def start(x,y):
    screen = turtle.Screen()
    screen.clear()
    
    screen.bgpic("background.gif")
    
    turtle.register_shape('start_button.gif')
    turtle.register_shape('about_button.gif')

    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    text.color('white')
    text.goto(20,250)
    text.write("Clouds.Jump" , font=("Ravie",50,"italic"), align="center")

    start_button=turtle.Turtle()
    start_button.penup()
    start_button.speed(100)
    start_button.shape('start_button.gif')
    start_button.goto(0,-20)
    start_button.onclick(player_page)

    about_button = turtle.Turtle()
    about_button.penup()
    about_button.speed(100)
    about_button.shape('about_button.gif')
    about_button.goto(0,-220)
    about_button.onclick(about_us)

def about_us(x,y):
    screen = turtle.Screen()
    screen.clear()
    screen.bgpic("about.gif")

    back_button = turtle.Turtle()
    back_button.penup()
    back_button.speed(100)
    back_button.shape('back_button.gif')
    back_button.goto(250,-250)
    back_button.onclick(start)

def starting_page():
    screen = turtle.Screen()
    screen.bgpic("background.gif")

    print("reached")
    turtle.register_shape('start_button.gif')
    turtle.register_shape('about_button.gif')
    turtle.register_shape('back_button.gif')

    text = turtle.Turtle()
    text.speed(100)
    text.hideturtle()
    text.penup()
    text.color('white')
    text.goto(20,250)
    text.write("Clouds.Jump" , font=("Ravie",50,"italic"), align="center")

    start_button=turtle.Turtle()
    start_button.penup()
    start_button.speed(100)
    start_button.shape('start_button.gif')
    start_button.goto(0,-20)
    start_button.onclick(player_page)

    about_button = turtle.Turtle()
    about_button.penup()
    about_button.speed(100)
    about_button.shape('about_button.gif')
    about_button.goto(0,-220)
    about_button.onclick(about_us)


