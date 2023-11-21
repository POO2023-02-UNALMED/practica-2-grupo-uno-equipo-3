import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from gestorAplicacion.productos.producto import Producto 
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
#from gestorAplicacion.administracion.guia import Guia

class Pagar(Frame): 
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870", highlightthickness=3)
        self.pack(expand=True)
    
        sucursal_prueba = None

        self.Label_Titulo = tk.Label(self, text="Pagar", font=("Arial", 30), fg="#085870")
        self.Label_Titulo.pack(pady=5)

        self.Label_descripcion = tk.Label(self, text="En esta funcionalidad podrás escoger la manera de pagar tu envío")
        self.Label_descripcion.pack(pady=5)


        labelSucursal = Label(self, text="Selecciona la sucursal\n"+ 
                              "en la que te encuentras:", font=("Arial", 10))
        labelSucursal.pack(pady=5)

        todas_las_sucursales = [s.getNombre() for s in Sucursal.getTodasLasSucursales()]
        self.combobox_sucursales = ttk.Combobox(self, values=todas_las_sucursales)
        self.combobox_sucursales.pack(pady=5)
                   
        self.combobox_sucursales.bind("<<ComboboxSelected>>", self.guardar_sucursal) 

        def verificar():
            if entrada.get() == "":
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")
            
            elif entrada.get().isdigit():
                guia = None
            
                for producto in Producto.getTodosLosProductos():
                    if producto.getCodigo() == int(entrada.get()):
                        guia = producto.getGuia()
                        
                        if self.sucursal_seleccionada != None:
                                self.pack_forget()
                                metodos = Metodos(ventana, self.sucursal_seleccionada, guia)
                                metodos.pack()

                        break
            else:
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")

        #####Verificar
        text = Label(self, text="Ingrese el código de su guía", font=("Arial", 12, "bold"))
        text.pack(pady=5)

        entrada= Entry(self)
        entrada.pack(pady=5)

        boton = Button(self, text="Verificar", command=verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(pady=5)    

    def guardar_sucursal(self, event):
            nombresucursal_seleccionada = self.combobox_sucursales.get()
            self.sucursal_seleccionada = None
            
            for sucursal in Sucursal.getTodasLasSucursales():
                   if sucursal.getNombre() == nombresucursal_seleccionada:
                       self.sucursal_seleccionada = sucursal
                       break
                      

class Metodos(Frame):
    def __init__(self, ventana, sucursal_seleccionada, guia):
        super().__init__(ventana)
        sucursal_seleccionada=sucursal_seleccionada
        guia=guia

        self.config(bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.pack(expand=True)

        frame = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        frame.pack(expand=True)

        Label_Titulo = tk.Label(self, text="Método de pago", font=("Arial", 30), fg="#085870")
        Label_Titulo.pack(pady=10)

        Label_descripcion = tk.Label(self, text="Selecciona el método de pago de tu preferencia:")
        Label_descripcion.pack(pady=10)

        boton_tarjeta = tk.Button(self, text="Tarjeta de crédito", command=self.metodo_tarjeta)
        boton_tarjeta.pack(pady=10)

        boton_efectivo = tk.Button(self, text="Efectivo", command=self.metodo_efectivo)
        boton_efectivo.pack(pady=10)
    
    def metodo_tarjeta(self, guia, sucursal_seleccionada):
        Label_Titulo.pack_forget()
        Label_descripcion.pack_forget()
        boton_efectivo.pack_forget()
        boton_tarjeta.pack_forget()

        Label_Titulo = tk.Label(self.frame, text="Pago por tarjeta de crédito", font=("Arial", 30), fg="#085870")
        Label_Titulo.pack(pady=10)

        Label_descripcion = tk.Label(self.frame, text="Ingresa los siguientes datos:")
        Label_descripcion.pack(pady=10)

        nombre_label = tk.Label(self.frame, text="Nombre del titular:")
        nombre_label.pack(pady=5)

        numero_label = tk.Label(self.frame, text="Número:")
        numero_label.pack(pady=10)

        cvv_label = tk.Label(self.frame, text="CVV:")
        cvv_label.pack(pady=10)

        fecha_label = tk.Label(self.frame, text="Fecha de expiración:")
        fecha_label.pack(pady=10)

        nombre_entry = tk.Entry(self.frame)
        nombre_entry.pack(pady=5)
        numero_entry = tk.Entry(self.frame)
        numero_entry.pack(pady=5)
        cvv_entry = tk.Entry(self.frame)
        cvv_entry.pack(padx=5)
        fecha_entry = tk.Entry(self.frame)
        fecha_entry.pack(padx=5)

        cuentaCliente = None
        for cuenta in CuentaBancaria.getTodasLasCuentas():
             if cuenta.getNumero() == numero_entry.get():
                cuentaCliente = cuenta
                break
        
        if cuentaCliente is not None:
            if cuentaCliente.getTitular().getNombre()==nombre_entry.get():
                if cuentaCliente.getCVV() == cvv_entry.get():
                    if cuentaCliente.getFechaExpiracion()== fecha_entry.get():
                        confirmarPago(guia, cuentaCliente, sucursal)
                    else:
                        return messagebox.showwarning("Error", "Datos incorrectos")
                else:
                        return messagebox.showwarning("Error", "Datos incorrectos")
            else:
                        return messagebox.showwarning("Error", "Datos incorrectos")
        else:
                        return messagebox.showwarning("Error", "Esta cuenta no existe")

        def confirmarPago(guia, cuenta_cliente, sucursal):
             
             pass
             

    def metodo_efectivo(self, guia, sucursal):
        guia = guia
        sucursal = sucursal
        precio = 0
        if guia.get_sucursal_origen() == sucursal: ##pago remitente
        
            tipo_pago = guia.get_tipo_pago()
            if tipo_pago == TipoPago.REMITENTE:
                guia.set_pago_pendiente(guia.get_pago_pendiente() * 0)
                precio = guia.get_precio_total()
            elif tipo_pago == TipoPago.FRACCIONADO:
                guia.set_pago_pendiente(guia.get_pago_pendiente() / 2)
                precio = guia.get_precio_total() / 2
        else:
            # Está pagando el destinatario
            tipo_pago = guia.get_tipo_pago()
            if tipo_pago == TipoPago.DESTINATARIO:
                guia.set_pago_pendiente(0)
                precio = guia.get_precio_total()
            elif tipo_pago == TipoPago.FRACCIONADO:
                guia.set_pago_pendiente(0)
                precio = guia.get_precio_total() / 2

        sucursal.agregar_producto(guia.get_producto())
        return messagebox.showwarning("Gracias por usar nuestro servicio, por favor acerquese a la caja numero 4 para cancelar"+str(precio))  


    