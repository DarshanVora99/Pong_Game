from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
# import cv2

from scoreboard import Scoreboard

# Setting Background
screen = Screen()
r_paddle_position = (350, 0)
l_paddle_position = (-350, 0)
BACKGROUND_COLOR = "black"

screen.setup(width=800, height=600)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("PONG Game")
screen.tracer(0)
scoreboard = Scoreboard()

# Creating paddle
r_paddle = Paddle(r_paddle_position)
l_paddle = Paddle(l_paddle_position)


game_is_on = True

# Controlling paddle

screen.listen()
screen.onkey(key="Up", fun=r_paddle.paddle_up)
screen.onkey(key="Down", fun=r_paddle.paddle_down)
screen.onkey(key="w", fun=l_paddle.paddle_up)
screen.onkey(key="s", fun=l_paddle.paddle_down)

# Creating ball
ball = Ball()

while game_is_on:
    time.sleep(ball.increase_speed)
    screen.update()

    # Detecting collision with Upper and lower Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    ball.move()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:

        ball.bounce_x()

    # Detect when paddle misses

    # Right paddle missed
    if ball.xcor() > 380:
        ball.come_to_origin()
        scoreboard.l_point()

    # Left paddle missed
    if ball.xcor() < -380:
        ball.come_to_origin()
        scoreboard.r_point()

screen.exitonclick()
