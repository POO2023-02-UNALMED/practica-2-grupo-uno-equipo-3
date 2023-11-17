from gestorAplicacion.personas.persona import Persona 
# Falta implementar serialización

class Destinatario(Persona):

    def __init__(self, nombre, cedula, telefono):
        super().__init__(nombre, cedula, telefono)
    
    def __str__(self):
        return f"El destinatario identificado como {self.nombre} y cedula {self.cedula}"
