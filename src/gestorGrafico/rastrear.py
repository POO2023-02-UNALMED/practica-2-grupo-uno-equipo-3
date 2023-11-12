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
            elif entrada.get().isdigit():
                guia = None
            
                for producto in Producto.getTodosLosProductos():
                    if producto.getCodigo == int(entrada.get()):
                        guia = producto.getGuia
                        break
            else:
                return messagebox.showwarning("Error, ingrese un código válido")
            
            if guia != None:
                return messagebox.showwarning("codigo correcto")
            else:
                return messagebox.showwarning("Lo sentimos, el código de la guía no coincide, intentelo de nuevo")

                


            

        frame = Frame(ventana, width=400, height=200,bg="green",highlightbackground="#085870",highlightthickness=5)
        frame.pack(expand=True)
        
        texto0 = ("Esta funcionalidad permite:\n1. Agregar una nueva materia al sistema. 3. Agregar un grupo a una materia existente."+
                 "\n2. Eliminar una materia existente del sistema. 4. Eliminar un grupo existente en alguna materia.")
        descripcion = Label(self, text=texto0, font=("Arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20, padx=5)
        
        entrada = Entry(frame)
        texto=Label(frame,text="Ingrese el código de su paquete:", font=("arial", 11, "bold"))
        boton = Button(frame, text="Verificar", command= verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(side="bottom")
        texto.pack(side="top",pady=10)
        entrada.pack(side="bottom", pady=5)