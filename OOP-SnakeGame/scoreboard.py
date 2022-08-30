from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.write(f"Score: {self.score}", move=False, align="center", font=('Times New Roman', 24, 'bold'))
        self.hideturtle()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=('Times New Roman', 24, 'bold'))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align="center", font=('Times New Roman', 24, 'bold'))


