from turtle import Turtle, Screen

screen = Screen()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", False, align="center", font=('Courier', 18, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over. Final Score = {self.score}", False, align="center", font=('Courier', 18, 'normal'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
