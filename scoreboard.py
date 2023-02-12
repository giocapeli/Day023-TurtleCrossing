from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 250)
        self.color("black")
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 18, 'normal'))
        self.hideturtle()

    def increasse(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', move=False, align='center', font=('Arial', 18, 'normal'))
        
    def game_over(self):
        self.goto(0, -30)
        self.write(f'GAME OVER', move=False, align='center', font=('Arial', 40, 'normal'))


