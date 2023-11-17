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
  
        self.Label_Titulo = tk.Label(self, text="Recoger Paquete", font=("Arial", 30))
        self.Label_Titulo.pack(pady=10)

        labelCod = Label(tk.Frame, text="Código del paquete",font=("Arial",12))
        labelCod.grid(pady=10,column=0,row=1)

        botonReclamar = Button(self, text="Reclamar Paquete", command=self.reclamar_paquete)
        botonReclamar.pack(pady=20)

    def reclamar_paquete(self):
        try:
            codigo_paquete = int(self.entry_codigo.get())
            nombre_destinatario = self.entry_nombre.get()
            cedula_destinatario = int(self.entry_cedula.get())

           

            producto = self.encontrar_producto_por_codigo(codigo_paquete)

            if producto:
                guia = producto.getGuia()
                if self.verificar_datos(producto, cedula_destinatario):
                    if guia.getSucursalLlegada() == self.sucursal:
                        if producto in self.sucursal.getInventario() and guia.getEstado() != guia.estado.ENTREGADO:
                            # Resto del código para recoger el paquete
                            messagebox.showinfo("Operación exitosa", "Paquete recogido con éxito")
                            self.destroy()
                        else:
                            messagebox.showinfo("Error", "El paquete no está disponible para ser recogido.")
                    else:
                        messagebox.showinfo("Error", "El paquete no está en esta sucursal.")
                else:
                    messagebox.showinfo("Error", "Los datos ingresados no corresponden con los del remitente.")
            else:
                messagebox.showinfo("Error", "El paquete que intenta buscar no existe.")

        except Exception as e:
            messagebox.showerror("Error", str(e))


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
        etiqueta.pack(pady=10)

        def reclamar():
            try:

                nombre_destinatario = nombre_Destinatario2.get()
                cedula_destinatario = int(cedula_Destinatario2.get())
                codigo_paquete = int(codigoPaqueteE.get())

                producto = self.encontrarProductoPorCodigo(codigo_paquete)
                confirmacion = messagebox.askokcancel("Confirmación", f"¿Está seguro de reclamar el paquete {codigo_paquete}?")

                if confirmacion:
                    if producto:
                        guia = producto.getGuia()
                    if self.verificarDatos(producto,cedula_destinatario):
                        if guia.getSucursalLlegada()==self.sucursal:
                            if producto in self.sucursal.getInventario() and guia.getEstado != guia.estado.ENTREGADO:
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


        titulo = Label(self, text="Reclamar Paquete", font=("arial", 14), fg="white", bg="#085870")
        titulo.pack(side="top", anchor="c")

        texto = ("A continuación, deberá ingresar la información necesaria para reclamar\n"
                 "un paquete que será entregado a usted.")
        descripcion = Label(self, text=texto, font=("arial", 11), fg="white", bg="#085870")
        descripcion.pack(anchor="n", pady=20)

        sFrame = Frame(self, bg="#cedae0")
        sFrame.pack()

        # Puedes adaptar los nombres de los campos según tus necesidades
        nombre_Destinatario1 = Label(sFrame, text="Nombre del Paquete", font=("arial", 11), fg="white", bg="#085870")
        nombre_Destinatario1.grid(row=1, column=0, padx=10, pady=8)
        nombre_Destinatario2 = Entry(sFrame, font=("arial", 11))
        nombre_Destinatario2.grid(row=1, column=1, padx=10, pady=8)

        codigoPaqueteL = Label(sFrame, text="Código del Paquete", font=("arial", 11), fg="white", bg="#085870")
        codigoPaqueteL.grid(row=2, column=0, padx=10, pady=8)
        codigoPaqueteE = Entry(sFrame, font=("arial", 11))
        codigoPaqueteE.grid(row=2, column=1, padx=10, pady=8)

        cedula_Destinatario1 = Label(sFrame, text="Descripción del Paquete", font=("arial", 11), fg="white", bg="#085870")
        cedula_Destinatario1.grid(row=3, column=0, padx=10, pady=8)
        cedula_Destinatario2 = Entry(sFrame, font=("arial", 11))
        cedula_Destinatario2.grid(row=3, column=1, padx=10, pady=8)

        # Puedes agregar más campos según tus necesidades

        botonReclamar = Button(sFrame, text="Reclamar Paquete", command=reclamar, font=("arial", 11), fg="white",
                               bg="#085870")
        botonReclamar.grid(row=4, column=0, padx=10, pady=10, sticky='e')


