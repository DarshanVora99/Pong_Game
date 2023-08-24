from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        # self.speed("slow")
        self.y_move = 10
        self.x_move = 10
        self.increase_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed *= 0.9

    def come_to_origin(self):
        self.goto(0, 0)
        self.increase_speed = 0.1
        self.bounce_x()



