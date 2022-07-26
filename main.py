from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake")
screen.tracer(0)
screen.colormode(255)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=snake.moving_up)
screen.onkey(key="Down", fun=snake.moving_down)
screen.onkey(key="Left", fun=snake.moving_left)
screen.onkey(key="Right", fun=snake.moving_right)
while True:
    while snake.is_within_screen() and not snake.self_collision():
        screen.update()
        time.sleep(0.07)
        snake.move()

        # Detect collision with food:
        if snake.head.distance(food) < 15:
            snake.extend()
            food.refresh()
            scoreboard.update_score()
    # Reset game:
    # scoreboard.game_over()
    time.sleep(2)
    scoreboard.reset_game()
    snake.reset()

screen.exitonclick()
