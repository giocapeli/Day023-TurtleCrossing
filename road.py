from turtle import Turtle

class Road(Turtle):
    
    def __init__(self):
        super().__init__()
        self.one_side_y = -230
        self.other_side_y = self.one_side_y + 30 * 15
        self.penup()
        self.hideturtle()
        self.pensize(5)
        self.color("gray")
        self.setheading(0)
        self.create_road()
        
    def create_road(self):
        self.goto(-320, self.one_side_y)
        self.pendown()
        self.forward(650)
        self.penup()
        
        self.pensize(3)
        for n in range(15):

            self.goto(-320, self.one_side_y + 30 * n)
            for n in range(20):
                self.pendown()
                self.forward(15)
                self.penup()
                self.forward(40)
            self.penup()
            
        self.pensize(5)

        self.goto(-320, self.other_side_y)
        self.pendown()
        self.forward(650)
        self.penup()
        # self.create_lines()
        # self.goto(-320, self.other_side_x)
        # self.pendown()
        # self.forward(650)
        
    
    def create_lines(self):
        for x in range(22):
            self.goto(-320, self.one_side_y)
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(20)
        
