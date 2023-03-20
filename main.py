import re
from Obj.Ahorcado import Ahorcado
from Serv.AhorcadoServicio import AhorcadoServicio
from tkinter import *
from tkinter import messagebox


def reset():
    entradaPalabra.config(state = "normal")
    entradaPalabra.delete("0", "end")
    entradaPalabra.config(state=DISABLED)
    botonEnviarPalabra.config(state = DISABLED)
    entradaLetra.config(state = DISABLED)
    botonEnviarLetra.config(state = DISABLED)
    textoIntentos.config(text="")
    textoSecreto.config(text="")
    textoEstado.config(text="Juego Terminado, para reiniciar ve a Archivo-> Nuevo Juego")
    juego1.__init__()
    window.update()

def juevoNuevo():

    entradaPalabra.config(state="normal")
    botonEnviarPalabra.config(state="normal")
    textoEstado.config(text="Juego en curso")

def palabraSecreta():
    palabra = entradaPalabra.get()
    sa.inicializar_parametros(juego1, palabra)
    botonEnviarPalabra.config(state=DISABLED)
    entradaPalabra.config(state=DISABLED)
    entradaLetra.config(state="normal")
    botonEnviarLetra.config(state="normal")
    textoSecreto.config(text=juego1.get_ahorcado())
    textoIntentos.config(text=(f"Te quedan {juego1.get_intentos()} intentos"))

def enviarLetra():
    if juego1.get_intentos() > 0:
        letra = entradaLetra.get()
        sa.iniciar_juego(juego1, letra)
        textoIntentos.config(text=(f"Te quedan {juego1.get_intentos()} intentos"))
        textoSecreto.config(text=juego1.get_ahorcado())
        entradaLetra.delete("0", "end")
        window.update()
        if juego1.get_intentos()  == 0:
            messagebox.showinfo("PERDISTE", "JAJAJA PERDISTE OTRA VEZ")
            reset()
        elif (juego1.gano() == True):
            messagebox.showinfo("GANASTE", "FELICIDADES SOS EL GANADOR DE ESTA RONDA")
            reset()

def enter(event):
    enviarLetra()

def acercaDe():
    messagebox.showinfo("Acerca de...", "Creado con fines de estudio\n Autor: Pablo Velasco"
                                        "\npor dudasy/o sugerencias\n contacto: pablor.velasco.suarez@gmail.com",)
def salir():
    window.destroy()



#Interfaz
window = Tk()
window.title("Ahorcado x_x")
window.geometry("400x300")
window.resizable(0, 0)

#logica del ejercicio
juego1 = Ahorcado()
sa = AhorcadoServicio()

#widgets interfaz ventana


textoPalabra = Label(window, text="Ingresa palabra secreta!", font=('arial', 10, 'bold'))
entradaPalabra =Entry(window, show="*", state=DISABLED, width=25, font=('arial', 8, 'bold'))
botonEnviarPalabra = Button(window, text="Palabra secreta ok!", state = DISABLED, command= palabraSecreta,
                            width=20, font=('arial', 8, 'bold'))

textoLetra = Label(window, text="Ingresa una letra!", font=('arial', 10, 'bold'))
entradaLetra = Entry(window, state = DISABLED, width=25, font=('arial', 8, 'bold'))
botonEnviarLetra = Button(window, text="Enviar", state = DISABLED, command=enviarLetra,
                            width=20, font=('arial', 8, 'bold'))

textoSecreto = Label(window, borderwidth=1, width=25, font=('arial', 15, 'bold'))

textoIntentos = Label(window, borderwidth=1,  width=25, font=('arial', 10, 'bold'), fg="red")

textoEstado = Label(window, text="Para iniciar el juego ve a Archivo-> Nuevo Juego", width=50)

#bind del enter a el boton enviar letra
window.bind('<Return>', enter)

#Widgets de la barra de menu
barraMenu = Menu(window)
archivoMenu =Menu(barraMenu)


barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
archivoMenu.add_command(label="Nuevo Juego", command= juevoNuevo)
archivoMenu.add_command(label="Reset", command=reset)
archivoMenu.add_command(label="Salir", command=salir)
barraMenu.add_command(label="Acerca de", command=acercaDe)

#Posicion/formato de widgets
window.config(menu=barraMenu)


# posicion en la grilla


textoPalabra.grid(row = 0, column = 0, pady=3, ipady=3)
entradaPalabra.grid(row = 1, column = 0, pady=5, ipady=5)
botonEnviarPalabra.grid(row = 2, column = 0, pady=5, ipady=5)




textoLetra.grid(row = 3, column = 0, pady=3, ipady=3)
entradaLetra.grid(row=4, column=0, pady=5, ipady=5)
botonEnviarLetra.grid(row=5, column=0, pady=5, ipady=5)


textoSecreto.grid(row=0,column=1, pady=5, ipady=5)
textoIntentos.grid(row=1,column=1, pady=5, ipady=5)

textoEstado.grid(row=6, column=0, columnspan=2,pady= 25)


window.mainloop()

