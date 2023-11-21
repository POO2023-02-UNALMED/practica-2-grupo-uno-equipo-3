from tkinter import *
from tkinter import messagebox
from gestorGrafico.enviar import Enviar
from gestorGrafico.pagar import Pagar
from gestorGrafico.rastrear import Rastrear
from gestorGrafico.rastrear import Estado
from gestorGrafico.recoger import Recoger
from gestorAplicacion.transportes.camion import Camion
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorGrafico.OpinionesSucursal import TablaSucursales
from gestorAplicacion.transportes.transporte import Transporte




class Principal(Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Principal Correminas")
        self.resizable(0, 0)
        self.geometry("865x480")
        self.configure(bg="#ECE3CE")
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
        
        # Metodo para limpiar una ventana y dejarla sin widgets
        def limpiar(ventana):
            for widget in ventana.winfo_children():
                if isinstance(widget, Frame):
                    widget.destroy()
            if Estado.hilos:
                Estado.detenerHilos()
                
            camionesFuera = []
            avionesFuera = []
            
            sucursal = Sucursal.getTodasLasSucursales()[0]
            
            for camion in sucursal.getCamionesEnSucursal():
                camion.agregarProductos()
                
                if camion.getUbicacionActual() == sucursal:
                    if len(camion.getInventario()) >= 3: #Cambiarlo
                        camion.iniciarRecorrido()
                        camionesFuera.append(camion)
                
                else:
                    camionesFuera.append(camion) #Evitar error de duplicacion
                    
            for camion in camionesFuera:
                sucursal.getCamionesEnSucursal().remove(camion)
                
            for avion in sucursal.getAvionesEnSucursal():
                avion.agregarProductos()
                
                if avion.getUbicacionActual() == sucursal:
                    if len(avion.getInventario()) >= 5: #Cambiar
                        avion.iniciarRecorrido()
                        avionesFuera.append(avion)
                
                else:
                    avionesFuera.append(avion)
            
            for avion in avionesFuera:
                sucursal.getAvionesEnSucursal().remove(avion)

        # Porfa no lo comenten que así no puedo hacer pruebas
        def enviar():
            limpiar(self)
            Enviar(self).pack()
            
        def pagar():
            limpiar(self)
            Pagar(self).pack()
            
        def rastrear():
            limpiar(self)
            Rastrear(self).pack()
        
        def recoger():
            limpiar(self)
            Recoger(self).pack()
            
        def opinion():
            limpiar(self)
            TablaSucursales(self).pack()
            
        def salir():
            from main import MainWindow
            self.destroy()
            MainWindow()
            




        def infoBasica():
            texto = """¡Bienvenido a la aplicación de Mensajería "Correminas"!

        Para comenzar a disfrutar de nuestra plataforma, dirígete al menú llamado "Procesos y Consultas" en la esquina superior derecha. Aquí encontrarás cinco funcionalidades clave:

        1) Enviar Producto: Envía tus paquetes de manera sencilla. Solo necesitas seleccionar el tipo de paquete y proporcionar información básica, incluidos los detalles del remitente y del destinatario.

        2) Pagar Servicios: Realiza el pago de los servicios que nuestra compañía ha proporcionado. Tienes tres opciones de pago: compartido, del remitente o contraentrega.

        3) Rastrear Pedido: Mantén un seguimiento constante de tus paquetes. Ingresa el código de envío y sigue su trayectoria para tener siempre todo bajo control ;)

        4) Recoger Paquete: Facilitamos la recogida de tus paquetes. Simplemente proporciona los datos del destinatario para verificar y retirar tu paquete de nuestra sucursal.

        5) Opinión sobre Sucursales: Queremos conocer tu experiencia. Utiliza esta función para compartir tus opiniones y comentarios sobre el servicio en nuestras sucursales. ¡Valoramos tu retroalimentación y trabajamos para ofrecerte la mejor experiencia posible!

        Gracias por elegir "Correminas". Esperamos que tengas una experiencia excepcional. ¡Envía, paga, sigue, recoge y comparte tu opinión con nosotros!


                """
            messagebox.showinfo("Informacion Basica", texto)


        frame = Frame(self)
        frame.config(bg="#739072")
        frame.pack(expand=True)

        bienvenida_label = Label(frame, text="¡Bienvenido a la ventana principal de CorreMinas!", font=("Arial", 14), fg="white", bg="#739072")
        bienvenida_label.pack(padx=10, pady=10)

        frame_2 = Frame(self)
        frame_2.config(bg="#739072")
        frame_2.pack(expand=True)

        info_Label = Label(frame_2,text= """
        Para comenzar a disfrutar de nuestra plataforma, dirígete al menú llamado "Procesos y Consultas" en la esquina superior derecha. Aquí encontrarás cinco funcionalidades clave:

        1) Enviar Producto: Envía tus paquetes de manera sencilla. Solo necesitas seleccionar el tipo de paquete y proporcionar información básica, incluidos los detalles del remitente y del destinatario.

        2) Pagar Servicios: Realiza el pago de los servicios que nuestra compañía ha proporcionado. Tienes tres opciones de pago: compartido, del remitente o contraentrega.

        3) Rastrear Pedido: Mantén un seguimiento constante de tus paquetes. Ingresa el código de envío y sigue su trayectoria para tener siempre todo bajo control ;)

        4) Recoger Paquete: Facilitamos la recogida de tus paquetes. Simplemente proporciona los datos del destinatario para verificar y retirar tu paquete de nuestra sucursal.

        5) Opinión sobre Sucursales: Queremos conocer tu experiencia. Utiliza esta función para compartir tus opiniones y comentarios sobre el servicio en nuestras sucursales. ¡Valoramos tu retroalimentación y trabajamos para ofrecerte la mejor experiencia posible!

        Gracias por elegir "Correminas". Esperamos que tengas una experiencia excepcional. ¡Envía, paga, sigue, recoge y comparte tu opinión con nosotros!""",font=("Arial",10),fg="white",bg="#739072",wraplength=600)
        info_Label.pack(padx=10,pady=10)

        # Menus
        menuBar = Menu(self)
        self.option_add("*tearOff",  False)
        self.config(menu=menuBar)

        # Menu Archivo
        menuArchivo = Menu(menuBar)
        menuBar.add_cascade(label="Archivo",menu=menuArchivo,activebackground="#3A4D39")

        menuArchivo.add_cascade(label="Aplicacion",activebackground="#3A4D39",command=infoBasica)
        menuArchivo.add_cascade(label="Salir",activebackground="#3A4D39",command=salir)

        # Menu Procesos y consultas
        menuProcesosConsultas = Menu(menuBar)
        menuBar.add_cascade(label="Procesos y Consultas",menu=menuProcesosConsultas,activebackground="#3A4D39")

        menuProcesosConsultas.add_cascade(label="Enviar Producto",activebackground="#3A4D39", command=enviar)
        menuProcesosConsultas.add_cascade(label="Pagar Servicios",activebackground="#3A4D39", command=pagar)
        menuProcesosConsultas.add_cascade(label="Rastrear Pedido",activebackground="#3A4D39", command=rastrear)
        menuProcesosConsultas.add_cascade(label="Reclamar Paquete",activebackground="#3A4D39", command=recoger)
        menuProcesosConsultas.add_cascade(label="Opinion Sucursales",activebackground="#3A4D39", command=opinion)
        
        # Menu Ayuda
        menuAyuda = Menu(menuBar)
        menuBar.add_cascade(label="Ayuda",menu=menuAyuda,activebackground="#3A4D39")
        
        menuAyuda.add_cascade(label="Acerca de...",activebackground="#3A4D39",command=Ayuda)


 




        self.mainloop()


