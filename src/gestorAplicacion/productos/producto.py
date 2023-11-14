import random
from abc import ABC, abstractmethod

class Producto(ABC):
    _contadorProductos = 0 
    _todosLosProductos = []

    def __init__(self, codigo, volumen, peso):
        self.codigo = codigo
        self.peso = peso
        self.volumen = volumen
        self.costoDelPedido = 0.0  
        self.guia = None  

        Producto._contadorProductos += 1

    @classmethod
    def generarCodigo(cls):
        return random.randint(10000, 99999)

    @abstractmethod
    def asignarCostoDelPedido(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    #set
    def setPeso(self, peso):
        self.peso = peso

    def setVolumen(self, volumen):
        self.volumen = volumen

    def setCostodelPedido(self, costoDelPedido):
        self.costoDelPedido = costoDelPedido

    def setGuia(self, guia):
        self.guia = guia
    
    def setCodigo(self, codigo):
        self.codigo = codigo

    #get
    def getCostoDelPedido(self):
        return self.costoDelPedido

    def getCodigo(self):
        return self.codigo

    def getPeso(self):
        return self.peso

    def getVolumen(self):
        return self.volumen

    def getGuia(self):
        return self.guia

    @classmethod
    def getContadorProductos(cls):
        return Producto._contadorProductos

    @classmethod
    def getTodosLosProductos(cls):
        return Producto._todosLosProductos

    @classmethod
    def setTodosLosProductos(cls, productos):
        Producto._todosLosProductos = productos
        