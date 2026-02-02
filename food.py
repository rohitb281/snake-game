from turtle import Turtle, Screen
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.6, 0.6)
        self.color("yellow")
        self.speed(0)
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
