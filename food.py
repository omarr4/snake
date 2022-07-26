from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.set_new_color()
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def set_new_color(self):
        self.color(
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

