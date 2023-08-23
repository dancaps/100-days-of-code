from turtle import Turtle

STARTING_COORDINATES = (0, 0)
MOVE_DISTANCE = 20
STARTING_SNAKE_LENGTH = 3
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for _ in range(0, STARTING_SNAKE_LENGTH):
            self.create_segment()

    def create_segment(self):
        if len(self.segments) < 1:
            last_x = 0
            last_y = 0
        else:
            last_x = self.segments[-1].xcor()
            last_y = self.segments[-1].ycor()

        segment = Turtle()
        segment.penup()
        segment.shape("square")
        segment.color("white")
        segment.goto(x=-20 * last_x, y=last_y)
        self.segments.append(segment)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x_cord = self.segments[segment - 1].xcor()
            new_y_cord = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x_cord, new_y_cord)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
