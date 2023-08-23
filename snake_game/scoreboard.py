from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=280)
        self.write_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.color("red")
        self.write(f"GAME OVER!", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)
