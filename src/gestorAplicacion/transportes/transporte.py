from typing import List
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.productos.producto import Producto
from abc import ABC, abstractmethod

class Transporte(ABC):
    todosLosTransportes = []

    def __init__(self, sucursalOrigen, capacidadVolumen, capacidadPeso, matricula, sucursalDestino=None):
        self.sucursalOrigen = sucursalOrigen
        self.sucursalDestino = sucursalDestino
        self.capacidadVolumen = capacidadVolumen
        self.capacidadPeso = capacidadPeso
        self.matricula = matricula
        self.ubicacionActual = sucursalOrigen
        self.ubicacionAnterior = None
        self.ubicacionSiguiente = None
        self.enSucursal = True
        self.ruta = []
        self.inventario = []
        
        Transporte.todosLosTransportes.append(self)

        self.asignarRuta()

    @abstractmethod    
    def asignarRuta(self):
        pass

    @abstractmethod
    def iniciarRecorrido(self):
        pass

    @abstractmethod
    def ubicarTransporte(self):
        pass

    @abstractmethod
    def entrarASucursal(self, sucursal):
        pass

    @abstractmethod
    def salirDeSucursal(self, sucursal):
        pass

    def agregarProductos(self):
        for producto in self.sucursalOrigen.getInventario():
            if producto.getGuia().getSucursalOrigen() == self.sucursalOrigen and producto.getGuia().getVehiculo() == self:
                self.inventario.append(producto)

        for producto in self.inventario:
            if producto in self.sucursalOrigen.getInventario():
                self.sucursalOrigen.getInventario().remove(producto)

    def getUbicacionAnterior(self):
        return self.ubicacionAnterior

    def getUbicacionActual(self):
        return self.ubicacionActual

    def getUbicacionSiguiente(self):
        return self.ubicacionSiguiente

    def getSucursalOrigen(self):
        return self.sucursalOrigen

    def getRuta(self):
        return self.ruta

    def getMatricula(self):
        return self.matricula

    def getInventario(self):
        return self.inventario

    def getCapacidadPeso(self):
        return self.capacidadPeso

    def getCapacidadVolumen(self):
        return self.capacidadVolumen

    @classmethod
    def getTodosLosTransportes(cls):
        return cls.todosLosTransportes

    def isEnSucursal(self):
        return self.enSucursal

    @classmethod
    def setTodosLosTransportes(cls, lista):
        cls.todosLosTransportes = lista

    def setInventario(self, inventario):
        self.inventario = inventario
