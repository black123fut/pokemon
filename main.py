from tkinter import *
from character import juego


def comienzo():
    root = Toplevel()
    main.withdraw()
    root.title("Pokemon")
    root.geometry("400x400")

    diag1 = Label(root, text="Hola " + entrada_nombre.get() + "! \n Bienvenido al mundo pokemon. \n Mi nombre es OAK,\
    este mundo esta habitado por criaturas \n llamadas pokemon, para algunas persona \n son mascotas y otras los usan \
    para luchar, dejando \n esto de lado tu propia leyenda pokemon esta \n punto de comenzar! Un mundo de aventuras \n \
    te esperan! Vamos!")
    img_1 = PhotoImage(file="imagenes\doctor.png")
    label_com = Label(root, image=img_1, bg="black")
    boton_game = Button(root, text="Continuar", command=juego, width=8, height=3, bg="yellow")

    boton_game.pack(side=BOTTOM)
    diag1.pack(side=TOP)
    label_com.pack(side=TOP)



main = Tk()
main.title("Pokemon")
main.geometry("400x400")

nombre = Label(main, text="¿Cual es tu nombre? \n Nombre:")
entrada_nombre = Entry(main)
boton1 = Button(main, text="Jugar", command=comienzo, width=8, height=3, bg="yellow")

imagen_1 = PhotoImage(file="imagenes\pokemon1.png")
label_img = Label(main, image=imagen_1)

imagen_2 = PhotoImage(file="imagenes\doctor.png")
label_img1 = Label(main, image=imagen_2)

boton1.pack(side=BOTTOM)
label_img.pack(side=TOP)
label_img1.pack(side=BOTTOM)
nombre.pack(side=LEFT)
entrada_nombre.pack(side=LEFT)


main.mainloop()
