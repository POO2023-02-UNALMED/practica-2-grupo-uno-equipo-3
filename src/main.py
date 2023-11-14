import tkinter as tk
from tkinter import *
from gestorGrafico.principal import Principal
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion
from baseDatos.deserializador import Deserializador
from baseDatos.serializador import Serializador

from gestorGrafico.inicio import Inicio

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Correminas")
        self.resizable(0,0)
        self.geometry("865x480")
        Inicio(self)
        self.mainloop()

    def abrirPrincipal(self):
        self.destroy()         
        Principal()

if __name__=="__main__":
    # MedellinSur = Sucursal("Medellin Sur", 500,500,10,10,None,None)
    # MedellinNorte = Sucursal("Medellin Norte", 500,500,10,10,None,None)
    # BogotaSur = Sucursal("Bogota Sur", 500,500,10,10,None,None)
    # BogotaNorte = Sucursal("Bogota Norte", 500,500,10,10,None,None)
    # CaliSur = Sucursal("Cali Sur", 500,500,10,10,None,None)
    # CaliNorte = Sucursal("Cali Norte", 500,500,10,10,None,None)
    # PastoSur = Sucursal("Pasto Sur", 500,500,10,10,None,None)
    # PastoNorte = Sucursal("Pasto Norte", 500,500,10,10,None,None)
    # opinion1 = Opinion(4,4,MedellinNorte)
    # opinion2 = Opinion(4,4,MedellinSur)
    # opinion3 = Opinion(4,4,BogotaNorte)
    # opinion4 = Opinion(4,4,BogotaSur)
    # opinion5 = Opinion(4,4,CaliNorte)
    # opinion6 = Opinion(4,4,CaliSur)
    # opinion7 = Opinion(4,4,PastoNorte)
    # opinion8 = Opinion(4,4,PastoSur)
    # MedellinNorte.setOpinionSucursal(opinion1)
    # MedellinSur.setOpinionSucursal(opinion2)
    # BogotaNorte.setOpinionSucursal(opinion3)
    # BogotaSur.setOpinionSucursal(opinion4)
    # CaliNorte.setOpinionSucursal(opinion5)
    # CaliSur.setOpinionSucursal(opinion6)
    # PastoNorte.setOpinionSucursal(opinion7)
    # PastoSur.setOpinionSucursal(opinion8)
    # Serializador.serializar()

    Deserializador.deserializar()

    MainWindow()