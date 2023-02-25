import turtle
import winsound
# WWINDOW
wn = turtle.Screen()
wn.title('PingPong by @BelkinNikita')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('yellow')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# BALL
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 0.15
ball.dy = 0.15

# FUNCTIONS
def paddle_a_up():
    y = paddle_a.ycor()
    if paddle_a.ycor() < 250:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if paddle_a.ycor() > -240:
        y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    if paddle_b.ycor() < 250:
        y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    if paddle_b.ycor() > -240:
        y -= 20
    paddle_b.sety(y)


# BUTTONS
wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

# SCORE
score_a = 0
score_b = 0

# WRITING
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.speed(0)
pen.color('white')
pen.goto(0,260)
pen.write('Player A: {}  Player B: {}'.format(score_a,score_b), align='center', font=('Courier', 24,'normal'))




# TO KEEP WINDOW OPEN
while True:
    wn.update()
    # BALL FLYING
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # BORDERS
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        if score_a == 2 :
            pen.clear()
            pen.goto(0, 0)
            pen.write('Player A is a WINNER', align='center', font=('Courier', 35,'normal'))
            winsound.PlaySound('clapping.wav', winsound.SND_FILENAME)
            turtle.bye()
        else:
            ball.goto(0,0)
            paddle_a.goto(-350,0)
            paddle_b.goto(350,0)
            ball.dx *= -1
            ball.dy = 0.1
            score_a += 1
            pen.clear()
            pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center',
                  font=('Courier', 24, 'normal'))


    if ball.xcor() < -390:
        if score_b == 2 :
            pen.clear()
            pen.goto(0, 0)
            pen.write('Player B is a WINNER', align='center', font=('Courier', 35,'normal'))
            winsound.PlaySound('clapping.wav', winsound.SND_FILENAME)
            turtle.bye()
        else:
            ball.goto(0, 0)
            paddle_a.goto(-350, 0)
            paddle_b.goto(350, 0)
            ball.dx *= -1
            ball.dy = 0
            score_b += 1
            pen.clear()
            pen.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center',
                      font=('Courier', 24, 'normal'))


    # COLLISIONS
    if ball.xcor() > 340 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40 and ball.xcor() < 350):
        ball.setx(340)
        ball.dx *= -1
        ball.dy += 0.2
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() < -340 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40 and ball.xcor() > -350):
        ball.setx(-340)
        ball.dx *= -1
        ball.dy += 0.2
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
