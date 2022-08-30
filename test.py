from turtle import Turtle, Screen


melih = Turtle()
screen = Screen()
screen.onkey()


def move():
    melih.fd(25)
    melih.lt(25)

screen.listen()
screen.onkey(key="space", fun=move)


screen.exitonclick()