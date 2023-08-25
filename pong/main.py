from turtle import Turtle, Screen
from paddle import Paddle

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Screen setup
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("PONG")
screen.bgcolor("black")
screen.tracer(0)

# Object setup
r_paddle = Paddle(x_pos=350, y_pos=0)
l_paddle = Paddle(x_pos=-350, y_pos=0)

# Listener setup
screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")


is_game_running = True
while is_game_running:
    screen.update()

screen.exitonclick()
