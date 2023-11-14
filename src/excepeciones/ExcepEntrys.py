from excepeciones.ErrorAplicacion import ErrorAplicacion

class ExcepEntrys(ErrorAplicacion):
    def __init__(self,error):
        super().__init__(error)

class CampoVacio(ExcepEntrys):
    def __init__(self):
        super().__init__("Algunos campos del formulario no fueron llenados")

class CampoIncorrecto(ExcepEntrys):
    def __init__(self):
        super().__init__("El tipo de dato de Entrada no es correcto")

class CampoInvalido(ExcepEntrys):
    def __init__(self):
        super().__init__("El Campo no fue llenado correctamente")