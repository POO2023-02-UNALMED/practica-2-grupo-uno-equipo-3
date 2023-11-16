import tkinter as tk
from tkinter import *
from gestorGrafico.principal import Principal
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.destinatario import Destinatario
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
from gestorAplicacion.productos.documento import Documento
from gestorAplicacion.administracion.guia import Guia 
from gestorAplicacion.transportes.transporte import Transporte
from gestorAplicacion.transportes.camion import Camion
from gestorAplicacion.transportes.avion import Avion


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
    medellinSur = Sucursal("Medellin Sur", 500,500,10,10,None,None)
    medellinNorte = Sucursal("Medellin Norte", 500,500,10,10,None,None)
    bogotaSur = Sucursal("Bogota Sur", 500,500,10,10,None,None)
    bogotaNorte = Sucursal("Bogota Norte", 500,500,10,10,None,None)
    caliSur = Sucursal("Cali Sur", 500,500,10,10,None,None)
    caliNorte = Sucursal("Cali Norte", 500,500,10,10,None,None)
    pastoSur = Sucursal("Pasto Sur", 500,500,10,10,None,None)
    pastoNorte = Sucursal("Pasto Norte", 500,500,10,10,None,None)
    
    camionesMN = [Camion(medellinNorte, 27, 300,"ABC109"), Camion(medellinNorte, 27, 300, "ABC110")]
    camionesMS = [Camion(medellinSur, 50, 300, "FUQ143"), Camion(medellinSur, 50, 300, "FUQ142")]
    camionesCN = [Camion(caliNorte, 50, 300, "FTR456"), Camion(caliNorte, 50, 300, "FTR457")]
    camionesCS = [Camion(caliSur, 50, 300, "STU673"), Camion(caliSur, 50, 300, "STU674")]
    camionesPN = [Camion(pastoNorte, 50, 300, "STP673"), Camion(pastoNorte, 50, 300, "STP674")]
    camionesPS = [Camion(pastoSur, 50, 300, "POO123"), Camion(pastoSur, 50, 300, "POO456")]
    camionesBN = [Camion(bogotaNorte, 50, 300, "GUY256"), Camion(bogotaNorte, 50, 300, "GUY257")]
    camionesBS = [Camion(bogotaSur, 50, 300, "QWE109"), Camion(bogotaSur, 50, 300, "QWE110")]

    avionesMN = [Avion(medellinNorte, bogotaNorte, 200, 2000, "EDF678")]
    avionesMS = [Avion(medellinSur, bogotaSur, 200, 2000, "HIJ432")]
    avionesCN = [Avion(caliNorte, medellinNorte, 200, 2000, "KLM123")]
    avionesCS = [Avion(caliSur, medellinSur, 200, 2000, "OKJ098")]
    avionesPN = [Avion(pastoNorte, caliNorte, 200, 2000, "THI876")]
    avionesPS = [Avion(pastoSur, caliSur, 200, 2000, "TLP234")]
    avionesBN = [Avion(bogotaNorte, pastoNorte, 200, 2000, "JHG109")]
    avionesBS = [Avion(bogotaSur, pastoSur, 200, 2000, "DFG567")]
    
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
    
    guzman = Cliente("Jaime Guzman", 123456789, 987654321)
    guzmanCuenta = CuentaBancaria(guzman, 1010101010, 666, "09/27", 1000000)
    
    david = Destinatario("David", 55555, 666666)
    davidCuenta = CuentaBancaria(david, 987654321, 333, "08/25", 300000)
    
    documento = Documento()
    guiaDocumento = Guia(documento, guzman, david, medellinNorte, bogotaSur, Guia.tipoDePago.FRACCIONADO, camionesMN[0])

    Deserializador.deserializar()

    MainWindow()