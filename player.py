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
        self.goto(0, -250)
        self.position_x = 0

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
