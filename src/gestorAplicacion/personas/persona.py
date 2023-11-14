from abc import ABC, abstractmethod

class Persona(ABC):
    todasLasPersonas = []

    def __init__(self,nombre, cedula,telefono):
        self.nombre = nombre
        self.cedula =cedula
        self.telefono = telefono
        
        Persona.todasLasPersonas.append(self)

    @abstractmethod
    def __str__(self):
        pass
    
    @classmethod
    def getTodasLasPersonas(cls):
        return cls.todasLasPersonas
    @classmethod
    def setTodasLasPersonas(cls,lista):
        cls.todasLasPersonas = lista

    def getNombre(self):
        return self.nombre
    
    def setNombre(self, nombre):
        self.nombre = nombre

    def getCedula(self):
        return self.cedula
    
    def setCedula(self, cedula):
        self.cedula = cedula

    def getCuentaBancaria(self):
          return self.cuentaBancaria 
      
    def setCuentaBancaria(self,cuentaBancaria):
        self.cuentaBancaria = cuentaBancaria

    def getTelefono(self):
        return self.telefono
    
    def setTelefono(self,telefono):
        self.telefono = telefono