from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.refresh()

    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    
    def move_backward(self):
        self.backward(MOVE_DISTANCE)

    def move_right(self):
        self.position_x += MOVE_DISTANCE
        self.goto(self.position_x, self.ycor())

    def move_left(self):
        self.position_x -= MOVE_DISTANCE
        self.goto(self.position_x, self.ycor())

    def refresh(self):
        self.goto(0, -260)
        self.position_x = 0
