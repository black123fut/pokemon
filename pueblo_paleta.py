from tkinter import *
from bosque import bosque_p1


def pueblo():
    pantalla = Toplevel()
    pantalla.title("Pokemon")

    contenedor = Canvas(pantalla, width=520, height=433)
    # Pone el fondo al Canvas.
    background_image2 = PhotoImage(file="imagenes\paleta.png")
    contenedor.create_image(520, 433, anchor=SE, image=background_image2)

    # Pone al sprite en el Canvas.
    lista_img = ["imagenes\jarriba.gif", "imagenes\mright.gif", "imagenes\left.gif", "imagenes\down.gif"]
    direcciones = []

    for imgfile in lista_img:
        photo = PhotoImage(file=imgfile)
        direcciones.append(photo)

    mover = contenedor.create_image(355, 311, anchor=NW, image=direcciones[3])

    # variables de la velocidad de movimiento del sprite.
    vx = 10
    vy = 10

    # define las limitaciones al moverse hacia: L, R, U, D.
    def izquierda(event):
        contenedor.itemconfig(mover, image=direcciones[2])
        x1, y1 = contenedor.coords(mover)
        if 50 <= x1 and 37 <= y1 <= 54:  # limite espacio arriba
            contenedor.coords(mover, x1 - vx, y1)
        elif 50 <= x1 <= 103 and 54 <= y1 <= 172: #casa izquierda
            contenedor.coords(mover, x1 - vx, y1)
        elif 225 <= x1 <= 295 and 54 <= y1 <= 172: #medio casas
            contenedor.coords(mover, x1 - vx, y1)
        elif 425 <= x1 and 54 <= y1 <= 172: #casa derecha
            contenedor.coords(mover, x1 - vx, y1)
        elif 50 <= x1 and 161 <= y1 <= 187: #espacio mitad
            contenedor.coords(mover, x1 - vx, y1)
        elif 50 <= x1 <= 280 and 182 <= y1 <= 301: #laboratorio izq-arboles
            contenedor.coords(mover, x1 - vx, y1)
        elif 442 <= x1 and 182 <= y1 <= 290: #laboratorio der-arboles
            contenedor.coords(mover, x1 - vx, y1)
        elif 50 <= x1 and 290 <= y1 <= 347: #espacio abajo
            contenedor.coords(mover, x1 - vx, y1)
        elif 50 <= x1 <= 145 and 347 <= y1 <= 420: #izq-lago
            contenedor.coords(mover, x1 - vx, y1)
        elif 243 <= x1 and 347 <= y1 <= 420: #lago-derecha
            contenedor.coords(mover, x1 - vx, y1)

    #abajo y -18
    def derecha(event):
        contenedor.itemconfig(mover, image=direcciones[1])
        x1, y1 = contenedor.coords(mover)
        if 40 <= x1 <= 433 and 37 <= y1 <= 54: #espacio arriba
            contenedor.coords(mover, x1 + vx, y1)
        elif x1 <= 62 and 54 <= y1 <= 172: # izq- casa izq
            contenedor.coords(mover, x1 + vx, y1)
        elif 209 <= x1 <= 260 and 54 <= y1 <= 172: #medio casa
            contenedor.coords(mover, x1 + vx, y1)
        elif 409 <= x1 <= 433 and 54 <= y1 <= 172: #casa der - derecha
            contenedor.coords(mover, x1 + vx, y1)
        elif x1 <= 433 and 161 <= y1 <= 187: #espacio mitad
            contenedor.coords(mover, x1 + vx, y1)
        elif x1 <= 235 and 182 <= y1 <= 290: #laboratorio - izquierda
            contenedor.coords(mover, x1 + vx, y1)
        elif 400 <= x1 <= 433 and 182 <= y1 <= 301: #laboratorio - derecha
            contenedor.coords(mover, x1 + vx, y1)
        elif x1 <= 433 and 290 <= y1 <= 347: #espacio abajo
            contenedor.coords(mover, x1 + vx, y1)
        elif x1 <= 105 and 347 <= y1 <= 420: #izq - lago
            contenedor.coords(mover, x1 + vx, y1)
        elif 235 <= x1 <= 433 and 347 <= y1 <= 420: #lago - derecha
            contenedor.coords(mover, x1 + vx, y1)

    def abajo(event):
        contenedor.itemconfig(mover, image=direcciones[3])
        x1, y1 = contenedor.coords(mover)
        if 290 <= y1 <= 380 and 270 <= x1 <= 433: #lab - abajo
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 380 and 433 <= x1 <= 484: #lab derecha
            contenedor.coords(mover, x1, y1 + vy)
        elif 157 <= y1 <= 175 and 300 <= x1 <= 418: #casa der - lab
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 175 and 412 <= x1 <= 484: #casa der - der
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 39 and 285 <= x1 <= 412: #espacio arriba casa derecha
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 175 and 265 <= x1 <= 286: #espacio medio derecha
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 380 and 238 <= x1 <= 265: #espacio medio medio
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 320 and 210 <= x1 <= 238: #espacio medio izquierda
            contenedor.coords(mover, x1, y1 + vy)
        elif 157 <= y1 <= 320 and 150 <= x1 <= 210: #casa izq - lago
            contenedor.coords(mover, x1, y1 + vy)
        elif 157 <= y1 <= 380 and 95 <= x1 <= 150: #casa izq - abajo
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 380 and 38 <= x1 <= 95: #espacio izquierda
            contenedor.coords(mover, x1, y1 + vy)
        elif 32 <= y1 <= 39 and 90 <= x1 <= 218: #espacio arriba casa izquierda
            contenedor.coords(mover, x1, y1 + vy)

    def arriba(event):
        contenedor.itemconfig(mover, image=direcciones[0])
        x1, y1 = contenedor.coords(mover)
        if 175 <= y1 <= 200 and 304 <= x1 <= 412: # casa der-lab
            contenedor.coords(mover, x1, y1 - vy)
        elif 306 <= y1 <= 430 and 270 <= x1 <= 433: #abajo - lab
            contenedor.coords(mover, x1, y1 - vy)
        elif 48 <= y1 <= 203 and 412 <= x1 <= 434: #espacio casa derecha
            contenedor.coords(mover, x1, y1 - vy)
        elif 48 <= y1 <= 430 and 434 <= x1 <= 460: #espacio arboles derecha
            contenedor.coords(mover, x1, y1 - vy)
        elif 48 <= y1 <= 74 and 35 <= x1 <= 475: #arboles arriba derecha
            contenedor.coords(mover, x1, y1 - vy)
        elif 175 <= y1 <= 430 and 98 <= x1 <= 210: #casa izq arriba
            contenedor.coords(mover, x1, y1 - vy)
        elif 48 <= y1 <= 430 and 35 <= x1 <= 98:  #arboles - casa izq
            contenedor.coords(mover, x1, y1 - vy)
        elif 25 <= y1 <= 175 and 265 <= x1 <= 286: #espacio medio derecha
            contenedor.coords(mover, x1, y1 - vy)
        elif 48 <= y1 <= 400 and 243 <= x1 <= 265: #espacio medio medio
            contenedor.coords(mover, x1, y1 - vy)
        elif 48 <= y1 <= 337 and 210 <= x1 <= 244: #espacio medio izquierda
            contenedor.coords(mover, x1, y1 - vy)
        elif y1 <= 30 and 260 <= x1 <= 310:
            pantalla.withdraw()  # cierra la vetana del pueblo_paleta.
            bosque_p1()  # Abre el la funcion del bosque verde.

    contenedor.bind("<Right>", derecha)
    contenedor.bind("<Left>", izquierda)
    contenedor.bind("<Down>", abajo)
    contenedor.bind("<Up>", arriba)

    contenedor.pack()
    contenedor.focus_set()
    pantalla.mainloop()

