from turtle import Turtle
import turtle
import random

turtle.colormode(255)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.teleport()

    def new_color(self):
        rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        while sum(rand_color) < 200:
            rand_color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.color(rand_color)

    def teleport(self):
        rand_x = random.randint(-14, 14) * 20
        rand_y = random.randint(-14, 14) * 20
        self.new_color()
        self.goto(rand_x, rand_y)
