from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)  # Position the score at the top-center of the screen
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the previous score before writing the new one
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align=ALIGNMENT, font=FONT)

