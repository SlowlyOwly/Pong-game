from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from line import Line
from score import Score

screen = Screen()
screen.setup(width=1000, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((460, 0))
l_paddle = Paddle((-460, 0))

score = Score()

ball = Ball()
line = Line()

screen.listen()
screen.onkeypress(r_paddle.turn_up, "Up")
screen.onkeypress(r_paddle.turn_down, "Down")
screen.onkeypress(l_paddle.turn_up, "w")
screen.onkeypress(l_paddle.turn_down, "s")


game_on = True

while game_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Ball wall collision
    if ball.ycor() == 290 or ball.ycor() == -280:
        ball.bounce_y()

    # Paddle bounce
    if ball.distance(r_paddle) < 20 and ball.xcor() > 430:
        ball.bounce_x()

    elif ball.distance(r_paddle) < 40 and ball.xcor() > 430:
        ball.bounce_x()
    elif ball.distance(r_paddle) < 60 and ball.xcor() > 430:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 20 and ball.xcor() < -430:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 40 and ball.xcor() < -430:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 60 and ball.xcor() < -430:
        ball.bounce_x()

    # Ball out of edge
    if ball.xcor() > 520:
        ball.reset_position()
        score.clear()
        score.l_point()
        screen.update()
        time.sleep(1)

    if ball.xcor() < -520:
        ball.reset_position()
        score.clear()
        score.r_point()
        screen.update()
        time.sleep(1)

    if score.l_score == 10 or score.r_score == 10:
        score.game_over()
        game_on = False


screen.exitonclick()
