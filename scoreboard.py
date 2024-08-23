from turtle import Turtle

ALLIGMENT = 'center'
FONT = ('Courier',24,'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=240)
        self.score = 0
        self.color('white')
        self.update_score()
        self.hideturtle()

    # Update score function
    def update_score(self):
        self.write(f'SCORE: {self.score}',align=ALLIGMENT, font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write('GAME OVER', align=ALLIGMENT, font=FONT)

    # Add point to score
    def add_point(self):
        self.score += 1
        self.clear()
        self.update_score()


