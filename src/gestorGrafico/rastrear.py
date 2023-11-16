import tkinter as tk
from tkinter import *
from tkinter import messagebox
from gestorAplicacion.productos.producto import Producto 
from gestorAplicacion.administracion.guia import Guia

class Rastrear(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)

        def consultarProgreso():
            self.pack_forget()
            estado = Estado(ventana, entrada.get())
            estado.pack()
            
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
                consultarProgreso
            else:
                return messagebox.showwarning("Lo sentimos, el código de la guía no coincide, intentelo de nuevo")

                


            

        frame = Frame(self,bg="green",highlightbackground="#085870",highlightthickness=5)
        frame.pack(fill=tk.BOTH,expand=True)
        
        texto0 = ("Esta funcionalidad permite:\n1. Agregar una nueva materia al sistema. 3. Agregar un grupo a una materia existente."+
                 "\n2. Eliminar una materia existente del sistema. 4. Eliminar un grupo existente en alguna materia.")
        descripcion = Label(frame, text=texto0, font=("Arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20, padx=5)
        
        entrada = Entry(frame)
        texto=Label(frame,text="Ingrese el código de su paquete:", font=("arial", 11, "bold"))
        boton = Button(frame, text="Verificar", command= consultarProgreso,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(side="bottom")
        texto.pack(side="top",pady=10)
        entrada.pack(side="bottom", pady=5)
        
class Estado(Frame):
    def __init__(self, ventana, guia):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)
        
        enviado = False
        
        if guia.getTipoDePago() == Guia.tipoDePago.REMITENTE:
            if guia.getPagoPendiente() == 0:
                enviado = True
        
        elif guia.getTipoDePago() == Guia.tipoDePago.FRACCIONADO:
            if guia.getPagoPendiente() == guia.getPrecioTotal() / 2:
                enviado = True
        
        else:
            enviado = True
        
        if enviado:
            frame = Frame(ventana, width=400, height=200,bg="green",highlightbackground="#085870",highlightthickness=5)
            texto = Label(self, "Lo sentimos, completa el pago para finalizar el registro del envío", font=("Arial", 14)).place(width=100, x=200)
            

        