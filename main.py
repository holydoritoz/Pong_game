from turtle import Screen
from paddle import Paddle
from ball import Ball
from dashboard import Dashboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My pong Game')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

table_dashboard = Dashboard()

screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        table_dashboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        table_dashboard.r_point()

screen.exitonclick()
