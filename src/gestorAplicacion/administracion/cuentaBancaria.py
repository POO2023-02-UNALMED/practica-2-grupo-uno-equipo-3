import random

class CuentaBancaria:
    todas_las_cuentas = []

    def __init__(self, titular, numero, cvv, fecha_expiracion, saldo):
        self.titular = titular
        self.numero = numero
        self.cvv = cvv
        self.fecha_expiracion = fecha_expiracion
        self.saldo = saldo

        

        CuentaBancaria.todas_las_cuentas.append(self)

    @classmethod
    def generar_numero_aleatorio(cls):
        numero = 100000000000 + random.randint(0, 899999999)
        return numero

    @classmethod
    def generar_cvv_aleatorio(cls):
        cvv = 100 + random.randint(0, 899)
        return cvv

    @classmethod
    def generar_fecha_expiracion_aleatoria(cls):
        mes = 1 + random.randint(0, 11)
        año = 22 + random.randint(0, 9)
        fecha_expiracion = f"{mes:02d}/{año:02d}"
        return fecha_expiracion

    @classmethod
    def generar_saldo_aleatorio(cls):
        saldo = random.randint(0, 9999999)
        return saldo

    def get_titular(self):
        return self.titular

    def get_numero(self):
        return self.numero

    def get_cvv(self):
        return self.cvv

    def get_fecha_expiracion(self):
        return self.fecha_expiracion

    def get_saldo(self):
        return self.saldo

    @classmethod
    def get_todas_las_cuentas(cls):
        return cls.todas_las_cuentas
    @classmethod
    def setTodasLasCuentasBancarias(cls,lista):
        cls.todas_las_cuentas = lista

    def set_saldo(self, saldo):
        self.saldo = saldo

    def __str__(self):
        return "--------------------------------\n" + \
               "Titular: " + self.get_titular().get_nombre() + "\n" + \
               "Número De Cuenta: " + str(self.numero) + "\n" + \
               "CVV: " + str(self.cvv) + "\n" + \
               "Fecha De Expiración: " + self.fecha_expiracion + "\n" + \
               "Saldo: $" + str(self.saldo) + "\n" + \
               "--------------------------------"

    def descontar_saldo(self, monto_a_pagar):
        if self.saldo < monto_a_pagar:
            return False
        else:
            self.saldo -= monto_a_pagar
            return True

    def aumentar_saldo(self, monto_a_pagar):
        self.saldo += monto_a_pagar

    todas_las_cuentas = []