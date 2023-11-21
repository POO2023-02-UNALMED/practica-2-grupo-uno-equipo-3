import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from gestorAplicacion.productos.producto import Producto 
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
from gestorAplicacion.administracion.guia import Guia

class Pagar(Frame): 
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.pack(expand=True)

        sucursal_prueba = None

        self.Label_Titulo = tk.Label(self, text="Pagar", font=("Arial", 30), bg="#739072", foreground="white")
        self.Label_Titulo.pack(pady=5)

        self.Label_descripcion = tk.Label(self, text="En esta funcionalidad podrás escoger la manera de pagar tu envío", font=("arial", 11), bg="#739072", fg="white")
        self.Label_descripcion.pack(pady=5)


        labelSucursal = Label(self, text="Selecciona la sucursal\n"+ 
                              "en la que te encuentras:", font=("arial", 11), bg="#739072", fg="white")
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
                            if guia.getPagoPendiente() != 0:
                                if guia.getTipoDePago() == Guia.tipoDePago.DESTINATARIO and self.sucursal_seleccionada == guia.getSucursalOrigen():
                                    self.pack_forget()
                                    pagar = Pagar(ventana)
                                    pagar.pack()
                                    messagebox.showinfo("Paga Destinatario", "El pago del envío lo realiza el destinatario")
                                else :
                                    self.pack_forget()
                                    metodos = Metodos(ventana, self.sucursal_seleccionada, guia)
                                    metodos.pack()
                            else:
                                self.pack_forget()
                                pagar = Pagar(ventana)
                                pagar.pack()
                                messagebox.showinfo("Pago completado", "El envío ha sido completamente pagado")

                        break
            else:
                entrada.delete(0, END)
                return messagebox.showwarning("Error", "Ingrese un código válido")

        #####Verificar
        text = Label(self, text="Ingrese el código de su guía", font=("arial", 11, "bold"), bg="#739072", fg="white")
        text.pack(pady=5)

        entrada= Entry(self)
        entrada.pack(pady=5)

        boton = Button(self, text="Verificar", command=verificar,bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton.pack(pady=5)    

    def guardar_sucursal(self, event):
            nombresucursal_seleccionada = self.combobox_sucursales.get()
            self.sucursal_seleccionada = None
            
            for sucursal in Sucursal.getTodasLasSucursales():
                   if sucursal.getNombre() == nombresucursal_seleccionada:
                       self.sucursal_seleccionada = sucursal
                       break
                      
class Metodos(tk.Frame):
    def __init__(self, ventana, sucursal_seleccionada, guia):
        super().__init__(ventana)
        self.config(bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.pack(expand=True)

        def metodoTarjeta(guia, sucursal):
            self.pack_forget()
            tarjeta = Tarjeta(ventana, guia, sucursal)
            tarjeta.pack()
                
        def metodoEfectivo(guia, sucursal):
            
            paq = guia.getProducto()

            #mensaje de confirmacion
            confirmacion = messagebox.askokcancel("Confirmación", f"¿Está seguro de pagar el producto con código: {paq.getCodigo()}?")

            #se obtiene la guia del paquete
            guiaPaq = guia
   
            #Lógica para poder reclamar el paquete
            if confirmacion:
                if paq:
                    if guiaPaq:
                        #paga el remitente
                        if guiaPaq.getSucursalOrigen() == sucursal: 
                            pago = guiaPaq.getTipoDePago()
                            if pago == Guia.tipoDePago.REMITENTE:
                                guiaPaq.setPagoPendiente(int(guiaPaq.getPagoPendiente()) * 0)
                                precio = guiaPaq.getPrecioTotal()
                                sucursal.getInventario().append(guiaPaq)
                                
                            if pago == Guia.tipoDePago.FRACCIONADO:
                                guiaPaq.setPagoPendiente(int(guiaPaq.getPagoPendiente()) / 2)
                                precio = int(guiaPaq.getPrecioTotal()) / 2
                                sucursal.getInventario().append(guiaPaq)

                        else:
                        # Está pagando el destinatario
                            pago = guiaPaq.getTipoDePago()
                            if pago == Guia.tipoDePago.DESTINATARIO:
                                guiaPaq.setPagoPendiente(int(guiaPaq.getPagoPendiente()) / 2)
                                precio = int(guiaPaq.getPrecioTotal()) / 2

                            if pago == Guia.tipoDePago.FRACCIONADO:
                                guiaPaq.setPagoPendiente(0)
                                precio = int(guiaPaq.getPrecioTotal()) / 2


                #sucursal.agregar_producto(guia.get_producto())
            messagebox.showinfo("Pago realizado con éxito", f"Gracias por confiar en nosotros, por favor acerquese a la caja numero 4 para cancelar un total de $ {str(precio)}")

        Label_Titulo = tk.Label(self, text="Método de pago", font=("Arial", 30), bg="#739072", foreground="white")
        Label_Titulo.pack(pady=10)

        Label_descripcion = tk.Label(self, text="Selecciona el método de pago de tu preferencia:", font=("Arial", 11),bg="#739072", fg="white")
        Label_descripcion.pack(pady=10)

        frame = Frame(self, bg="#739072")
        frame.pack(padx=20, pady=5)
        
        boton_tarjeta = tk.Button(frame, text="Tarjeta de crédito", command=lambda: metodoTarjeta(guia, sucursal_seleccionada), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_tarjeta.pack(side="left", padx=20, pady=5)

        boton_efectivo = tk.Button(frame, text="Efectivo", command=lambda: metodoEfectivo(guia, sucursal_seleccionada), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_efectivo.pack(side="left", padx=20, pady=5)
        
class Tarjeta(Frame):
    def __init__(self, ventana, guia, sucursal):
        super().__init__(ventana)
        self.config(bg="#739072", highlightbackground="#3A4D39", highlightthickness=3)
        self.pack(expand=True)
        
        descripcion = tk.Label(self, text="Ingresa los siguientes datos:", font=("Arial", 11), bg="#739072", fg="white")
        descripcion.pack(pady=5)
        
        frame = Frame(self, bg="#739072")
        frame.pack(padx=20, pady=5)
        
        nombre = Label(frame, text="Nombre del Titular: ", font=("Arial", 11),bg="#739072", fg="white")
        nombre.grid(row=1, column=1)
        
        nombreEntrada = Entry(frame)
        nombreEntrada.grid(row=1, column=2)
        
        numero = Label(frame, text="Número: ", font=("Arial", 11),bg="#739072", fg="white")
        numero.grid(row=2, column=1)
        
        numeroEntrada = Entry(frame)
        numeroEntrada.grid(row=2, column=2)
        
        cvv = Label(frame, text="CVV: ", font=("Arial", 11),bg="#739072", fg="white")
        cvv.grid(row=3, column=1)
        
        cvvEntrada = Entry(frame)
        cvvEntrada.grid(row=3, column=2)
        
        fecha = Label(frame, text="Fecha de Expiración: ", font=("Arial", 11),bg="#739072", fg="white")
        fecha.grid(row=4, column=1)
        
        fechaEntrada = Entry(frame)
        fechaEntrada.grid(row=4, column=2)
        

        def verificar():
            cuentaCliente = None
            print(1)
            for cuenta in CuentaBancaria.get_todas_las_cuentas():
                if cuenta.get_numero() == int(numeroEntrada.get()):
                    cuentaCliente = cuenta
                    break
                
            if cuentaCliente != None:
                if cuentaCliente.get_titular().getNombre() == str(nombreEntrada.get()):
                    if cuentaCliente.get_numero() == int(numeroEntrada.get()):
                        if cuentaCliente.get_cvv() == int(cvvEntrada.get()):
                            if cuentaCliente.get_fecha_expiracion() == str(fechaEntrada.get()):
                                self.pack_forget()
                                confirmar = ConfirmarPago(ventana, guia, cuentaCliente, sucursal)
                                confirmar.pack()
                            else:
                                datosIncorrectos()
                        else:
                            datosIncorrectos()
                    else:
                            datosIncorrectos()
                else:
                    datosIncorrectos()
            else:
                cuentaNoExiste()
                
        boton = Button(self, text="Validar Datos", command=verificar,bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton.pack(pady=5)
         
        def datosIncorrectos():
            self.pack_forget()
            tarjeta = Tarjeta(ventana, guia, sucursal)
            tarjeta.pack()
            return messagebox.showwarning("Error", "Datos incorrectos, intente nuevamente")
        
        def cuentaNoExiste():
            self.pack_forget()
            tarjeta = Tarjeta(ventana, guia, sucursal)
            tarjeta.pack()
            return messagebox.showwarning("Error", "Lo sentimos, esta cuenta no existe, intentelo de nuevo")
        
class ConfirmarPago(Frame):
    def __init__(self, ventana, guia, cuentaCliente, sucursal):
        super().__init__(ventana)
        self.config(bg="#739072", highlightbackground="#3A4D39", highlightthickness=3)
        self.pack(expand=True)
        
        precio = guia.getPrecioTotal()
        
        if guia.getTipoDePago() == Guia.tipoDePago.FRACCIONADO:
            precio = precio / 2
        
        
        texto = Label(self, text="¿Desea confirmar el pago por $" + str(precio) + "?", font=("Arial", 11),bg="#739072", fg="white") 
        texto.pack(pady=5)
        
        frame = Frame(self, bg="#739072")
        frame.pack()
        
        
        def opcionSi():
            if guia.getSucursalOrigen() == sucursal:
                if guia.getTipoDePago() == Guia.tipoDePago.REMITENTE:
                    if cuentaCliente.descontar_saldo(guia.getPagoPendiente()):
                        guia.setPagoPendiente(0)
                        cuentaCliente.get_titular().subirReputacion()
                        sucursal.agregarProducto(guia.getProducto())
                        
                        self.pack_forget()
                        pagar = Pagar(ventana)
                        pagar.pack()
                        
                        return messagebox.showinfo("Pago realizado", "¡¡Transacción exitosa!!\n" + "Muchas gracias por usar nuestro servicio,\n favor acerquese a la caja #3 para despachar el pedido")
                    
                    else:
                        self.pack_forget()
                        pagar = Pagar(ventana)
                        pagar.pack()
                        
                        return messagebox.showinfo("Fondos Insuficientes", "Lo sentimos, no hay suficiente dinero en la cuenta")
                    
                elif guia.getTipoDePago() == Guia.tipoDePago.FRACCIONADO:
                    if cuentaCliente.descontar_saldo(guia.getPagoPendiente() / 2):
                        guia.setPagoPendiente(guia.getPagoPendiente() / 2)
                        cuentaCliente.get_titular().subirReputacion()
                        sucursal.agregarProducto(guia.getProducto())
                        
                        self.pack_forget()
                        pagar = Pagar(ventana)
                        pagar.pack()
                        
                        return messagebox.showinfo("Pago Realizado", "¡¡Transacción exitosa!!\n" + "Muchas gracias por usar nuestro servicio,\n favor acerquese a la caja #3 para despachar el pedido\n"+"Recuerda que el destinatario debe pagar un total de $" + str(guia.getPrecioTotal()/2))
                
                elif guia.getTipoDePago() == Guia.tipoDePago.DESTINATARIO:
                    self.pack_forget()
                    pagar = Pagar(ventana)
                    pagar.pack()

                    return messagebox.showinfo("", "El destinatario realiza el pago del pedido")
                
            else:
                if guia.getTipoDePago() == Guia.tipoDePago.DESTINATARIO or guia.getTipoDePago() == Guia.tipoDePago.FRACCIONADO:
                    if cuentaCliente.descontar_saldo(guia.getPagoPendiente()):
                        guia.setPagoPendiente(0)
                        cuentaCliente.get_titular().subirReputacion()
                        
                        self.pack_forget()
                        pagar = Pagar(ventana)
                        pagar.pack()
                        
                        return messagebox.showinfo("", "¡¡Transacción exitosa!!\n" + "Muchas gracias por usar nuestro servicio,\n favor acerquese a la caja #3 para despachar el pedido")
                        
        def opcionNo():
            self.pack_forget()
            pagar = Pagar(ventana)
            pagar.pack()
            
            return messagebox.showinfo("", "Servicio cancelado, vuelve pronto")
        
            
        si = Button(frame, text="Sí",command=opcionSi,bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        si.pack(side="left", padx=20, pady=5)
        
        no = Button(frame, text="No",command=opcionNo,bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        no.pack(side="left", padx=20, pady=5)
        
        
    
                        
                
            


                        
                
                
        

    
    
        
             

    

    