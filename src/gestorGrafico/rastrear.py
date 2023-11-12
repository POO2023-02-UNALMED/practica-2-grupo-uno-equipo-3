import tkinter as tk
from tkinter import *
from tkinter import messagebox

class Rastrear(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)

        def consultarProgreso():
            self.pack_forget()
            pro = progreso(ventana)
            pro.pack()


        def verificar():
            lista=[12345]

            if entrada.get() == "":
                return messagebox.showwarning("Error")

            for codigo in lista:
                if codigo == int(entrada.get()):
                    exist = True
                return messagebox.showwarning("codigo correcto")
                break

        frame = Frame(ventana, width=400, height=200,bg="green",highlightbackground="#085870",highlightthickness=5)
        frame.pack(expand=True)
        entrada = Entry(frame)
        texto=Label(frame,text="Ingrese el código de su paquete:", font=("arial", 11, "bold"))
        boton = Button(frame, text="Verificar", command= verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(side="bottom")
        texto.pack(side="top",pady=10)
        entrada.pack(side="bottom", pady=5)