from turtle import Turtle

ALIGNMENT = "center"
FONT =("Courier", 24, "bold")


def initialize_high_score():
    with open("data.txt", "r") as file:
        return int(file.read())


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = initialize_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def save_high_score(self):
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))



    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.save_high_score()
        self.score = 0
        self.update_scoreboard()
