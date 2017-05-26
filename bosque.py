from tkinter import *
from ciudad_plateada import pewter_city


def bosque_p1():
    global contenedor3
    town = Toplevel()
    town.title("Pokemon")
    town.geometry("528x475")
    contenedor3 = Canvas(town, width=412, height=600)
    # pone el fondo de bosque al Canvas.
    lista_fondos = []
    lista_fondos.append(PhotoImage(file="imagenes\Bosque_verde.png"))

    contenedor3.create_image(412, 600, anchor=SE, image=lista_fondos[0], tags="FONDO")

    # coloca alsprite en el contenedor3(Canvas)
    lista_img = ["imagenes\jarriba.gif", "imagenes\mright.gif", "imagenes\left.gif", "imagenes\down.gif"]
    direcciones = []

    for imgfile in lista_img:
        photo = PhotoImage(file=imgfile)
        direcciones.append(photo)

    mover2 = contenedor3.create_image(113, 520, anchor=NW, image=direcciones[0], tags="SPRITE")
    # Velocidad del sprite
    vx = 15
    vy = 15

    def izquierda(event):
        contenedor3.itemconfig(mover2, image=direcciones[2])
        x1, y1 = contenedor3.coords(mover2)
        if 76 <= x1 <= 160 and 190 <= y1 <= 400:  # espacio arboles medio izq
            contenedor3.coords(mover2, x1 - vx, y1)
        elif 76 <= x1 <= 160 and 470 <= y1 <= 585:  # arboles abajo
            contenedor3.coords(mover2, x1 - vx, y1)
        elif 76 <= x1 <= 380 and 390 <= y1 <= 470:  # espacio abajo
            contenedor3.coords(mover2, x1 - vx, y1)
        elif 305 <= x1 <= 378 and 2 <= y1 <= 390:  # arboles derecha
            contenedor3.coords(mover2, x1 - vx, y1)


    def derecha(event):
        contenedor3.itemconfig(mover2, image=direcciones[1])
        x1, y1 = contenedor3.coords(mover2)
        if 62 <= x1 <= 336 and 390 <= y1 <= 470:  # espacio abajo
            contenedor3.coords(mover2, x1 + vx, y1)
        elif 62 <= x1 <= 126 and 470 <= y1 <= 590:  # espacio abajo
            contenedor3.coords(mover2, x1 + vx, y1)
        elif 62 <= x1 <= 126 and 190 <= y1 <= 400:  # espacio abajo
            contenedor3.coords(mover2, x1 + vx, y1)
        elif 295 <= x1 <= 335 and 2 <= y1 <= 390:  # arboles derecha
            contenedor3.coords(mover2, x1 + vx, y1)

    def abajo(event):
        contenedor3.itemconfig(mover2, image=direcciones[3])
        x1, y1 = contenedor3.coords(mover2)
        if 390 <= y1 <= 465 and 140 <= x1 <= 293:
            contenedor3.coords(mover2, x1, y1 + vy)
        elif y1 <= 465 and 293 <= x1 <= 340:
            contenedor3.coords(mover2, x1, y1 + vy)
        elif y1 >= 190 and 65 <= x1 <= 140:
            contenedor3.coords(mover2, x1, y1 + vy)

    def arriba(event):
        contenedor3.itemconfig(mover2, image=direcciones[0])
        x1, y1 = contenedor3.coords(mover2)
        if y1 >= 210 and 65 <= x1 <= 140:
            contenedor3.coords(mover2, x1, y1 - vy)
        elif 408 <= y1 <= 515 and 140 <= x1 <= 293:
            contenedor3.coords(mover2, x1, y1 - vy)
        elif 0 <= y1 <= 515 and 293 <= x1 <= 340:
            contenedor3.coords(mover2, x1, y1 - vy)
        elif y1 <= 20:
            town.withdraw()
            bosque_p2()


    contenedor3.bind("<Left>", izquierda)
    contenedor3.bind("<Right>", derecha)
    contenedor3.bind("<Down>", abajo)
    contenedor3.bind("<Up>", arriba)

    contenedor3.focus_set()
    contenedor3.pack()
    town.mainloop()

def bosque_p2():
    forest = Toplevel()
    forest.title("Pokemon")

    canvas = Canvas(forest, width=412, height=600)
    bosque_pt2 = PhotoImage(file="imagenes\Bosque_1r.png")
    canvas.create_image(412, 600, anchor=SE, image=bosque_pt2)


    lista_img = ["imagenes\jarriba.gif", "imagenes\mright.gif", "imagenes\left.gif", "imagenes\down.gif"]
    direcciones_2 = []

    for imgfile in lista_img:
        photo = PhotoImage(file=imgfile)
        direcciones_2.append(photo)

    mover3 = canvas.create_image(311, 570, anchor=NW, image=direcciones_2[0])

    vx = 15
    vy = 15

    def izquierda(event):
        canvas.itemconfig(mover3, image=direcciones_2[2])
        x1, y1 = canvas.coords(mover3)
        if 276 <= x1 <= 375 and 143 <= y1 <= 590:  # espacio arboles medio izq
            canvas.coords(mover3, x1 - vx, y1)
        elif 31 <= x1 <= 375 and 70 <= y1 <= 143:  # arboles abajo
            canvas.coords(mover3, x1 - vx, y1)
        elif 31 <= x1 <= 130 and 70 <= y1 <= 338:  # espacio abajo
            canvas.coords(mover3, x1 - vx, y1)
        elif 10 <= x1 <= 130 and 338 <= y1 <= 470:  # arboles derecha
            canvas.coords(mover3, x1 - vx, y1)
        elif x1 <= 20 and 338 <= y1 <= 470:
            forest.withdraw()
            pewter_city()

    def derecha(event):
        canvas.itemconfig(mover3, image=direcciones_2[1])
        x1, y1 = canvas.coords(mover3)
        if 240 <= x1 <= 305 and 145 <= y1 <= 590:  # espacio abajo
            canvas.coords(mover3, x1 + vx, y1)
        elif 22 <= x1 <= 305 and 30 <= y1 <= 130:
            canvas.coords(mover3, x1 + vx, y1)
        elif 15 <= x1 <= 65 and 130 <= y1 <= 477:
            canvas.coords(mover3, x1 + vx, y1)



    def abajo(event):
        canvas.itemconfig(mover3, image=direcciones_2[3])
        x1, y1 = canvas.coords(mover3)
        if 63 <= y1 <= 600 and 260 <= x1 <= 369:
            canvas.coords(mover3, x1, y1 + vy)
        elif 63 <= y1 <= 101 and 98 <= x1 <= 275:
            canvas.coords(mover3, x1, y1 + vy)
        elif 63 <= y1 <= 415 and 23 <= x1 <= 98:
            canvas.coords(mover3, x1, y1 + vy)

    def arriba(event):
        canvas.itemconfig(mover3, image=direcciones_2[0])
        x1, y1 = canvas.coords(mover3)
        if 85 <= y1 <= 590 and 252 <= x1 <= 361:
            canvas.coords(mover3, x1, y1 - vy)
        elif 85 <= y1 <= 163 and 111 <= x1 <= 252:
            canvas.coords(mover3, x1, y1 - vy)
        elif 85 <= y1 <= 472 and 25 <= x1 <= 111:
            canvas.coords(mover3, x1, y1 - vy)


    canvas.bind("<Left>", izquierda)
    canvas.bind("<Right>", derecha)
    canvas.bind("<Down>", abajo)
    canvas.bind("<Up>", arriba)

    canvas.pack()
    canvas.focus_set()

    forest.mainloop()