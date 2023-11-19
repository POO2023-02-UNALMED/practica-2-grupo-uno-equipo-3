import tkinter as tk
from tkinter import *
from tkinter import messagebox
from gestorAplicacion.productos.producto import Producto 
#from gestorAplicacion.administracion.guia import Guia

class Pagar(Frame): 
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870", highlightthickness=3)
        self.pack(expand=True)
    
        self.Label_Titulo = tk.Label(self, text="Pagar", font=("Arial", 30), fg="#085870")
        self.Label_Titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.Label_descripcion = tk.Label(self, text="En esta funcionalidad podrás escoger la manera de pagar tu envío")
        self.Label_descripcion.grid(row=1, column=0, columnspan=2, pady=10)

        text = Label(self, text="Ingrese el código de su guía", font=("Arial", 12, "bold"))
        text.grid(row=2, column=0, columnspan=2, pady=5, sticky="n")

        entrada= Entry(self)
        entrada.grid(row=3, column=0, columnspan=2, pady=5)

        def verificar():
            if entrada.get() == "":
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")
            
            elif entrada.get().isdigit():
                guia = None

                for producto in Producto.getTodosLosProductos():
                    if producto.getCodigo() == int(entrada.get()):
                        guia = producto.getGuia()
                        break
            else:
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")
                

        boton = Button(self, text="Verificar", command=verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(pady=5)