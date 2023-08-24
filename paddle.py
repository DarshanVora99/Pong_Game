from turtle import Turtle
PADDLE_COLOR = "white"


class Paddle(Turtle):
    def __init__(self, paddle_position):
        super().__init__()
        self.penup()

        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(PADDLE_COLOR)
        self.goto(paddle_position)

    def paddle_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
