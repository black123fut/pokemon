from tkinter import *

def juego():
    pantalla = Toplevel()
    pantalla.title("Pokemon")
    pantalla.minsize(400, 400)
    contenedor = Canvas(pantalla, width=400, height=400)
    contenedor.create_rectangle(200, 175, 320, 225, width=0 , fill="brown")

    gif_i1 = PhotoImage(file="imagenes\obajo_1.png")
    izq = contenedor.create_image(200, 200, anchor=NW, image=gif_i1)

    vx = 10
    vy = 10

    def izquierda(event):
        x1, y1 = contenedor.coords(izq)
        contenedor.coords(izq, x1 - vx, y1)

    def derecha(event):
        x2, y2 = contenedor.coords(izq)
        contenedor.coords(izq, x2 + vx, y2)

    def abajo(event):
        x3, y3 = contenedor.coords(izq)
        contenedor.coords(izq, x3, y3 + vy)

    def arriba(event):
        x4, y4 = contenedor.coords(izq)
        contenedor.coords(izq, x4, y4 - vy)

    if izq == contenedor.place(x=200, y=400):
        paleta = Toplevel()
        pantalla.withdraw()
        paleta.title("Pokemon")
        paleta.minsize(400, 400)





    contenedor.bind("<Left>", izquierda)
    contenedor.bind("<Right>", derecha)
    contenedor.bind("<Down>", abajo)
    contenedor.bind("<Up>", arriba)

    contenedor.focus_set()
    contenedor.pack()
    contenedor.pack(padx=10, pady=10)

    pantalla.mainloop()