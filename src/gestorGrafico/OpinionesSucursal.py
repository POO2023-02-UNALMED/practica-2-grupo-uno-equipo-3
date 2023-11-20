from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorGrafico.FieldFrame import FieldFrame
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.administracion.membresia import *
from excepeciones.ErrorAplicacion import ErrorAplicacion
from excepeciones.ExcepEntrys import * 
from excepeciones.ExcepObj import *



class TablaSucursales(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(bg="#739072", highlightbackground="#3A4D39", highlightthickness=3)
        

        # Label Titulo
        self.Label_Titulo = tk.Label(self,text= "Opinion Sucursal",font=("Arial",30),bg="#739072",fg="white")
        self.Label_Titulo.pack(pady=10)

        self.Label_Descripccion = tk.Label(self,text="Queremos conocer tu experiencia. Utiliza esta función para compartir tus opiniones y comentarios sobre el servicio en nuestras sucursales. ¡Valoramos tu retroalimentación y trabajamos para ofrecerte la mejor experiencia posible!",font=("Arial",10),wraplength=250,bg="#739072",fg="white")
        self.Label_Descripccion.pack(pady=10)
        
        # Crear el widget Text para la tabla
        self.texto_tabla = tk.Text(self, height=10, width=60,bg="#739072",fg="white")
        self.texto_tabla.pack()

        # Crear el Combobox para seleccionar sucursales
        todas_las_sucursales = [s.getNombre() for s in Sucursal.getTodasLasSucursales()]
        self.combobox_sucursales = ttk.Combobox(self, values=todas_las_sucursales)
        self.combobox_sucursales.pack(pady=10)

        # Configurar evento para cambio en el ComboBox
        self.combobox_sucursales.bind("<<ComboboxSelected>>", self.cambiar_frame_sucursal)

        # Llenar el widget Text con la tabla inicial
        self.generar_tabla_sucursales()

    def generar_tabla_sucursales(self):
        tabla = []
        tabla.append("{:<20} {:>15} {:>20}".format("Sucursales", "Punt. Puntualidad", "Punt. Integridad"))
        tabla.append("------------------------------------------------------------")

        # Obtener datos de todas las sucursales
        for sucursal in Sucursal.getTodasLasSucursales():
            tabla.append("{:<20} {:>15.2f} {:>15.2f}".format(
                sucursal.getNombre(),
                sucursal.getOpinionSucursal().promedioPuntualidad(),
                sucursal.getOpinionSucursal().promedioIntegridad()
            ))

        tabla.append("------------------------------------------------------------")

        # Limpiar el contenido actual del widget Text
        self.texto_tabla.delete(1.0, tk.END)

        # Agregar la tabla al widget Text
        for linea in tabla:
            self.texto_tabla.insert(tk.END, f"{linea}\n")

    def cambiar_frame_sucursal(self, event):
        # Obtener la sucursal seleccionada
        sucursal_seleccionada = self.combobox_sucursales.get()
        print(sucursal_seleccionada)
        sucursal_encontrada = None
        for sucursal in Sucursal.getTodasLasSucursales():
            if sucursal.getNombre() == sucursal_seleccionada:
                sucursal_encontrada = sucursal
                break  # El break debe estar dentro de esta condición
        print(sucursal_encontrada)

        # Cambiar a otro frame y pasar la sucursal seleccionada
        frame_sucursal = FrameSucursal(self.master, sucursal_seleccionada, sucursal_encontrada)
        self.pack_forget()
        frame_sucursal.pack()
    
    

class FrameSucursal(tk.Frame):
    def __init__(self, ventana, sucursal_seleccionada,sucursal_encontrada):
        super().__init__(ventana)
        self.sucursal_seleccionada = sucursal_seleccionada
        self.sucursal_encontrada = sucursal_encontrada
        self.config(bg="#ECE3CE")
        self.pack(fill="both",expand=True)
        
        def cambiar_frame_confirmacion():
            self.pack_forget()
            frame_confirmacion = FrameConfirmacion(self.master)
            frame_confirmacion.pack()

        def cambiar_frame_datos():
            self.pack_forget()
            frame_datos = FrameDatos(self.master)
            frame_datos.pack()

        def verificacion_Puntualidad():
            sucursal = self.sucursal_encontrada
            resultado = False
            if sucursal.getOpinionSucursal().promedioPuntualidad() <= 1:
                sucursal.setCapacidadPeso(sucursal.getCapacidadPeso() - 10)
                resultado = True
            return resultado



        # Logica de Las opiniones
        def guardar_opiniones():
            valores_opiniones = fieldFrame_opiniones.guardarValores()
            try:
                opinion_Integridad  = float(valores_opiniones[0])
                opinion_Puntualidad = float(valores_opiniones[1])
                if 0 <= opinion_Integridad <= 5 and 0 <= opinion_Puntualidad <= 5:

                    self.sucursal_encontrada.getOpinionSucursal().opinionIntegridad.append(opinion_Integridad)
                    self.sucursal_encontrada.getOpinionSucursal().opinionPuntualidad.append(opinion_Puntualidad)
                    confirmacion = messagebox.askokcancel("Confirmacion","Desea confirmar las opiniones registradas")
                    if confirmacion and opinion_Integridad >= 1 :
                        cambiar_frame_confirmacion()
                    elif confirmacion and opinion_Integridad < 1:
                        cambiar_frame_datos()
                else:
                    messagebox.showerror("Error",CampoInvalido().mostrarMensaje())
            except:
                messagebox.showerror("Error",CampoIncorrecto().mostrarMensaje())
            finally:
                if verificacion_Puntualidad():
                    messagebox.showwarning("Alerta Punt Puntualiadad baja", f"Sentimos la molestia que pudimos haber causado, para el mejoramiento del servicio hemos implementado en esta sucursal un plan de mejoramiento en la sucursal {self.sucursal_seleccionada}.")



        # Crear contenido para el nuevo frame
        frame = Frame(self,bg="#739072")
        frame.pack(padx=10,pady=10)

        etiqueta = tk.Label(frame, text=f"Ha seleccionado la sucursal: {self.sucursal_seleccionada}",font=("Arial",20),bg="#3A4D39",fg="white")
        etiqueta.pack(pady=10,padx=10)

        label_info = tk.Label(frame,text="Por favor, comparte tu opinión sobre la sucursal, calificándola en una escala del 1 al 5.",font=("Arial",10),bg="#3A4D39",fg="white")
        label_info.pack(pady=10,padx=10)

        titulo_criterio = "Opiniones"
        criterios = ["Opinion Integridad", "Opinion Puntualidad"]
        titulo_valores = "Valores del 1 al 5"


        fieldFrame_opiniones = FieldFrame(self, titulo_criterio, criterios, titulo_valores,None,None)
        fieldFrame_opiniones.pack(padx=30,pady=30)
        fieldFrame_opiniones.config(width=400,height=400,bg="#ECE3CE")
        
        # Agregar un botón para guardar las opiniones
        boton_guardar = tk.Button(self, text="Guardar Opiniones", command=guardar_opiniones)
        boton_guardar.pack(pady=10)


class FrameConfirmacion(tk.Frame):
        def __init__(self, ventana):
            super().__init__(ventana)
            self.config(bg="#ECE3CE")
            self.pack(fill="both",expand=True)

            frame = Frame(self,bg="#739072")
            
            frame.pack(anchor="center",expand=True)

            Confirmacion_label = Label(frame, text="¡Muchas Gracias por registrar tu opinion!", font=("Arial", 20), fg="white", bg="#3A4D39")
            Confirmacion_label.pack(padx=10, pady=10)

            agradecimiento_label = Label(frame, text="En nuestra empresa tu opinion hace la diferencia...", font=("Arial",10),fg="white", bg="#3A4D39")
            agradecimiento_label.pack(padx=10,pady=10)


class FrameDatos(tk.Frame):
    def __init__(self,ventana):
        super().__init__(ventana)
        self.config(bg="#ECE3CE")
        self.pack(fill="both",expand=True)

        def guardar_datos():
            datos = fieldFrame_Datos.guardarValores()

            try:
                nombre = datos[0]
                cedula = int(datos[1])
                telefono = int(datos[2])
                encontrado = False

                for persona in Persona.getTodasLasPersonas():
                    if persona._nombre == nombre and persona._cedula == cedula and isinstance(persona, Cliente):
                        encontrado = True
                        persona.getMembresia().setBeneficio(Tipo.PLATINUM)
                        
                        label_resultado.config(bg="white", text="Lamentamos los inconvenientes Sr/ Sra " + persona.getNombre() + " se le ha mejorado la membresia a Platinum como compensacion")
                        break  # Terminar la búsqueda una vez que se ha encontrado la persona
                    
                if not encontrado:
                    persona_nueva = Cliente(nombre, cedula, telefono)
                    persona_nueva.getMembresia().setBeneficio(Tipo.PLATINUM)
                    
                    label_resultado.config(bg="white",text="Se le ha creado una cuenta con los siguientes datos: " + persona_nueva.__str__() + " La proxima vez que use nuestro servicio utilice esta cuenta para acceder a grandiosos beneficios.",wraplength=0)

            except:
                messagebox.showerror("Error",CampoIncorrecto().mostrarMensaje())


        titulo_criterio = "Datos Personales"
        criterios = ["Nombre","Cedula","Telefono"]
        titulo_valores = ""

        frame = Frame(self,bg="#739072")
        frame.pack(padx=10,pady=10)
        Disculpas_label = Label(frame, text= "Sentimos su mala experiencia con nuestro servicio",font=("Arial",20),fg="white", bg="#3A4D39")
        Disculpas_label.pack(padx=10,pady=10)
        info_label = Label(frame, text="Como compensación, por favor, proporcione sus datos y le otorgaremos una recompensa",font=("Arial",10),fg="white", bg="#3A4D39",wraplength=0)
        info_label.pack(padx=10,pady=10)

        fieldFrame_Datos = FieldFrame(self,titulo_criterio,criterios,titulo_valores,None,None)
        fieldFrame_Datos.pack(padx=30,pady=30)
        fieldFrame_Datos.config(width=400,height=400,bg="#ECE3CE")

        boton_guardar = tk.Button(self, text="Guardar Datos", command=guardar_datos)
        boton_guardar.pack(pady=10)

        label_resultado = Label(self,text="",bg="#ECE3CE")
        label_resultado.pack(pady=10)





        

            

        

