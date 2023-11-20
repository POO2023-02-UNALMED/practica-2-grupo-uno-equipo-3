import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from gestorAplicacion.productos.producto import Producto 
from gestorAplicacion.administracion.sucursal import Sucursal
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


        labelSucursal = Label(self, text="Selecciona la sucursal\n"+ 
                              "en la que te encuentras:", font=("Arial", 10))
        labelSucursal.grid(pady=10, column=0, row=3, columnspan=2)

        todas_las_sucursales = [s.getNombre() for s in Sucursal.getTodasLasSucursales()]
        self.combobox_sucursales = ttk.Combobox(self, values=todas_las_sucursales)
        self.combobox_sucursales.grid(pady=10, column=0, row=4, columnspan=2)

        self.combobox_sucursales.bind("<<ComboboxSelected>>", self.asignar_sucursal)

    def asignar_sucursal(self, event):

        sucursal= self.combobox_sucursales.get()
           

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
                
                if guia is not None:
                    if guia.getPagoPendiente()!=0: #Si aun hay pago pendiente
                        if guia.getSucursalOrigen() == sucursal:
                            if guia.getTipoDePago() == tipoDePago.REMITENTE or guia.getTipoDePago() == tipoDePago.FRACCIONADO:
                               pass
                               #tipo_cliente = remitente
                                #Funcion cambio de frame
                            else: 
                                return messagebox.showinfo("El tipo de pago seleccionado fue contraentrega, el destinatario paga completamente el pedido")
                        else:
                            if guia.getTipoDePago() == tipoDePago.DESTINATARIO or guia.getTipoDePago() == tipoDePago.FRACCIONADO:
                                pass
                                #tipo_cliente = #destinatario
                                #Funcion cambio de frame
                            
                            else:
                                return messagebox.showinfo("El pedido ya está completamente pagado, Diríjase a la pestaña principal para recoger su pedido.")
                    
                    else:
                        return messagebox.showinfo("El pedido ya está completamente pagado, Diríjase a la pestaña principal para recoger su pedido.")

            else:
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")
            
                
        boton = Button(self, text="Verificar", command=verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.grid(row=4, column=0, columnspan=2, pady=5)