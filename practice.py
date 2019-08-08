import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")


player = turtle.Turtle()
player.color("green")
player.shape("square")

speed = 1

def turnleft():
    player.left(90)

turtle.listen()
turtle.onkey(turnleft, "Left")

def turnright():
    player.right(90)

turtle.listen()
turtle.onkey(turnright, "Right")


while True:
    player.forward(speed)

delay = input("press ur face noob")
