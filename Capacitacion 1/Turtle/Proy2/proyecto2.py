import turtle
import time
import random

#Variables marcador#
retraso = 0.1
cuenta = 0
cuenta_alta = 0
## 

#Crear pantalla#
s = turtle.Screen()
s.setup(650,650)
s.bgcolor('gray')
s.title('Snake')
s.tracer()
###

#Crear cabeza de Snake#
snake = turtle.Turtle()
snake.speed(4)
snake.shape('square')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
snake.color('green')
##
#Creamos comida#
comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)
##


cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto.write("Marcador: 0\tMarcador más alto: 0", align="center", font=("verdana", 24, "normal"))

def arriba():
    snake.direction = 'up'

def abajo():
    snake.direction = 'down'

def derecha():
    snake.direction = 'right'

def izquierda():
    snake.direction = 'left'


def movimiento():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")


while True:
    s.update()

    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        snake.home()
        cuerpo.clear()
        snake.direction = 'stop'

        cuenta = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador más alto:{}".format(cuenta, cuenta_alta),align="center", font=("verdana", 24, "normal"))

    if snake.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        cuenta += 10

        if cuenta > cuenta_alta:
            cuenta_alta = cuenta
            texto.clear()
            texto.write("Marcador:{}\tMarcador más alto:{}".format(cuenta, cuenta_alta),align="center", font=("verdana", 24, "normal"))

    total = len(cuerpo)

    for i in range(total -1,0,-1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        cuerpo[0].goto(x,y)


    movimiento()
    for i in cuerpo:
        if i.distance(snake) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            snake.home()
            cuerpo.clear()
            snake.direction = "stop"

    time.sleep(retraso)

turtle.done()
