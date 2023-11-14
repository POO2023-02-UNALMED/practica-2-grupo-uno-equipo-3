import tkinter as tk
from tkinter import messagebox,Frame

class Recoger(Frame):
    @staticmethod
    def encontrarProductoPorCodigo(codigo):
        for producto in producto.getTodosLosProductos():
            if producto.getCodigo() == codigo:
                return producto
        return None
    
    @staticmethod
    def verificarDatos(producto, cedulaDestinatario):
        guia = producto.getGuia()
        destinatario = guia.getDestinatario()
        if int(destinatario.getCedula()) == cedulaDestinatario:
            return True
        return False
    def __init__(self, sucursal):
        super().__init__()
        self.sucursal = sucursal
        self.title("Recoger Paquete")
        self.geometry("400x300")

        self.label_codigo = tk.Label(self, text="Ingrese el código de la guía:")
        self.entry_codigo = tk.Entry(self)

        self.label_nombre = tk.Label(self, text="Ingrese su nombre:")
        self.entry_nombre = tk.Entry(self)

        self.label_cedula = tk.Label(self, text="Ingrese su cédula:")
        self.entry_cedula = tk.Entry(self)

        self.button_recoger = tk.Button(self, text="Recoger Paquete", command=self.recoger_paquete)

        self.label_codigo.pack(pady=10)
        self.entry_codigo.pack(pady=5)
        self.label_nombre.pack(pady=10)
        self.entry_nombre.pack(pady=5)
        self.label_cedula.pack(pady=10)
        self.entry_cedula.pack(pady=5)
        self.button_recoger.pack(pady=20)

    def recoger_paquete(self):
        codigo_paquete = int(self.entry_codigo.get())
        nombre_destinatario = self.entry_nombre.get()
        cedula_destinatario = int(self.entry_cedula.get())

        producto = self.encontrarProductoPorCodigo(codigo_paquete)

        if producto:
            guia = producto.getGuia()
            if self.verificarDatos(producto, cedula_destinatario):
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

