from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.administracion.membresia import Membresia

class Cliente(Persona):

    def __init__(self, nombre, cedula, telefono):
        super().__init__(nombre,cedula,telefono)
        self._membresia = Membresia()
    
    def getMembresia(self):
        return self._membresia
    
    def setMembresia(self, membresia):
        self._membresia = membresia

    def __str__(self):
        return f"El cliente identificado como {super().getNombre()} \ncon cedula {super().getCedula()} cuenta con membresia {self.getMembresia().getBeneficio().value[0]}"
    
    def informacionMembresia(self):
         return f"El cliente identificado como {super().getNombre()} \ncon cedula {super().getCedula()} cuenta con membresia  {self.getMembresia().getBeneficio()}"