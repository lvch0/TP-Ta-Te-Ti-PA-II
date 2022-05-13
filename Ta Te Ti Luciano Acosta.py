from tkinter import *
import random

def next_turn(fila, columna):

    global jugador

    if botones[fila][columna]['text'] == "" and checkeoGanador() is False:

        if jugador == jugadores[0]:

            botones[fila][columna]['text'] = jugador

            if checkeoGanador() is False:
                jugador = jugadores[1]
                label.config(text=("Turno de  "+jugadores[1]))

            elif checkeoGanador() is True:
                label.config(text=(jugadores[0]+" es el ganador"))

            elif checkeoGanador() == "Empate":
                label.config(text="Empate")

        else:

            botones[fila][columna]['text'] = jugador

            if checkeoGanador() is False:
                jugador = jugadores[0]
                label.config(text=("Turno de "+jugadores[0]))

            elif checkeoGanador() is True:
                label.config(text=(jugadores[1]+" es el ganador"))

            elif checkeoGanador() == "Empate":
                label.config(text="Empate")

def checkeoGanador():

    for fila in range(3):
        if botones[fila][0]['text'] == botones[fila][1]['text'] == botones[fila][2]['text'] != "":
            botones[fila][0].config(bg="green")
            botones[fila][1].config(bg="green")
            botones[fila][2].config(bg="green")
            return True

    for columna in range(3):
        if botones[0][columna]['text'] == botones[1][columna]['text'] == botones[2][columna]['text'] != "":
            botones[0][columna].config(bg="green")
            botones[1][columna].config(bg="green")
            botones[2][columna].config(bg="green")
            return True

    if botones[0][0]['text'] == botones[1][1]['text'] == botones[2][2]['text'] != "":
        botones[0][0].config(bg="green")
        botones[1][1].config(bg="green")
        botones[2][2].config(bg="green")
        return True

    elif botones[0][2]['text'] == botones[1][1]['text'] == botones[2][0]['text'] != "":
        botones[0][2].config(bg="green")
        botones[1][1].config(bg="green")
        botones[2][0].config(bg="green")
        return True

    elif espaciosVacios() is False:

        for fila in range(3):
            for columna in range(3):
                botones[fila][columna].config(bg="yellow")
        return "Empate"

    else:
        return False


def espaciosVacios():

    espacios = 9

    for filas in range(3):
        for columnas in range(3):
            if botones[filas][columnas]['text'] != "":
                espacios -= 1

    if espacios == 0:
        return False
    else:
        return True

def new_game():

    global jugador

    jugador = random.choice(jugadores)

    label.config("Turno de", text=jugador)

    for filas in range(3):
        for columnas in range(3):
            botones[filas][columnas].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Ta-Te-Ti")
jugadores = ["x","o"]
jugador = random.choice(jugadores)
botones = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=jugador + " turno", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="Iniciar", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for filas in range(3):
    for columnas in range(3):
        botones[filas][columnas] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda filas=filas, columnas=columnas: next_turn(filas,columnas))
        botones[filas][columnas].grid(row=filas,column=columnas)

window.mainloop()