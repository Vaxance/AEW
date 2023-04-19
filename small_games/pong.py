"""
Tutorial from: https://youtu.be/XGf2GcyHPhc?t=141
"""
import turtle, Genders


def create_paddle(start_x: int, start_y: int, colour: str):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color(colour)
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(start_x, start_y)
    return paddle

def paddle_a_up():
    paddle_a.sety(paddle_a.ycor() + 20)


def paddle_a_down():
    paddle_a.sety(paddle_a.ycor() - 20)

def paddle_b_up():
    paddle_b.sety(paddle_b.ycor() + 20)


def paddle_b_down():
    paddle_b.sety(paddle_b.ycor() - 20)

window = turtle.Screen()
window.title("Pong Turtlegame")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Paddles
paddle_a = create_paddle(-350, 0, "white")
paddle_b = create_paddle(350, 0, "white")

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# keybords
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

while True:
    window.update()
