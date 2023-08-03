# Symple pong for beginners 
# need : 2 players ( paddles) 1 ball 

# import turtle for game set, the sympliest way to create games, there is also PYGAME
import turtle

#from snake import game_over, game_over_message 

#create window to play as wn 
wn = turtle.Screen()
wn.title("Ping-Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600,startx= None, starty=None)
wn.tracer(0) # stop the window for updating

pos_pad_a_x = -375
pos_pad_b_x = 370
dist = 20
"___________________________________________________________________________________________________"
# FOR MAke it Fansier 
# Adding variables for score
score_player_a = 0
score_player_b = 0 
"___________________________________________________________________________________________________"
# ADDING GAME OBJECTS TO THE GAME
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)   # setting speed of turtle module, set the speed at maximum (animation)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid= 3, stretch_len= 1)
paddle_a.penup()    # draw a line, we dont need it
paddle_a.goto(pos_pad_a_x, 0)   # where start

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)   # setting speed of turtle module, set the speed at maximum (animation)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid= 3, stretch_len= 1)
paddle_b.penup()    # draw a line, we dont need it
paddle_b.goto(pos_pad_b_x, 0)   # where start

# Ball 
ball = turtle.Turtle()
ball.speed(0)   # setting speed of turtle module, set the speed at maximum (animation)
ball.shape("circle")
ball.color("white")
ball.penup()    # draw a line, we dont need it
ball.goto(0, 0)   # where start

#Ball have movemment in x and y coordinate and need to not go out the game
ball.dx = 0.15   # dx= delta in x 0,2 pixels cause 2 was so fast in my pc
ball.dy = 0.15
"______________________________________________________________________________________________________________"
# FOR MAke it Fansier 
# Add a Counter using Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier",24, "normal"))
"______________________________________________________________________________________________________________"
# FUNCTIONS TO MOVE PADDLE A UP AND DOWN
def paddle_a_up():
    y = paddle_a.ycor()
    y += dist
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= dist
    paddle_a.sety(y)

# Keyboard binding paddle A  (wich key will command)
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# FUNCTIONS TO MOVE PADDLE B UP AND DOWN
def paddle_b_up():
    y = paddle_b.ycor()
    y += dist
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= dist
    paddle_b.sety(y)

# Keyboard binding paddle B
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#Main game loop
while True:
    
    wn.update()  # First thing to do. Create the basis for the continuity of game 

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking  ( the ball not go away and hit the corners) 800 x 600 px
    # UP CORNER
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1    #reverse direcction

    # DOWN CORNER
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1  

    # Rigth CORNER    
    if ball.xcor() > 390:
        ball.setx(390)
        ball.dx *= -1
        score_player_a += 1   # if ball hit the corner is point
        pen.clear()
        pen.write("Player A: {}  Player B: {} ".format(score_player_a, score_player_b), align="center", font=("Courier",24, "normal"))
    
    # LEFT CORNER
    if ball.xcor() < -390:
        ball.setx(-390)
        ball.dx *= -1
        score_player_b += 1  # if ball hit the corner is point
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_player_a, score_player_b), align="center", font=("Courier",24, "normal"))
        
    # PADDLE A  MARGEN 
    # UP
    if paddle_a.ycor() > 278:
        paddle_a.sety (278)
       
    # DOWN
    if paddle_a.ycor()<-270:
        paddle_a.sety (-270)
      

    # PADDLE B  MARGEN 
    # UP
    if paddle_b.ycor() > 278:
        paddle_b.sety (278)
       
    # DOWN
    if paddle_b.ycor()< -270:
        paddle_b.sety (-270)
      

    # Paddle and Ball collision (paddle size= 350) 
        # Paddle A
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40): 
        ball.setx(- 340)
        ball.dx *= -1 

        # Paddle B
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40): 
        ball.setx(340)
        ball.dx *= -1 

  

