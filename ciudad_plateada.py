from tkinter import *
from tkinter import messagebox

def pewter_city():
    ventana = Toplevel()
    ventana.title("Pokemon")

    canvas = Canvas(ventana, width=631, height=484)

    fondo = PhotoImage(file="imagenes\Pewter_city.png")
    canvas.create_image(631, 484, anchor=SE, image=fondo)

    lista_img = ["imagenes\jarriba.gif", "imagenes\mright.gif", "imagenes\left.gif", "imagenes\down.gif"]
    direcciones_2 = []

    for imgfile in lista_img:
        photo = PhotoImage(file=imgfile)
        direcciones_2.append(photo)

    mover3 = canvas.create_image(317, 465, anchor=NW, image=direcciones_2[0])

    vx = 15
    vy = 15

    def izquierda(event):
        canvas.itemconfig(mover3, image=direcciones_2[2])
        x1, y1 = canvas.coords(mover3)
        canvas.coords(mover3, x1 - vx, y1)


    def derecha(event):
        canvas.itemconfig(mover3, image=direcciones_2[1])
        x1, y1 = canvas.coords(mover3)
        canvas.coords(mover3, x1 + vx, y1)


    def abajo(event):
        canvas.itemconfig(mover3, image=direcciones_2[3])
        x1, y1 = canvas.coords(mover3)
        canvas.coords(mover3, x1, y1 + vy)

    def arriba(event):
        canvas.itemconfig(mover3, image=direcciones_2[0])
        x1, y1 = canvas.coords(mover3)
        if x1 == 317 and y1 == 465:
            messagebox.showinfo("Felicitaciones", "Has ganado el juego")
        canvas.coords(mover3, x1, y1 - vy)


    canvas.bind("<Left>", izquierda)
    canvas.bind("<Right>", derecha)
    canvas.bind("<Down>", abajo)
    canvas.bind("<Up>", arriba)

    canvas.pack()
    canvas.focus_set()

    ventana.mainloop()