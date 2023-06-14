from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
high_score = 0


class ScoreBoard(Turtle):

    def __init__(self, player_name):
        super().__init__()
        self.score = 0
        self.player_name = player_name
        self.color("white")
        self.hideturtle()
        self.penup()
        self.reset_alignment()
        self.display_score()

    def reset_alignment(self):
        self.goto(0, 270)

    def update_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        global high_score
        if high_score < self.score:
            high_score = self.score
        self.write(f"Player: {self.player_name} Score: {self.score}, High-score: {high_score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
