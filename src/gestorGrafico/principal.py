from tkinter import *
from tkinter import messagebox
from gestorGrafico.enviar import Enviar
from gestorGrafico.pagar import Pagar
from gestorGrafico.rastrear import Rastrear
from gestorGrafico.recoger import Recoger
from gestorGrafico.OpinionesSucursal import TablaSucursales

class Principal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Principal Correminas")
        self.resizable(0, 0)
        self.geometry("865x480")
        self.configure(bg="#cedae0")
        self.pack_propagate(False)

        # Funciones para los Labels de los menus
        def Ayuda():
            Autores = (
                "Autores de la aplicacion:\n\n"
                + "Kevin Leandro Ramos Luna \n\n"
                + "Tomas Gomez Cardona\n\n"
                + "Daniela Andrea Sanchez Aristizabal\n\n"
                + "Luis Alejandro Martinez Ramirez\n\n"
                + "Tomas Murillo Aristizabal"
            )

            messagebox.showinfo("Los que se merecen un 5",Autores)

        #Metodo para limpiar una ventana y dejarla sin widgets
        def limpiar(ventana):
            for widget in ventana.winfo_children():
                if isinstance(widget, Frame):
                    widget.destroy()

        def enviar():
            limpiar(self)
            Enviar(self).pack()
            
        def pagar():
            limpiar()
            Pagar(self).pack()
            
        def rastrear():
            limpiar(self)
            Rastrear(self).pack()
        
        def recoger():
            limpiar()
            Recoger(self).pack()
            
        def opinion():
            limpiar()
            OpinionSucursal(self).pack()
            
        def salir():
            self.destroy()

        def infoBasica():
            texto = """¡Bienvenido a la aplicación de Mensajería "Correminas"!

        Para comenzar a disfrutar de nuestra plataforma, dirígete al menú llamado "Procesos y Consultas" en la esquina superior derecha. Aquí encontrarás cinco funcionalidades clave:

        1) Enviar un Paquete: Envía tus paquetes de manera sencilla. Solo necesitas seleccionar el tipo de paquete y proporcionar información básica, incluidos los detalles del remitente y del destinatario.

        2) Pagar Servicios: Realiza el pago de los servicios que nuestra compañía ha proporcionado. Tienes tres opciones de pago: compartido, del remitente o contraentrega.

        3) Rastrear Pedido: Mantén un seguimiento constante de tus paquetes. Ingresa el código de envío y sigue su trayectoria para tener siempre todo bajo control ;)

        4) Recoger Paquete: Facilitamos la recogida de tus paquetes. Simplemente proporciona los datos del destinatario para verificar y retirar tu paquete de nuestra sucursal.

        5) Opinión sobre Sucursales: Queremos conocer tu experiencia. Utiliza esta función para compartir tus opiniones y comentarios sobre el servicio en nuestras sucursales. ¡Valoramos tu retroalimentación y trabajamos para ofrecerte la mejor experiencia posible!

        Gracias por elegir "Correminas". Esperamos que tengas una experiencia excepcional. ¡Envía, paga, sigue, recoge y comparte tu opinión con nosotros!


                """
            messagebox.showinfo("Informacion Basica", texto)


        frame = Frame(self)
        frame.pack(anchor="center",expand=True)

        bienvenida_label = Label(frame, text="¡Bienvenido a la ventana principal de CorreMinas!", font=("Arial", 14), fg="white", bg="#085870")
        bienvenida_label.pack(padx=10, pady=10)
        
        # Menus
        menuBar = Menu(self)
        self.option_add("*tearOff",  False)
        self.config(menu=menuBar)

        # Menu Archivo
        menuArchivo = Menu(menuBar)
        menuBar.add_cascade(label="Archivo",menu=menuArchivo,activebackground="blue")

        menuArchivo.add_cascade(label="Aplicacion",activebackground="blue",command=infoBasica)
        menuArchivo.add_cascade(label="Salir",activebackground="blue",command=salir)

        # Menu Procesos y consultas
        menuProcesosConsultas = Menu(menuBar)
        menuBar.add_cascade(label="Procesos y Consultas",menu=menuProcesosConsultas,activebackground="blue")

        menuProcesosConsultas.add_cascade(label="Envio de Paquetes",activebackground="blue",command=enviar)
        menuProcesosConsultas.add_cascade(label="Pagar Servicios",activebackground="blue",command=pagar)
        menuProcesosConsultas.add_cascade(label="Rastrear Pedido",activebackground="blue",command=rastrear)
        menuProcesosConsultas.add_cascade(label="Recoger Paquete",activebackground="blue",command=recoger)
        menuProcesosConsultas.add_cascade(label="Opinion Sucursales",activebackground="blue",command=opinion)
        
        # Menu Ayuda
        menuAyuda = Menu(menuBar)
        menuBar.add_cascade(label="Ayuda",menu=menuAyuda,activebackground="blue")
        
        menuAyuda.add_cascade(label="Acerca de...",activebackground="blue",command=Ayuda)


 




        self.mainloop()


if __name__=="__main__":
     Principal()