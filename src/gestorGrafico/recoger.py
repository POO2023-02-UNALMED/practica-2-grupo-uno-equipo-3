from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#from typing import Self
from gestorAplicacion.administracion import guia
from gestorAplicacion.productos import producto
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.administracion.sucursal import Sucursal
from excepeciones.ErrorAplicacion import ErrorAplicacion
from excepeciones.ExcepEntrys import * 
from excepeciones.ExcepObj import *

#Creación de la clase Recoger que hereda de Frame
class Recoger(tk.Frame):
    def __init__(self, ventana):
        #se inicializa la ventana llamando al super
        super().__init__(ventana)
        self.config(bg="#739072", highlightbackground="#3A4D39", highlightthickness=3,)
        self.pack(expand=True)

        #Label de titulo, descripción y seleccion de sucursal, con sus respectivas configuraciones
        self.Label_Titulo = tk.Label(self, text="Reclamar Paquete", font=("Arial", 30), bg="#739072", fg="white")
        self.Label_Titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.Label_descripcion = tk.Label(self, text="¡Hola querido cliente! En este apartado podrá reclamar los paquetes que se hayan enviado\n"+ "a su nombre solo, deberá ingresar la información necesaria para reclamar dicho paquete", font=("Arial", 11), bg="#739072", fg="white")
        self.Label_descripcion.grid(row=1, column=0, columnspan=2, pady=10)

        self.Label_sele_suc = tk.Label(self, text="Primero necesitamos saber en qué sucursal se encuentra,\n"+ 
                                       "para ello por favor seleccione una de las opciones", font=("Arial", 11), bg="#739072", fg="white")
        self.Label_sele_suc.grid(row=2, column=0, columnspan=2, pady=10)


        #Selección sucursal y combobox
        labelSucursal = Label(self, text="Selecciona la sucursal\n"+ 
                              "en la que te encuentras:", font=("Arial", 11), bg="#739072", fg="white")
        labelSucursal.grid(pady=10, column=0, row=3, columnspan=2)

        todas_las_sucursales = [s.getNombre() for s in Sucursal.getTodasLasSucursales()]
        self.combobox_sucursales = ttk.Combobox(self, values=todas_las_sucursales)
        self.combobox_sucursales.grid(pady=10, column=0, row=4, columnspan=2)

        self.combobox_sucursales.bind("<<ComboboxSelected>>", self.cambiar_frame_sucursal)


    #función para cambiar de frame dependiendo de la sucursal seleccionada
    def cambiar_frame_sucursal(self, event):
        nombresucursal_seleccionada = self.combobox_sucursales.get()
        sucursal_seleccionada = None
        for sucursal in Sucursal.getTodasLasSucursales():
            if sucursal.getNombre() == nombresucursal_seleccionada:
                sucursal_seleccionada = sucursal
                break
        if sucursal_seleccionada:
            #se llama la clase FrameSucursal
            frame_sucursal = FrameSucursal(self.master, sucursal_seleccionada,nombresucursal_seleccionada)
            self.pack_forget()  
            frame_sucursal.pack()

#Acá se obtiene el nuevo frame dependiendo de la sucursal seleccionada
class FrameSucursal(tk.Frame):
    def __init__(self, ventana, sucursal_seleccionada, nombresucursalSeleccionada):
        #configuración para la ventana
        super().__init__(ventana)
        self.nombresucursalSeleccionada = nombresucursalSeleccionada
        self.sucursal_seleccionada = sucursal_seleccionada
        self.config(bg="#739072", highlightbackground="#3A4D39", highlightthickness=3,)
        self.pack(expand=True)

        etiqueta = tk.Label(self, text=f"Ha seleccionado la sucursal: {nombresucursalSeleccionada}", font=("arial", 20), bg="#739072", fg="white")
        etiqueta.pack(pady=5)

        self.entryCod = Entry(self)
        self.entryName = Entry(self)
        self.entryCC = Entry(self)

        labelCod = Label(self, text="Código del Paquete", font=("Arial", 11), bg="#739072", fg="white")
        labelCod.pack(padx=10, pady=8)
        self.entryCod.pack(padx=10, pady=5)

        labelName = Label(self, text="Nombre de quien reclama", font=("Arial", 11),bg="#739072", fg="white")
        labelName.pack(padx=10, pady=8)
        self.entryName.pack(padx=10, pady=5)

        labelCC = Label(self, text="Cédula de quien reclama", font=("Arial", 11), bg="#739072", fg="white")
        labelCC.pack(padx=10, pady=8)
        self.entryCC.pack(padx=10, pady=5)

        botonReclamar = Button(self, text="Reclamar Paquete", command=self.reclamar,bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        botonReclamar.pack(padx=10, pady=5)

    #funcionalidad de reclamar
    def reclamar(self):
        try:
            #se obtienen los valores de los entry
            Cod = int(self.entryCod.get())

            #se llama a la funcion con el entry anterior
            paq = self.encontrarProductoPorCodigo(Cod)

            #mensaje de confirmacion
            confirmacion = messagebox.askokcancel("Confirmación", f"¿Está seguro de reclamar el paquete {Cod}?")

            #verificar ciudad de destino
            ciudadSiNo = self.verificarCiudadDestino(paq,self.nombresucursalSeleccionada)

            #se obtiene la guia del paquete
            guiaPaq = paq.getGuia()

            #Lógica para poder reclamar el paquete
            if confirmacion:
                if paq:
                    if guiaPaq:
                        #se verifican los datos del destinatario
                        if self.verificarDatos(paq, int(self.entryCC.get())):
                            if ciudadSiNo:
                                #se verifica si el paquete se encuentra en el inventario de la sucursal seleccionada
                                if (paq in self.sucursal_seleccionada.getInventario()):
                                    #se verifica que el paquete no haya sido entregado aún
                                    if (guiaPaq.getEstado() != guia.Guia.estado.ENTREGADO):
                                        #se verifica el tipo de pago y si hay o no saldo pendiente
                                        if (guiaPaq.getTipoDePago() == guia.Guia.tipoDePago.REMITENTE):
                                            if (guiaPaq.getPagoPendiente() == 0):
                                                messagebox.showinfo("Operación realizada con éxito", "Puedes reclamar tu paquete")
                                                #HAY QUE ELIMINAR EL PAQUETE DEL INVENTARIO DE LA SUCURSAL 
                                                self.destroy()
                                                if (guiaPaq.getPagoPendiente() != 0):
                                                    messagebox.showinfo("Falta pago", "Para poder reclamar tu paquete debes pagar la mitad del envío")
                                        elif (guiaPaq.getTipoDePago() == guia.Guia.tipoDePago.FRACCIONADO):
                                            if (guiaPaq.getPagoPendiente() == 0):
                                                messagebox.showinfo("Operación realizada con éxito", "Puedes reclamar tu paquete")
                                                self.destroy()
                                            if (guiaPaq.getPagoPendiente() != 0):
                                                messagebox.showinfo("Falta pago", "Para poder reclamar tu paquete debes pagar la mitad del envío")
                                        elif (guiaPaq.getTipoDePago() == guia.Guia.tipoDePago.DESTINATARIO):
                                            if (guiaPaq.getPagoPendiente() == 0):
                                                messagebox.showinfo("Operación realizada con éxito", "Puedes reclamar tu paquete")
                                                self.destroy()
                                            if (guiaPaq.getPagoPendiente() != 0):
                                                messagebox.showinfo("Falta pago", "Para poder reclamar tu paquete debes pagar el total por el envío")
                                    else:
                                        messagebox.showinfo("Paquete no encontrado", "Tu paquete ya ha sido reclamado")
                                else:
                                    messagebox.showinfo("No ha llegado", "El paquete no está disponible para ser recogido")
                            else:
                                messagebox.showinfo("Sucursal errónea", "El paquete no tiene como destino la sucursal en la que te encuentras")
                        else:
                            messagebox.showinfo("Datos incorrectos", "Los datos que proporcionó no coinciden con los del remitente")
                    else:
                        messagebox.showinfo("Paquete no encontrado", f"No se encontró ningún paquete con el código {Cod}")
                else:
                    self.destroy()
        except:
            messagebox.showerror("Error", CampoVacio().mostrarMensaje())

    #función que se encarga de verificar si la ciudad seleccionada es la misma que la ciudad destino accediendo a la guia del producto
    def verificarCiudadDestino(self, paq, posibleCiudad):
        guia = paq.getGuia()
        sucursalDestino = guia.getSucursalLlegada().getNombre()
        print("verificar ciudad (sucursalDestino)",sucursalDestino)
        print("posible ciudad(escogida)",posibleCiudad)
        return sucursalDestino == posibleCiudad
    
    #función que se encarga de verificar los datos ingresados en los entrys, compara la cc ingresada con la cc de la guia del producto
    def verificarDatos(self, paq, Cedula):
        guia = paq.getGuia()
        destinatario = guia.getDestinatario()
        
        return int(destinatario.getCedula()) == int(Cedula)

    #Función que se encargar de encontrar el producto con el código digitado en el entry
    def encontrarProductoPorCodigo(self, cod):
        for i in producto.Producto.getTodosLosProductos():
            if int(i.getCodigo()) == int(cod):
                return i
        return None



# from tkinter import *
# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from gestorAplicacion.administracion import guia
# from gestorAplicacion.productos import producto
# from gestorGrafico.FieldFrame import FieldFrame
# from gestorAplicacion.administracion.opinion import Opinion
# from gestorAplicacion.administracion.sucursal import Sucursal
# from excepeciones.ErrorAplicacion import ErrorAplicacion
# from excepeciones.ExcepEntrys import * 
# from excepeciones.ExcepObj import *

# class Recoger(tk.Frame):
#     def __init__(self, ventana):
#         super().__init__(ventana)
#         self.config(highlightbackground="#085870", highlightthickness=3)
#         self.pack(expand=True)
  

#         self.Label_Titulo = tk.Label(self, text="Reclamar Paquete", font=("Arial", 30))
#         self.Label_Titulo.grid(row=0,column=0,columnspan=2,pady=10)

#         self.Label_descripcion = tk.Label(self,text="¡Hola querido cliente! En este apartado podrá reclamarlos paquetes que se hayan enviado\n"+ "a su nombre solo, deberá ingresar la información necesaria para reclamar dicho paquete")
#         self.Label_descripcion.grid(row=1, column=0, columnspan=2, pady=10)

#         self.Label_sele_suc = tk.Label(self,text="Primero necesitamos saber en qué sucursal se encuentra,\n"+ 
#                                        "para ello por favor seleccione una de las opciones")
#         self.Label_sele_suc.grid(row=2,column=0,columnspan=2,pady=10)
#         #Sucursal a elegir 
#         labelSucursal = Label(self,text="Selecciona la sucursal\n"+ 
#                               "en la que te encuentras:", font=("Arial",10))
#         labelSucursal.grid(pady=10,column=0,row=3,columnspan=2)

#         # Crear el Combobox para seleccionar sucursales
#         todas_las_sucursales = [s.getNombre() for s in Sucursal.getTodasLasSucursales()]
#         self.combobox_sucursales = ttk.Combobox(self, values=todas_las_sucursales)
#         self.combobox_sucursales.grid(pady=10,column=0,row=4,columnspan=2)

#         # Configurar evento para cambio en el ComboBox
#         self.combobox_sucursales.bind("<<ComboboxSelected>>", self.cambiar_frame_sucursal)


#     def cambiar_frame_sucursal(self, event):
#         # Obtener la sucursal seleccionada
#         sucursal_seleccionada = self.combobox_sucursales.get()

#         # Cambiar a otro frame y pasar la sucursal seleccionada
#         frame_sucursal = FrameSucursal(self.master, sucursal_seleccionada)
#         self.pack_forget()  
#         frame_sucursal.pack()


# class FrameSucursal(tk.Frame):
#     def __init__(self, ventana, sucursal_seleccionada):
#         super().__init__(ventana)
#         self.sucursal_seleccionada = sucursal_seleccionada
#         self.config(bg="#085870")
#         self.pack(fill="both",expand=True)

#          # Crear contenido para el nuevo frame
#         etiqueta = tk.Label(self, text=f"Ha seleccionado la sucursal: {self.sucursal_seleccionada}",font=("arial",20))
#         etiqueta.pack(pady=40)

#         def reclamar():

            
#             try:
#                 Name = str(self.entryName.get())
#                 Cedula = int(self.entryCC.get())
#                 Cod = int(self.entryCod.get())


#                 paq = self.encontrarProductoPorCodigo(Cod)
#                 confirmacion = messagebox.askokcancel("Confirmación", f"¿Está seguro de reclamar el paquete {Cod}?")

#                 if confirmacion:
#                     if paq:
#                        #CAMBIAR GUIA
#                        guiaPaq = paq.getGuia()
#                     if self.verificarDatos(paq,Cedula):
#                         if guiaPaq.getSucursalLlegada() == self.sucursal_seleccionada:
#                             if paq in self.sucursal_seleccionada.getInventario():
#                                 if guiaPaq.getEstado() != guia.estado.ENTREGADO:
#                                 #quiero que salga un nuevo frame con una imagen con un paquete y el texto de poder recoger el paquete
#                                     if guiaPaq.getTipoDePago() == guia.tipoDePago.REMITENTE:
#                                         if guiaPaq._pagoPendiente() == 0:
#                                             messagebox.showinfo("Operación realizada con éxito","Puedes reclamar tu paquete")
#                                             self.destroy()

#                                     if guiaPaq.getTipoDePago() == guia.tipoDePago.DESTINATARIO:
#                                         if guia._pagoPendiente() != 0:
#                                             messagebox.showinfo("Falta pago","Para poder reclamar tu paquete debes pagar el total por el envío")

#                                     if guiaPaq.getTipoDePago() == guia.tipoDePago.FRACCIONADO:
#                                         if guiaPaq._pagoPendiente() != 0:
#                                             messagebox.showinfo("Falta pago","Para poder reclamar tu paquete debes pagar la mitad del envío")

#                                 if guiaPaq.getEstado() == guia.estado.ENTREGADO:
#                                     messagebox.showinfo("Paquete no encontrado", "Tu paquete ya ha sido reclamado")
                                
#                                 if guiaPaq.getEstado() == guia.estado.ENSUCURSALORIGEN:
#                                     messagebox.showinfo("El paquete no ha salido", "El paquete se encuentra en la sucursal de origen")

#                                 if guiaPaq.getEstado() == guia.estado.ENESPERA:
#                                     messagebox.showinfo("En espera", "El paquete se encuentra en espera")

#                             if paq not in self.sucursal_seleccionada.getInventario():
#                                 if guiaPaq.getSucursalLlegada() == self.sucursal_seleccionada and (guiaPaq.getEstado() == guia.Estado.ENTRANSITO):
#                                     messagebox.showinfo("No ha llegado","El paquete no está disponible para ser recogido")

#                         if guiaPaq.getSucursalLlegada() != self.sucursal_seleccionada:
#                                     messagebox.showinfo("Sucursal errónea", "El paquete no tiene como destino la sucursal en la que te encuentras")
#                     else: 
#                         messagebox.showinfo("Datos incorrectos", "Los datos que proporcionó no coindicen con los que digitó el remitente")  

#                 else:
#                     self.destroy()              
#             except:
#                 messagebox.showerror("Error", CampoInvalido().mostrarMensaje())



#         titulo = Label(self, text="Reclamar Paquete", font=("arial", 25), fg="white", bg="#085870")
#         titulo.pack(side="top", anchor="c")

#         texto = ("A continuación, deberá ingresar la información necesaria para reclamar\n"
#                  "el paquete que está asociado a usted.")
#         descripcion = Label(self, text=texto, font=("arial", 11), fg="white", bg="#085870")
#         descripcion.pack(anchor="n", pady=20)

#         sFrame = Frame(self, bg="#cedae0")
#         sFrame.pack()

#         labelCod = Label(sFrame, text="Código del Paquete", font=("arial", 11), fg="white", bg="#085870")
#         labelCod.grid(row=1, column=0, padx=10, pady=8)
#         self.entryCod = Entry(sFrame)
#         self.entryCod.grid(row=1, column=1, padx=10, pady=8)

#         labelName = Label(sFrame, text="Nombre de quien reclama", font=("arial", 11), fg="white", bg="#085870")
#         labelName.grid(row=2, column=0, padx=10, pady=8)
#         self.entryName = Entry(sFrame)
#         self.entryName.grid(row=2, column=1, padx=10, pady=8)

#         labelCC = Label(sFrame, text="Cédula de quien reclama", font=("arial", 11), fg="white", bg="#085870")
#         labelCC.grid(row=3, column=0, padx=10, pady=8)
#         self.entryCC = Entry(sFrame)
#         self.entryCC.grid(row=3, column=1, padx=10, pady=8)


#         botonReclamar = Button(sFrame, text="Reclamar Paquete", command=reclamar, font=("arial", 11), fg="white",
#                                bg="#085870")
#         botonReclamar.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

#     def verificarDatos(paq, Cedula):
#         #verificar si estos métodos están y si los puedo acceder
#         guia = producto.getGuia(paq)
#         destinatario = guia.getDestinatario()

#         if int(destinatario.getCedula()) == Cedula:
#             return True
#         return False #esto en caso que no sea el remitente


#     def encontrarProductoPorCodigo(cod):
#         #verificar si estos métodos están y si los puedo acceder
#         for i in producto.getTodosLosProductos():
#             if i.getCodigo() == cod:
#                 return i
#         return None