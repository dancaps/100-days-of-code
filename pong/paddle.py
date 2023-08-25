from turtle import Turtle

# constants
PADDLE_WIDTH = 1
PADDLE_HEIGHT = 5


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.resizemode("user")
        self.setheading(90)
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_HEIGHT, outline=0)
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(self.x_pos, self.y_pos)

    def up(self):
        if self.ycor() < 250:
            self.forward(10)

    def down(self):
        if self.ycor() > -240:
            self.back(10)
