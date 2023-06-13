from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
high_score = 0


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.display_score()

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        global high_score
        if high_score <= self.score:
            high_score = self.score
        self.write(f"Score: {self.score}, HighScore : {high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
