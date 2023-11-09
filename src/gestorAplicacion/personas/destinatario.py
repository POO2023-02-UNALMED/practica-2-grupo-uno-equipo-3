from persona import Persona 
# Falta implementar serialización

class Destinatario(Persona):

    def __init__(self, nombre, cedula, telefono):
        super.__init__(nombre, cedula, telefono)

    def __init__(self):
        self.nombre = "pepito"
        self.cedula = "105678907L" 
        self.telefono = "3225678976L"
    
    def __str__(self):
        return f"El destinatario identificado como {self.nombre} y cedula {self.cedula}"
