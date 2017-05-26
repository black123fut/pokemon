from tkinter import *
from pueblo_paleta import pueblo


def juego():
    global contenedor
    pantalla = Toplevel()
    pantalla.title("Pokemon")
    pantalla.minsize(335, 400)

    contenedor = Canvas(pantalla, width=335, height=400)

    # Pone el fondo al Canvas.
    background_image = PhotoImage(file="imagenes\laboratorio.png")
    contenedor.create_image(335, 400, anchor=SE, image=background_image)

    # Pone al sprite en el Canvas.
    lista_img = ["imagenes\jarriba.gif", "imagenes\mright.gif", "imagenes\left.gif", "imagenes\down.gif"]
    direcciones = []

    for imgfile in lista_img:
        photo = PhotoImage(file=imgfile)
        direcciones.append(photo)

    movimiento = contenedor.create_image(160, 200, anchor=NW, image=direcciones[0])

    # variables de la velocidad de movimiento del sprite.
    vx = 20
    vy = 20

    # Pone las limitaciones al moverse a la izquierda.
    def izquierda(event):
            contenedor.itemconfig(movimiento, image=direcciones[2])
            x1, y1 = contenedor.coords(movimiento)
            if x1 >= 14 and 73 <= y1 <= 175:  # Espacio arriba
                contenedor.coords(movimiento, x1 - vx, y1)
            elif x1 >= 142 and 29 <= y1 <= 73:  # Mitad salon
                contenedor.coords(movimiento, x1 - vx, y1)
            elif x1 >= 142 and 190 <= y1 <= 255:  # Limite libros izquierda
                contenedor.coords(movimiento, x1 - vx, y1)
            elif x1 >= 14 and 256 <= y1 <= 385:  # Espacio Abajo
                contenedor.coords(movimiento, x1 - vx, y1)


                # Pone las limitaciones al moverse a la derecha.

        # -25 abajo y -25 derecha, arriba -10
    def derecha(event):
            contenedor.itemconfig(movimiento, image=direcciones[1])
            x1, y1 = contenedor.coords(movimiento)
            if x1 <= 280 and 135 <= y1 <= 175:  # Espacio medio
                contenedor.coords(movimiento, x1 + vx, y1)
            elif x1 <= 152 and 190 <= y1 <= 255:  # limite libros derecha
                contenedor.coords(movimiento, x1 + vx, y1)
            elif x1 <= 152 and 100 <= y1 <= 147:  # limite mesa  205
                contenedor.coords(movimiento, x1 + vx, y1)
            elif x1 <= 280 and 60 <= y1 <= 83:  # Espacio arriba
                contenedor.coords(movimiento, x1 + vx, y1)
            elif x1 <= 280 and 256 <= y1 <= 385:  # Espacio abajo
                contenedor.coords(movimiento, x1 + vx, y1)
            elif x1 <= 152 and 29 <= y1 <= 60:  # Mitad de salon
                contenedor.coords(movimiento, x1 + vx, y1)

                # Pone las limitaciones al moverse hacia abajo.

    def abajo(event):
            contenedor.itemconfig(movimiento, image=direcciones[3])
            x1, y1 = contenedor.coords(movimiento)
            if 73 <= y1 <= 153 and 14 <= x1 <= 142:  # libros izquierda
                contenedor.coords(movimiento, x1, y1 + vy)
            elif 32 <= y1 <= 52 and 175 <= x1 <= 303:  # libros mesa
                contenedor.coords(movimiento, x1, y1 + vy)
            elif 135 <= y1 <= 153 and 175 <= x1 <= 303:  # libros derecha
                contenedor.coords(movimiento, x1, y1 + vy)
            elif 256 <= y1 <= 380 and 175 <= x1 <= 303:  # borde bajo der
                contenedor.coords(movimiento, x1, y1 + vy)
            elif 256 <= y1 <= 380 and 14 <= x1 <= 142:  # borde bajo izq
                contenedor.coords(movimiento, x1, y1 + vy)
            elif 10 <= y1 <= 355 and 135 <= x1 <= 182:  # borde mitad salon
                contenedor.coords(movimiento, x1, y1 + vy)
            elif y1 >= 355 and 135 <= x1 <= 182:  # entrada a pueblo_paleta
                pantalla.withdraw()
                pueblo()  # Abre la funcion del pueblo_violeta.

                # Pone las limitaciones al moverse hacia arriba.

    def arriba(event):
            contenedor.itemconfig(movimiento, image=direcciones[0])
            x1, y1 = contenedor.coords(movimiento)
            if 173 >= y1 >= 90 and 14 <= x1 <= 142:  # limite mueble + computadora
                contenedor.coords(movimiento, x1, y1 - vy)
            elif 83 >= y1 >= 77 and 175 <= x1 <= 303:  # libros superior derecha
                contenedor.coords(movimiento, x1, y1 - vy)
            elif 185 >= y1 >= 155 and 175 <= x1 <= 303:  # limite mesa
                contenedor.coords(movimiento, x1, y1 - vy)
            elif 390 >= y1 >= 35 and 135 <= x1 <= 185:  # borde arriba
                contenedor.coords(movimiento, x1, y1 - vy)
            elif 400 >= y1 >= 267 and 14 <= x1 <= 142:  # libros izquierda
                contenedor.coords(movimiento, x1, y1 - vy)
            elif 400 >= y1 >= 267 and 185 <= x1 <= 303:  # libros derecha
                contenedor.coords(movimiento, x1, y1 - vy)

    contenedor.bind("<Left>", izquierda)
    contenedor.bind("<Right>", derecha)
    contenedor.bind("<Down>", abajo)
    contenedor.bind("<Up>", arriba)
    contenedor.focus_set()
    contenedor.pack()
    pantalla.mainloop()

