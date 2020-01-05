import turtle

#Creating a window of the game
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#Paddle A
paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5, stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5, stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1


#Paddles' movement
def paddle_a_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_a_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_b_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_b_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)


#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main game loop
while True:
    wn.update()

    #Moving ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1



