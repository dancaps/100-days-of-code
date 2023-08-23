from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game! Get it?")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_running = True
while is_game_running:
    sleep(.05)
    screen.update()
    snake.move()

    # Eats food.
    if snake.head.distance(food) < 15:
        food.generate_food()
        scoreboard.update_score()
        snake.create_segment()

    # Hits the wall.
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        is_game_running = False
        scoreboard.game_over()

    # Hits the body.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_running = False
            scoreboard.game_over()


screen.exitonclick()
