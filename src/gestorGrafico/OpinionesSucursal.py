from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.administracion.sucursal import Sucursal
from excepeciones.ErrorAplicacion import ErrorAplicacion
from excepeciones.ExcepEntrys import * 
from excepeciones.ExcepObj import *



class TablaSucursales(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870", highlightthickness=3)

        # Label Titulo
        self.Label_Titulo = tk.Label(self,text= "Seleccione una sucursal",font=("Roman",20))
        self.Label_Titulo.pack(pady=10)
        # Crear el widget Text para la tabla
        self.texto_tabla = tk.Text(self, height=10, width=60)
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

        # Cambiar a otro frame y pasar la sucursal seleccionada
        frame_sucursal = FrameSucursal(self.master, sucursal_seleccionada)
        self.pack_forget()  
        frame_sucursal.pack()

class FrameSucursal(tk.Frame):
    def __init__(self, ventana, sucursal_seleccionada):
        super().__init__(ventana)
        self.sucursal_seleccionada = sucursal_seleccionada

        # Crear contenido para el nuevo frame
        etiqueta = tk.Label(self, text=f"Ha seleccionado la sucursal: {self.sucursal_seleccionada}")
        etiqueta.pack(pady=10)

# class Sucursal:
#     todasLasSucursales = []

#     def __init__(self, nombre):
#         self.nombre = nombre
#         self.opinionSucursal = None
#         Sucursal.todasLasSucursales.append(self)
    
#     def getNombre(self):
#         return self.nombre
#     def getOpinionSucursal(self):
#         return self.opinionSucursal

#     def setOpinionSucursal(self, opinionSucursal):
#         self.opinionSucursal = opinionSucursal

#     @classmethod
#     def getTodasLasSucursales(cls):
#         return cls.todasLasSucursales

# class Opinion:
#     todasLasOpiniones = []
    
#     def __init__(self, opinionPunt, opinionInt, sucursal):
#         self.opinionIntegridad = []
#         self.opinionPuntualidad = []
#         self.opinionIntegridad.append(opinionInt)
#         self.opinionPuntualidad.append(opinionPunt)
#         self.sucursal = sucursal
        
#         self.sucursal.setOpinionSucursal(self)
#         Opinion.todasLasOpiniones.append(self)
    
#     def promedioPuntualidad(self):
#         suma = sum(self.opinionPuntualidad)
#         return suma/ len(self.opinionPuntualidad)
    
#     def promedioIntegridad(self):
#         suma = sum(self.opinionIntegridad)
#         return suma/ len(self.opinionIntegridad)

if __name__ == "__main__":
    MedellinSur = Sucursal("Medellin Sur")
    MedellinNorte = Sucursal("Medellin Norte")
    BogotaSur = Sucursal("Bogota Sur")
    BogotaNorte = Sucursal("Bogota Norte")
    CaliSur = Sucursal("Cali Sur")
    CaliNorte = Sucursal("Cali Norte")
    PastoSur = Sucursal("Pasto Sur")
    PastoNorte = Sucursal("Pasto Norte")

    opinion1 = Opinion(4,4,MedellinNorte)
    opinion2 = Opinion(4,4,MedellinSur)
    opinion3 = Opinion(4,4,BogotaNorte)
    opinion4 = Opinion(4,4,BogotaSur)
    opinion5 = Opinion(4,4,CaliNorte)
    opinion6 = Opinion(4,4,CaliSur)
    opinion7 = Opinion(4,4,PastoNorte)
    opinion8 = Opinion(4,4,PastoSur)
    
    MedellinNorte.setOpinionSucursal(opinion1)
    MedellinSur.setOpinionSucursal(opinion2)
    BogotaNorte.setOpinionSucursal(opinion3)
    BogotaSur.setOpinionSucursal(opinion4)
    CaliNorte.setOpinionSucursal(opinion5)
    CaliSur.setOpinionSucursal(opinion6)
    PastoNorte.setOpinionSucursal(opinion7)
    PastoSur.setOpinionSucursal(opinion8)

    ventana_principal = tk.Tk()
    tabla_sucursales = TablaSucursales(ventana_principal)
    tabla_sucursales.pack(pady=10)

    ventana_principal.mainloop()