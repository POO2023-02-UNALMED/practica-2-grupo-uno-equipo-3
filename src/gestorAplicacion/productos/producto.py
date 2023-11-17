import random
from abc import ABC, abstractmethod

class Producto(ABC):
    _contadorProductos = 0 
    _todosLosProductos = []

    def __init__(self, codigo, volumen, peso):
        self._codigo = codigo
        self._peso = peso
        self._volumen = volumen
        self._costoDelPedido = 0.0  
        self._guia = None  

        Producto._todosLosProductos.append(self)
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
        self._peso = peso

    def setVolumen(self, volumen):
        self._volumen = volumen

    def setCostodelPedido(self, costoDelPedido):
        self._costoDelPedido = costoDelPedido

    def setGuia(self, guia):
        self._guia = guia
    
    def setCodigo(self, codigo):
        self._codigo = codigo

    #get
    def getCostoDelPedido(self):
        return self._costoDelPedido

    def getCodigo(self):
        return self._codigo

    def getPeso(self):
        return self._peso

    def getVolumen(self):
        return self._volumen

    def getGuia(self):
        return self._guia

    @classmethod
    def getContadorProductos(cls):
        return Producto._contadorProductos

    @classmethod
    def getTodosLosProductos(cls):
        return Producto._todosLosProductos

    @classmethod
    def setTodosLosProductos(cls, productos):
        Producto._todosLosProductos = productos
        