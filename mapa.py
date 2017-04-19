from tkinter import *


def campo():
    pantalla = Toplevel()
    pantalla.title("Pokemon")
    pantalla.minsize(400, 400)
    contenedor = Canvas(pantalla, width=400, height=400)

    gif_i1 = PhotoImage(file="izquierda_1.png")
    izq = contenedor.create_image(200, 200, anchor=NW, image=gif_i1)
