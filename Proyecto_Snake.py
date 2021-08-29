#------------Importar modulos---------------

import turtle
import time
import random

#--------------Variables--------------------
retraso = 0.1
marcador = 0
marcador_alto = 0

#--------------Interfaz grafica --------------------

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("black")
s.title("Proyecto Juego en Python Snake")


#--------------Creacion de la cabeza--------------------

serpiente = turtle.Turtle()
serpiente.speed(1)
serpiente.shape("square")
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = "stop"
serpiente.color("green")


#--------------Creacion de comida --------------------

comida = turtle.Turtle()
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)
comida.speed(0)

#--------------Cuerpo de la serpiente --------------------
cuerpo = []

#--------------Marcador---------------------------------------------------------------------------

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(-130, 250)
texto.write("Marcador: 0\tMarcador mas alto: 0",align="center",font=("verdana", 10, "normal"))

#--------------Funciones--------------------------------------------------------------------------

def arriba():
    serpiente.direction = "up"

def abajo():
    serpiente.direction = "down"

def derecha():
    serpiente.direction = "right"

def izquierda():
    serpiente.direction = "left"


def movimiento():
    if serpiente.direction == "up":
        y = serpiente.ycor()
        serpiente.sety(y+20)
    if serpiente.direction == "down":
        y = serpiente.ycor()
        serpiente.sety(y-20)
    if serpiente.direction == "right":
        x = serpiente.xcor()
        serpiente.setx(x+20)
    if serpiente.direction == "left":
        x = serpiente.xcor()
        serpiente.setx(x-20)

#--------------Acciones al Pulsar------------------------------------------------------

s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(izquierda, "Left")
s.onkeypress(derecha, "Right")

#--------------Acciones condicionadas del juego------------------------------------------------------------------

while True:
    s.update()

    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        serpiente.home()
        serpiente.direction = "stop"
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto),align="center", font=("verdana", 10, "normal" ))


    if serpiente.distance(comida) < 20:
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("square")
        nuevo_cuerpo.color("green")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,100)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 10
        if marcador > marcador_alto:
            marcador_alto = marcador 
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto),align="center", font=("verdana", 10, "normal" )) 


    total = len(cuerpo)
    for i in range(total -1,0,-1):
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x,y)

    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x,y)



    movimiento()


    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = "stop"

            marcador = 0
            texto.clear()
            texto.write("Marcador:{}\tMarcador mas alto:{}".format(marcador,marcador_alto),align="center", font=("verdana", 10, "normal" ))

    


    time.sleep(retraso)

#-----------------Mantener la ventana abierta--------------------------------------

turtle.done()