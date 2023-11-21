import tkinter as tk
from tkinter import *
from gestorGrafico.principal import Principal
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.destinatario import Destinatario
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
from gestorAplicacion.productos.producto import Producto
from gestorAplicacion.productos.animal import Animal
from gestorAplicacion.productos.paquete import Paquete
from gestorAplicacion.productos.documento import Documento
from gestorAplicacion.administracion.guia import Guia 
from gestorAplicacion.transportes.transporte import Transporte
from gestorAplicacion.transportes.camion import Camion
from gestorAplicacion.transportes.avion import Avion
import time
from gestorGrafico.OpinionesSucursal import FrameSucursal


from baseDatos.deserializador import Deserializador
from baseDatos.serializador import Serializador

from gestorGrafico.inicio import Inicio

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Correminas")
        self.resizable(0,0)
        self.geometry("865x480")
        self.iconbitmap("src\gestorGrafico\imagenes\icono.ico")

        Inicio(self)
        self.mainloop()

    def abrirPrincipal(self):
        self.destroy()         
        Principal()
    
    def abrirInicio(self):
        self.destroy()
        MainWindow()

if __name__=="__main__":
    medellinNorte = Sucursal("Medellin Norte", 500,500,10,10)
    medellinSur = Sucursal("Medellin Sur", 500,500,10,10)
    caliNorte = Sucursal("Cali Norte", 500,500,10,10)
    caliSur = Sucursal("Cali Sur", 500,500,10,10)
    pastoNorte = Sucursal("Pasto Norte", 500,500,10,10)
    pastoSur = Sucursal("Pasto Sur", 500,500,10,10)
    bogotaNorte = Sucursal("Bogota Norte", 500,500,10,10)
    bogotaSur = Sucursal("Bogota Sur", 500,500,10,10)

    
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
    
    opinion1 = Opinion(4,4,medellinNorte)
    opinion2 = Opinion(4,4,medellinSur)
    opinion3 = Opinion(4,4,bogotaNorte)
    opinion4 = Opinion(4,4,bogotaSur)
    opinion5 = Opinion(4,4,caliNorte)
    opinion6 = Opinion(4,4,caliSur)
    opinion7 = Opinion(4,4,pastoNorte)
    opinion8 = Opinion(4,4,pastoSur)
    medellinNorte.setOpinionSucursal(opinion1)
    medellinSur.setOpinionSucursal(opinion2)
    bogotaNorte.setOpinionSucursal(opinion3)
    bogotaSur.setOpinionSucursal(opinion4)
    caliNorte.setOpinionSucursal(opinion5)
    caliSur.setOpinionSucursal(opinion6)
    pastoNorte.setOpinionSucursal(opinion7)
    pastoSur.setOpinionSucursal(opinion8)
    
    
    guzman = Cliente("Jaime Guzman", 123456789, 987654321)
    guzmanCuenta = CuentaBancaria(guzman, 1010101010, 666, "09/27", 1000000)
    
    david = Destinatario("David", 55555, 666666)
    davidCuenta = CuentaBancaria(david, 987654321, 333, "08/25", 300000)
    
    oswaldo = Cliente("Oswaldo", 20202020, 567891234)
    oswaldoCuenta = CuentaBancaria(oswaldo, 99999999, 123, "23/29", 0)
    
    documento = Documento()
    guiaDocumento = Guia(documento, guzman, david, medellinNorte, pastoNorte, Guia.tipoDePago.DESTINATARIO, camionesMN[0])
    
    paquete = Paquete(4, 1, 1, 1, True, 10000)
    guiaPaquete = Guia(paquete, guzman, david, medellinNorte, bogotaNorte, Guia.tipoDePago.DESTINATARIO, camionesMN[0])

    animal = Animal("Toby", 3, 10, Animal.tipoAnimal.PERRO)
    guiaAnimal = Guia(animal, oswaldo, david, medellinNorte, bogotaNorte, Guia.tipoDePago.DESTINATARIO, avionesMN[0])
    
    documento2 = Documento()
    guiaDocumento2 = Guia(documento2, guzman, oswaldo, medellinNorte, bogotaNorte, Guia.tipoDePago.REMITENTE, avionesMN[0])
    
    paquete2 = Paquete(10, 3, 3, 3, True, 200000)
    guiaPaquete2 = Guia(paquete2, oswaldo, guzman, medellinNorte, bogotaNorte, Guia.tipoDePago.DESTINATARIO, avionesMN[0])
    
    animal2 = Animal("Ana", 5, 80, Animal.tipoAnimal.VACA)
    guiaAnimal2 = Guia(animal2, david, guzman, medellinNorte, bogotaNorte, Guia.tipoDePago.DESTINATARIO, avionesMN[0])

    medellinNorte.getInventario().append(documento)
    medellinNorte.getInventario().append(paquete)
    medellinNorte.getInventario().append(animal)
    medellinNorte.getInventario().append(documento2)
    medellinNorte.getInventario().append(paquete2)
    medellinNorte.getInventario().append(animal2)
    
    #Serializador.serializar()
    #Deserializador.deserializar()

    #No me lo borren gracias 😉
    camion = medellinNorte.getCamionesEnSucursal()[0]
    #amion.iniciarRecorrido()
    
    avion = medellinNorte.getAvionesEnSucursal()[0]
    #avion.iniciarRecorrido()  
      
    #avion.iniciarRecorrido()    
    
    print(guiaDocumento2) 
    MainWindow()
    
