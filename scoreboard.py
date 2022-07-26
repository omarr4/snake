from turtle import Turtle

START_SCORE = -1
ALIGNMENT = 'center'
POSITION = (0, 280)
COLOR = 'yellow'
FONT = ('Lucida Console', 13, 'normal')
GAME_OVER_FONT = ('Lucida Console', 45, 'bold')
GAME_OVER_COLOR = 'red'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(POSITION)
        self.color(COLOR)
        self.score = START_SCORE
        with open('data.txt') as score_data:
            self.high_score = int(score_data.read())
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score = {self.score} --- High Score = {self.high_score}",
                   align=ALIGNMENT,
                   font=FONT)

    # def game_over(self):
    #     self.penup()
    #     self.goto(0, 0)
    #     self.color(GAME_OVER_COLOR)
    #     self.write(arg="GAME OVER",
    #                align=ALIGNMENT,
    #                font=GAME_OVER_FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as score_data:
                score_data.write(str(self.high_score))
        self.score = -1

        self.update_score()
