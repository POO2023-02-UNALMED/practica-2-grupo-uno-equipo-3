import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import threading
from gestorAplicacion.productos.producto import Producto 
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.transportes.camion import Camion
from gestorAplicacion.administracion.sucursal import Sucursal

class Rastrear(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870",highlightthickness=3)
        self.pack(expand=True)

        def consultarProgreso(guia):
            self.pack_forget()
            estado = Estado(ventana, guia)
            estado.pack()
            
        def verificar():
            if entrada.get() == "":
                return messagebox.showwarning("Error")
            
            elif entrada.get().isdigit():
                guia = None
            
                for producto in Producto.getTodosLosProductos():
                    if producto.getCodigo() == int(entrada.get()):
                        guia = producto.getGuia()
                        consultarProgreso(guia)
                        break
            else:
                return messagebox.showwarning("Error, ingrese un código válido")
            
            if guia != None:
                consultarProgreso
            else:
                return messagebox.showwarning("Lo sentimos, el código de la guía no coincide, intentelo de nuevo")
        
        texto0 = ("Esta funcionalidad permite ver el estado y ubicación actual de su pedido\n" + str(Guia.getTodasLasGuias()[0].getProducto().getCodigo()))
        descripcion = Label(self, text=texto0, font=("Arial", 11), fg="white", bg="#085870")
        descripcion.pack(pady=5, padx=5)
        
        texto = Label(self,text="Ingrese el código de su paquete:", font=("arial", 11, "bold"))
        texto.pack(pady=5)
        
        entrada = Entry(self)
        entrada.pack(pady=5)
        
        boton = Button(self, text="Verificar", command=verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(pady=5)
        
class Estado(Frame):
    def __init__(self, ventana, guiaPaquete):
        super().__init__(ventana)
        self.config(highlightbackground="#085870", highlightthickness=3, width=565, height=100)
        self.pack_propagate(False)
        self.pack(side="top", expand=True)
        
        camion = Sucursal.getTodasLasSucursales()[0].getCamionesEnSucursal()[0]
        camion.iniciarRecorrido()
        enviado = False

        progress_var = tk.IntVar()
        progress_var.set(guiaPaquete.avancePedido())

        avance = Label(self, text="El camión con tu pedido está preparándose para salir \n")
        avance.pack(pady=0, fill="x")

        progress_bar = ttk.Progressbar(self, variable=progress_var, maximum=100, length=500)
        progress_bar.pack(pady=5)

        inicio = Label(self, text=guiaPaquete.getSucursalOrigen().getNombre())
        inicio.pack(side="left", anchor="sw", padx=5, pady=5)

        final = Label(self, text=guiaPaquete.getSucursalLlegada().getNombre())
        final.pack(side="right", anchor="se", padx=5, pady=5)

        porcentaje = Label(self, text="%"+str(guiaPaquete.avancePedido()))
        porcentaje.pack(side="bottom", pady=5)

        # Prevent the frame from adapting to its content
        # Set the specific width for the frame

        

        
        # if guia.getTipoDePago() == Guia.tipoDePago.REMITENTE:
        #     if guia.getPagoPendiente() == 0:
        #         enviado = True
        
        def actualizarBarra():
            print(guiaPaquete.avancePedido())
            for i in range(150):
                print(guiaPaquete.avancePedido())
                x = guiaPaquete.avancePedido()
                time.sleep(1)
                avance.config(text=camion.ubicarTransporte())
                if x != guiaPaquete.avancePedido():
                    porcentaje.config(text="%"+str(guiaPaquete.avancePedido()))
                    progress_var.set(guiaPaquete.avancePedido())
                    avance.config(text=camion.ubicarTransporte())
                
        hilo = threading.Thread(target=actualizarBarra)
        hilo.start()
        # elif guia.getTipoDePago() == Guia.tipoDePago.FRACCIONADO:
        #     if guia.getPagoPendiente() == guia.getPrecioTotal() / 2:
        #         enviado = True
        
        # else:
        #     enviado = True
        
        # if enviado:
        #     frame = Frame(ventana, width=400, height=200,bg="green",highlightbackground="#085870",highlightthickness=5)
        #     texto = Label(self, "Lo sentimos, completa el pago para finalizar el registro del envío", font=("Arial", 14)).place(width=100, x=200)
            

        