from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.administracion.sucursal import Sucursal
from excepeciones.ErrorAplicacion import ErrorAplicacion
from excepeciones.ExcepEntrys import * 
from excepeciones.ExcepObj import *

class Recoger(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870", highlightthickness=3)
        self.pack(expand=True)
  

        self.Label_Titulo = tk.Label(self, text="Reclamar Paquete", font=("Arial", 30))
        self.Label_Titulo.grid(row=0,column=0,columnspan=2,pady=10)

        self.Label_descripcion = tk.Label(self,text="¡Hola querido cliente! En este apartado podrá reclamarlos paquetes que se hayan enviado\n"+ "a su nombre solo, deberá ingresar la información necesaria para reclamar dicho paquete")
        self.Label_descripcion.grid(row=1, column=0, columnspan=2, pady=10)

        self.Label_sele_suc = tk.Label(self,text="Primero necesitamos saber en qué sucursal se encuentra,\n"+ 
                                       "para ello por favor seleccione una de las opciones")
        self.Label_sele_suc.grid(row=2,column=0,columnspan=2,pady=10)
        #Sucursal a elegir 
        labelSucursal = Label(self,text="Selecciona la sucursal\n"+ 
                              "en la que te encuentras:", font=("Arial",10))
        labelSucursal.grid(pady=10,column=0,row=3,columnspan=2)

        # Crear el Combobox para seleccionar sucursales
        todas_las_sucursales = [s.getNombre() for s in Sucursal.getTodasLasSucursales()]
        self.combobox_sucursales = ttk.Combobox(self, values=todas_las_sucursales)
        self.combobox_sucursales.grid(pady=10,column=0,row=4,columnspan=2)

        # Configurar evento para cambio en el ComboBox
        self.combobox_sucursales.bind("<<ComboboxSelected>>", self.cambiar_frame_sucursal)


    def cambiar_frame_sucursal(self, event):
        # Obtener la sucursal seleccionada
        sucursal_seleccionada = self.combobox_sucursales.get()

        # Cambiar a otro frame y pasar la sucursal seleccionada
        frame_sucursal = FrameSucursal(self.master, sucursal_seleccionada)
        self.pack_forget()  
        frame_sucursal.pack()


class FrameSucursal(tk.Frame):
    def __init__(self, ventana, sucursal_seleccionada):
        super().__init__(ventana)
        self.sucursal_seleccionada = sucursal_seleccionada
        self.config(bg="#085870")
        self.pack(fill="both",expand=True)

         # Crear contenido para el nuevo frame
        etiqueta = tk.Label(self, text=f"Ha seleccionado la sucursal: {self.sucursal_seleccionada}",font=("arial",20))
        etiqueta.pack(pady=40)

        def reclamar():
            try:
                Name = entryName.get()
                Cedula = int(entryCC.get())
                Cod = int(entryCod.get())

                producto = self.encontrarProductoPorCodigo(Cod)
                confirmacion = messagebox.askokcancel("Confirmación", f"¿Está seguro de reclamar el paquete {codigo_paquete}?")

                if confirmacion:
                    if producto:
                        guia = producto.getGuia()
                    if self.verificarDatos(producto,Cedula):
                        if guia.getSucursalLlegada()==self.sucursal:
                            if producto in self.sucursal.getInventario() and guia.getEstado != guia.estado.ENTREGADO:
                                #quiero que salga un nuevo frame con una imagen con un paquete y el texto de poder recoger el paquete
                                messagebox.showinfo("Operación realizada con éxito","Puedes reclamar tu paquete")
                                self.destroy()
                            else:
                                messagebox.showinfo("No ha llegado","El paquete no está disponible para ser recogido")
                        else:
                            messagebox.showinfo("Sucursal errónea","El paquete que intentas buscar no se encuentra en esta sucursal")
                    else:
                        messagebox.showinfo("Datos no válidos","Lo sentimos pero los datos que ingresaste no corresponden con los proporcionados por el remitente")
                else:
                    messagebox.showinfo("Paquete no existente", "El paquete que intentas buscar no existe o ya fue entregado")
                 
            except:
                messagebox.showerror("Error", CampoInvalido().mostrarMensaje())


        titulo = Label(self, text="Reclamar Paquete", font=("arial", 25), fg="white", bg="#085870")
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para reclamar\n"
                 "el paquete que está asociado a usted.")
        descripcion = Label(self, text=texto, font=("arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20)

        sFrame = Frame(self, bg="#cedae0")
        sFrame.pack()

        # Puedes adaptar los nombres de los campos según tus necesidades
        labelCod = Label(sFrame, text="Código del Paquete", font=("arial", 11), fg="white", bg="#085870")
        labelCod.grid(row=1, column=0, padx=10, pady=8)
        entryCod = Entry(sFrame)
        entryCod.grid(row=1, column=1, padx=10, pady=8)

        labelName = Label(sFrame, text="Nombre de quien reclama", font=("arial", 11), fg="white", bg="#085870")
        labelName.grid(row=2, column=0, padx=10, pady=8)
        entryName = Entry(sFrame)
        entryName.grid(row=2, column=1, padx=10, pady=8)

        labelCC = Label(sFrame, text="Cédula de quien reclama", font=("arial", 11), fg="white", bg="#085870")
        labelCC.grid(row=3, column=0, padx=10, pady=8)
        entryCC = Entry(sFrame)
        entryCC.grid(row=3, column=1, padx=10, pady=8)


        botonReclamar = Button(sFrame, text="Reclamar Paquete", command=reclamar, font=("arial", 11), fg="white",
                               bg="#085870")
        botonReclamar.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    def verificarDatos(producto, Cedula):
        #verificar si estos métodos están y si los puedo acceder
        guia = producto.getGuia()
        destinatario = guia.getDestinatario()

        if int(destinatario.getCedula()) == Cedula:
            return True
        return False #esto en caso que no sea el remitente


    def encontrarProductoPorCodigo(cod):
        #verificar si estos métodos están y si los puedo acceder
        for producto in getTodosLosProductos():
            if producto.getCodigo() == cod:
                return producto
        return None