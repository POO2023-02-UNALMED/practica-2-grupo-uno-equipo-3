import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import time
import threading
from gestorAplicacion.productos.producto import Producto 
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.transportes.camion import Camion
from gestorAplicacion.transportes.avion import Avion
from gestorAplicacion.administracion.sucursal import Sucursal

class Rastrear(Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.pack(expand=True)

        def consultarProgreso(guia):
            self.pack_forget()
            estado = Estado(ventana, guia)
            estado.pack()
            
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
            
            if guia != None:
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
                    consultarProgreso(guia)
                    
                else:
                    return messagebox.showwarning("Error", "Lo sentimos, completa el pago para finalizar el registro del envío")
                    
            else:
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Lo sentimos, el código de la guía no coincide, intentelo de nuevo")
                
        titulo = tk.Label(self, text="Rastrear Pedido", font=("Arial", 30), bg="#739072", foreground="white")
        titulo.pack(pady=5)
        
        #texto0 = ("Esta funcionalidad permite ver el estado y ubicación actual de su pedido\n" + "Codigo de prueba:" + str(Guia.getTodasLasGuias()[0].getProducto().getCodigo()) + "\nCaso de prueba avion: " +  str(Guia.getTodasLasGuias()[2].getProducto().getCodigo()))

        texto0 = ("Esta funcionalidad permite ver el estado y ubicación actual de su pedido\n")
        descripcion = Label(self, text=texto0, font=("Arial", 11), bg="#739072", fg="white")
        descripcion.pack(pady=5, padx=5)
        
        texto = Label(self,text="Ingrese el código de su paquete:", font=("arial", 11, "bold"), bg="#739072", fg="white")
        texto.pack(pady=5)
        
        entrada = Entry(self)
        entrada.pack(pady=5)
        
        boton = Button(self, text="Verificar", command=verificar,bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton.pack(pady=5)
        
class Estado(Frame):
    hilos = False
    def __init__(self, ventana, guiaPaquete):
        super().__init__(ventana)
        self.config(bg="#739072", highlightbackground="#3A4D39", highlightthickness=3, width=570, height=135)
        self.pack_propagate(False)
        self.pack(side="top", expand=True)
        Estado.hilos = True
                
        transporte = guiaPaquete.getVehiculo()

        progress_var = tk.IntVar()
        progress_var.set(guiaPaquete.avancePedido())
        guiaPaquete.avancePedido()

        def actualizarBarra():
            for i in range(150):
                if Estado.hilos:
                    if guiaPaquete.getEstado() == Guia.estado.ENSUCURSALORIGEN:
                        if type(guiaPaquete.getVehiculo()) is Camion:
                            mensaje = "El Camión con su pedido está preparándose para salir \n"
                        elif type(guiaPaquete.getVehiculo()) is Avion:
                            mensaje = "El Avión con su pedido está preparándose para salir \n"                            
                        avance.config(text=mensaje)
                        progress_var.set(0)
                        break
                    
                    elif guiaPaquete.getEstado() == Guia.estado.ENTRANSITO:
                        progress_var.set(guiaPaquete.avancePedido())
                        avance.config(text=transporte.ubicarTransporte())
                        porcentaje.config(text="%"+str(guiaPaquete.avancePedido()))
                        
                    elif guiaPaquete.getEstado() == Guia.estado.ENESPERA:
                        mensaje = "El producto ya llegó a la sucursal de destino.\n" \
                            "Diríjase a la pestaña recoger para reclamar su pedido"
                        progress_var.set(100)
                        avance.config(text=mensaje)
                        porcentaje.config(text="%100")
                        break
                    
                    elif guiaPaquete.getEstado() == Guia.estado.ENTREGADO:
                        mensaje = "El pedido ya ha sido reclamado\n"
                        progress_var.set(100)
                        avance.config(text=mensaje)
                        porcentaje.config(text="%100")
                        break
                    time.sleep(1)
                else:
                    break
            
        avance = Label(self, text="\n", bg="#739072", fg="white")
        avance.pack(pady=0, fill="x")
        
        frameCodigo = Frame(self, bg="#739072")
        frameCodigo.pack(side="bottom", pady=5)
        
        codigoTexto = Label(frameCodigo, text="Código: ", bg="#739072", fg="white")
        codigoTexto.pack(side="left")
        
        codigo = Entry(frameCodigo)
        codigo.insert(0, guiaPaquete.getProducto().getCodigo())
        codigo.config(state="readonly")
        codigo.pack(side="left")

        progress_bar = ttk.Progressbar(self, variable=progress_var, maximum=100, length=500)
        progress_bar.pack(pady=5)
        
        inicio = Label(self, text=guiaPaquete.getSucursalOrigen().getNombre(), bg="#739072", fg="white")
        inicio.pack(side="left", anchor="sw", padx=5, pady=5)

        final = Label(self, text=guiaPaquete.getSucursalLlegada().getNombre(), bg="#739072", fg="white")
        final.pack(side="right", anchor="se", padx=5, pady=5)

        porcentaje = Label(self, text="%"+str(guiaPaquete.avancePedido()), bg="#739072", fg="white")
        porcentaje.pack(side="bottom", pady=5)

        
        
        hilo = threading.Thread(target=actualizarBarra)
        hilo.start()
        

    def detenerHilos():
        Estado.hilos = False

            

        