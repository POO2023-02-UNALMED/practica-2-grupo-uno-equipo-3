from excepeciones.ErrorAplicacion import ErrorAplicacion

class ExcepObj(ErrorAplicacion):
    def __init__(self,error):
        super().__init__(error)

class codigoPaquete(ExcepObj):
    def __init__(self,codigo):
        super().__init__(f"No se ha podido encontrar el paquete relacionado al codigo {codigo}")

class dineroInsuficiente(ExcepObj):
    def __init__(self, cuentaBancaria):
        super().__init__(f"La cuenta bancaria:\n {cuentaBancaria} \n no tiene suficiente saldo")


