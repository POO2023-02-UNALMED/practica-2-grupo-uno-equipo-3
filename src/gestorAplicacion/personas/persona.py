from abc import ABC, abstractmethod

class Persona(ABC):
    _todasLasPersonas = []

    def __init__(self, nombre, cedula,telefono):
        self._nombre = nombre
        self._cedula = cedula
        self._telefono = telefono
        
        Persona._todasLasPersonas.append(self)

    @abstractmethod
    def __str__(self):
        pass
    
    @classmethod
    def getTodasLasPersonas(cls):
        return cls._todasLasPersonas
    
    @classmethod
    def setTodasLasPersonas(cls,lista):
        cls._todasLasPersonas = lista

    def getNombre(self):
        return self._nombre
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def getCedula(self):
        return self._cedula
    
    def setCedula(self, cedula):
        self._cedula = cedula

    def getCuentaBancaria(self):
          return self._cuentaBancaria 
      
    def setCuentaBancaria(self,cuentaBancaria):
        self._cuentaBancaria = cuentaBancaria

    def getTelefono(self):
        return self._telefono
    
    def setTelefono(self,telefono):
        self._telefono = telefono