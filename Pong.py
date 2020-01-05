import turtle

#Creating a window of the game
wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800,height=800)
wn.tracer(0)


#Main game loop
while True:
    wn.update()
