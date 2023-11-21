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
    
        self.sucursal_prueba = None

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

        #####Verificar
        text = Label(self, text="Ingrese el código de su guía", font=("Arial", 12, "bold"))
        text.pack(pady=5)

        entrada= Entry(self)
        entrada.pack(pady=5)

        def verificar():
            if entrada.get() == "":
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")
            
            elif entrada.get().isdigit():
                guia = None
            
                for producto in Producto.getTodosLosProductos():
                    if producto.getCodigo() == int(entrada.get()):
                        guia = producto.getGuia()
                        
                        if self.sucursal_prueba != None:
                                self.pack_forget()
                                metodos = Metodos(ventana, self.sucursal_prueba, guia)
                                metodos.pack()

                        break
            else:
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")

        boton = Button(self, text="Verificar", command=verificar,bg="#085870",font=("arial", 11, "bold"),fg="#cedae0")
        boton.pack(pady=5)

    def guardar_sucursal(self, event):
            nombresucursal_seleccionada = self.combobox_sucursales.get()
            sucursal_seleccionada = None
            for sucursal in Sucursal.getTodasLasSucursales():
                if sucursal.getNombre() == nombresucursal_seleccionada:
                    sucursal_seleccionada = sucursal
                    self.sucursal_prueba = sucursal_seleccionada
                    break        

class Metodos(Frame):
    def __init__(self, ventana, sucursal_seleccionada, guia):
        super().__init__(ventana)
        sucursal_seleccionada=sucursal_seleccionada
        guia=guia

        self.config(bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.pack(expand=True)

        self.frame = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        self.frame.pack(expand=True)

        self.Label_Titulo = tk.Label(self, text="Método de pago", font=("Arial", 30), fg="#085870")
        self.Label_Titulo.pack(pady=10)

        self.Label_descripcion = tk.Label(self, text="Selecciona el método de pago de tu preferencia:")
        self.Label_descripcion.pack(pady=10)

        self.boton_tarjeta = tk.Button(self, text="Tarjeta de crédito", command=self.metodo_tarjeta)
        self.boton_tarjeta.pack(pady=10)

        self.boton_efectivo = tk.Button(self, text="Efectivo", command=self.metodo_efectivo)
        self.boton_efectivo.pack(pady=10)
    
    def metodo_tarjeta(self, guia, sucursal_seleccionada):
        self.Label_Titulo.pack_forget()
        self.Label_descripcion.pack_forget()
        self.boton_efectivo.pack_forget()
        self.boton_tarjeta.pack_forget()

        self.Label_Titulo = tk.Label(self.frame, text="Pago por tarjeta de crédito", font=("Arial", 30), fg="#085870")
        self.Label_Titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.Label_descripcion = tk.Label(self.frame, text="Ingresa los siguientes datos:")
        self.Label_descripcion.grid(row=1, column=0, columnspan=2, pady=10)

        nombre_label = tk.Label(self.frame, text="Nombre del titular:")
        nombre_label.grid(row=2, column=0, pady=(10, 0), sticky="e")

        numero_label = tk.Label(self.frame, text="Número:")
        numero_label.grid(row=3, column=0, pady=10, sticky="e")

        cvv_label = tk.Label(self.frame, text="CVV:")
        cvv_label.grid(row=4, column=0, pady=10, sticky="e")

        fecha_label = tk.Label(self.frame, text="Fecha de expiración:")
        fecha_label.grid(row=5, column=0, pady=10, sticky="e")

        nombre_entry = tk.Entry(self.frame)
        nombre_entry.grid(row=2, column=1, pady=(10, 0), padx=5, sticky="w")
        numero_entry = tk.Entry(self.frame)
        numero_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w")
        cvv_entry = tk.Entry(self.frame)
        cvv_entry.grid(row=4, column=1, pady=5, padx=5, sticky="w")
        fecha_entry = tk.Entry(self.frame)
        fecha_entry.grid(row=5, column=1, pady=5, padx=5, sticky="w")

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



        def confirmarPago(self):
            pass
    def metodo_efectivo(self):
        pass


    