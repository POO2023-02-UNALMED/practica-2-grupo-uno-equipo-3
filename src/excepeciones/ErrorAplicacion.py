
class ErrorAplicacion(Exception):
    def __init__(self,error):
        self.error = "Manejo de errores de la Aplicacion: " + error
    
    def mostrarMensaje(self):
        return self.error