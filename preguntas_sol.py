from tkinter import *
from functools import partial
import random

puntaje = 10
numero_pregunta = 1
contador_pregunta = 1
correcta = ""

incorrectas = []
primera_ronda = True


def siguiente_pregunta():

    global correcta

    if numero_pregunta == 1:

        pregunta.config(
            text="¿Qué es el Sol y qué tipo de astro es?"
        )

        correcta = "Es una estrella y el centro del Sistema Solar."

    elif numero_pregunta == 2:

        pregunta.config(
            text="¿Cuál es la importancia del Sol para la vida en la Tierra?"
        )

        correcta = "Luz y calor, indispensables para la vida."

    elif numero_pregunta == 3:

        pregunta.config(
            text="¿Dónde se encuentra ubicado el Sol dentro del Sistema Solar?"
        )

        correcta = "En el centro del Sistema Solar."

    elif numero_pregunta == 4:

        pregunta.config(
            text="¿Cuál es la composición principal del Sol?"
        )

        correcta = "Principalmente hidrógeno y helio."

    elif numero_pregunta == 5:

        pregunta.config(
            text="¿Cuál es aproximadamente la temperatura de la superficie solar?"
        )

        correcta = "Aproximadamente 5.500 °C."

    elif numero_pregunta == 6:

        pregunta.config(
            text="¿Qué dimensiones tiene el Sol en comparación con la Tierra?"
        )

        correcta = "Su diámetro es unas 109 veces mayor que el de la Tierra."

    elif numero_pregunta == 7:

        pregunta.config(
            text="¿A qué distancia aproximada se encuentra el Sol de la Tierra?"
        )

        correcta = "A unos 150 millones de kilómetros."

    elif numero_pregunta == 8:

        pregunta.config(
            text="¿Cómo se produce la energía que emite el Sol?"
        )

        correcta = "Mediante la fusión nuclear de átomos de hidrógeno en su núcleo."

    elif numero_pregunta == 9:

        pregunta.config(
            text="¿Cuáles son las principales capas que componen la estructura del Sol?"
        )

        correcta = "Núcleo, zona radiativa, zona convectiva, fotosfera, cromosfera y corona."

    elif numero_pregunta == 10:

        pregunta.config(
            text="¿Qué función cumple el Sol en el mantenimiento del clima terrestre?"
        )

        correcta = "Proporciona la energía que impulsa el clima y los fenómenos atmosféricos."


def comprobar(boton):

    global puntaje
    global numero_pregunta
    global contador_pregunta
    global primera_ronda

    respuesta = boton.cget("text")

    if respuesta == correcta:

        resultado.config(
            text="Correcto",
            fg="green"
        )

    else:

        resultado.config(
            text="Incorrecto",
            fg="red"
        )

        if numero_pregunta not in incorrectas:

            incorrectas.append(numero_pregunta)

            if primera_ronda:
                puntaje -= 1


    # --------------------------
    # PRIMERA RONDA
    # --------------------------

    if primera_ronda:

        if len(orden_preguntas) > 0:

            numero_pregunta = orden_preguntas.pop(0)

            subtitulo.config(
                text=f"Pregunta {contador_pregunta}/10"
            )

            contador_pregunta += 1

            siguiente_pregunta()

        else:

            # Terminó la primera ronda
            primera_ronda = False

            # ¿Hay preguntas incorrectas?
            if len(incorrectas) > 0:

                numero_pregunta = incorrectas.pop(0)

                subtitulo.config(
                    text=f"Pregunta {contador_pregunta}/10"
                )

                contador_pregunta += 1

                siguiente_pregunta()

            else:

                terminar()


    else:

        if len(incorrectas) > 0:

            numero_pregunta = incorrectas.pop(0)

            subtitulo.config(
                text=f"Pregunta {contador_pregunta}/10"
            )

            contador_pregunta += 1

            siguiente_pregunta()

        else:

            terminar()


def terminar():

    pregunta.config(
        text="Game Over"
    )

    subtitulo.config(
        text=f"Puntaje: {puntaje}/10"
    )

    for b in botones:
        b.config(state=DISABLED)



base = Tk()
base.geometry("1000x800")


frame1 = Frame(base)
frame1.config(
    bg="light blue",
    height=200,
    width=700
)
frame1.pack(
    fill="both",
    expand=True
)


title = Label(frame1)
title.config(
    text="Sobre el sol",
    font=("Arial", 40)
)
title.pack()


subtitulo = Label(frame1)
subtitulo.config(
    text="Pregunta 1/10",
    font=("Arial", 30)
)
subtitulo.pack(pady=10)


pregunta = Label(frame1)
pregunta.config(
    text="",
    font=("Arial", 25)
)
pregunta.pack(pady=1)


resultado = Label(
    base,
    text="",
    font=("Arial", 25)
)
resultado.pack(pady=10)


frame2 = Frame(base)
frame2.config(
    bg="pink",
    height=700,
    width=600
)
frame2.pack(pady=1)


respuestas = [
    "Es una estrella y el centro del Sistema Solar.",
    "Luz y calor, indispensables para la vida.",
    "En el centro del Sistema Solar.",
    "Principalmente hidrógeno y helio.",
    "Aproximadamente 5.500 °C.",
    "Su diámetro es unas 109 veces mayor que el de la Tierra.",
    "A unos 150 millones de kilómetros.",
    "Mediante la fusión nuclear de átomos de hidrógeno en su núcleo.",
    "Núcleo, zona radiativa, zona convectiva, fotosfera, cromosfera y corona.",
    "Proporciona la energía que impulsa el clima y los fenómenos atmosféricos."
]

botones = []

orden_preguntas = list(range(1, 11))
random.shuffle(orden_preguntas)

numero_pregunta = orden_preguntas.pop(0)


for texto in respuestas:

    btn = Button(
        frame2,
        text=texto,
        width=80,
        font=("Arial", 15),
        bg="white"
    )

    btn.config(
        command=partial(comprobar, btn)
    )

    btn.pack(pady=1)

    botones.append(btn)


siguiente_pregunta()

base.mainloop()
