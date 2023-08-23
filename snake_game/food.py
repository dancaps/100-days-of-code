from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("green")
        self.generate_food()

    def generate_food(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
