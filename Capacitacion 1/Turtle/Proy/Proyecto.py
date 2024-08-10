import turtle
import random

s = turtle
s.title('Proyecto carrera tortugas')
s.bgcolor('gray')

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

#Personalizamos PJ#

jugador1.hideturtle()
jugador1.shape ("turtle")
jugador1.color("Blue","Blue")
jugador1.shapesize(2,2,2)
jugador1.pensize(3)

#Personalizamos PJ 2#
jugador2.hideturtle()
jugador2.shape ("turtle")
jugador2.color("red","red")
jugador2.shapesize(2,2,2)
jugador2.pensize(3)

##

#Generamos circulos de victoria y volvemos a punto de inicio de cerrera.#

jugador1.penup()
jugador1.goto(200,200)
jugador1.pendown()
jugador1.circle(40)

jugador1.penup()
jugador1.goto(-250,230)

jugador1.showturtle()

jugador2.penup()
jugador2.goto(200,-200)
jugador2.pendown()
jugador2.circle(40)

jugador2.penup()
jugador2.goto(-250,-170)

jugador2.showturtle()

dado = [1,2,3,4,5,6]

for i in range(20):
    if jugador1.pos() >= (200,200):
        print("La tortuga Azul a ganado")
        break
    elif jugador2.pos() >= (200,-200):
        print("La tortuga roja a ganado")
        break
    else:
        turno1 = input("Presione la tecla enter para avanzar a la tortuga azul: ")
        turno1 = random.choice(dado)
        print("Tu numero es: ", turno1,"\nAvanzas",turno1*20)
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Presione la tecla enter para avanzar a la tortuga roja: ")
        turno2 = random.choice(dado)
        print("Tu numero es: ", turno2,"\nAvanzas",turno2*20)
        jugador2.pendown()
        jugador2.forward(20*turno2)

turtle.done()

