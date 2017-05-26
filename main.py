from tkinter import *
from laboratorio import juego
import time
import pygame
from tkinter import messagebox

#comienzo
#El boton da comienzo al juego

ind_lista = 0

def hip(event):
    global ind_lista, contenedor
    root.withdraw()

    pantalla = Toplevel()
    pantalla.title("pokemon")
    pantalla.geometry("750x490")

    contenedor = Canvas(pantalla, width=750, height=500)

    lista = ["img\i_1.gif", "img\i_2.gif", "img\i_3.gif", "img\i_4.gif", "img\i_5.gif", "img\i_6.gif",
             "img\i_7.gif", "img\i_8.gif", "img\i_9.gif", "img\i_10.gif", "img\i_11.gif", "img\i_12.gif",
             "img\i_13.gif", "img\i_14.gif"]
    lista_oak = []

    for files in lista:
        img01 = PhotoImage(file=files)
        lista_oak.append(img01)

    actual = contenedor.create_image(0, 0, anchor=NW, image=lista_oak[ind_lista])

    def siguiente(event):
        global ind_lista
        ind_lista += 1
        contenedor.itemconfig(actual, image=lista_oak[ind_lista])
        if ind_lista == 11:
            nombre = Entry(pantalla)
            nombre.place(x=50, y=100)
        elif ind_lista == 13:
            transicion()

    contenedor.bind("<Right>", siguiente)
    contenedor.focus_set()
    contenedor.pack()
    pantalla.mainloop()


def transicion():
    global contenedor
    tran_lista = ["img\q_1.gif", "img\q_2.gif", "img\q_3.gif", "img\q_4.gif", "img\q_5.gif", "img\q_6.gif"]
    lista_fotos = []

    for ind in tran_lista:
        foto = PhotoImage(file=ind)
        lista_fotos.append(foto)

    # loop through the gif image objects for a while
    for t in range(0, 1):
        for gif in lista_fotos:
            contenedor.delete(ALL)
            contenedor.create_image(740, 500,anchor=SE ,image=gif)
            contenedor.update()
            time.sleep(0.7)
        if t == 0:
            juego()



root = Tk()
root.title("pokemon")
root.geometry("740x500")

imagelist = ["imagenes\Frame 1.gif", "imagenes\Frame 2.gif"]

# extract width and height info
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(root, width=width, height=height)
canvas.pack()

#Entrada: El nombre del jugador.
#Salida: La siguiente función.
#Guarda el nombre introducido en el Entry para ser usado en el juego.


canvas.bind("<Button-1>", hip)
# create a list of image objects
giflist = []

for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)

# loop through the gif image objects for a while
for k in range(0, 1000):
    for gif in giflist:
        canvas.delete(ALL)
        canvas.create_image(width / 2.0, height / 2.0, image=gif)
        canvas.update()
        time.sleep(0.5)

root.mainloop()