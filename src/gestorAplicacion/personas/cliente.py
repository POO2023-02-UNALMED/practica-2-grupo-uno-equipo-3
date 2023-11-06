from persona import Persona
class Cliente(Persona):

    def __init__(self, nombre, cedula, telefono):
        super.__init__(nombre,cedula,telefono)
    
    def getMembresia(self):
        return self.membresia
    def setMembresia(self, membresia):
        self.membresia = membresia

    def __str__(self):
        return f"El cliente identificado como {super.getNombre()} \ncon cedula {super.getCedula()} cuenta con membresia {getMembresia().getBeneficio()}"
    
    def informacionMembresia(self):
         return f"El cliente identificado como {super.getNombre()} \ncon cedula {super.getCedula()} cuenta con membresia  {getMembresia().getBeneficio()}"