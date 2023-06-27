from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


def fetch_high_score_from_file():
    with open("data.txt") as file:
        return int(file.read())


class ScoreBoard(Turtle):

    def __init__(self, player_name):
        super().__init__()
        self.score = 0
        self.high_score = fetch_high_score_from_file()
        self.player_name = player_name
        self.color("white")
        self.hideturtle()
        self.penup()
        self.reset_alignment()
        self.display_score()

    def reset_alignment(self):
        self.goto(0, 270)

    def increase_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Player: {self.player_name} Score: {self.score}, High-score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def update_high_score_in_file(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def reset(self) -> None:
        if self.high_score < self.score:
            self.high_score = self.score
            self.update_high_score_in_file()
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

