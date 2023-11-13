import random

class Membresia:
    class Tipo:
        def __init__(self, probabilidad):
            self.probabilidad = probabilidad

    def __init__(self, cliente=None):
        self.beneficio = self.crear_membresia()
        self.cliente = cliente

    def crear_membresia(self):
        probabilidad_total = 100
        numero_aleatorio = random.randint(1, probabilidad_total)

        acumulado = 0
        for membresia in self.Tipo:
            acumulado += membresia.probabilidad
            if numero_aleatorio <= acumulado:
                return membresia
        return self.Tipo.DEFAULT

    def get_beneficio(self):
        return self.beneficio

    def set_beneficio(self, beneficio):
        self.beneficio = beneficio

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def __str__(self):
        return f"El cliente tiene el beneficio {str(self.get_beneficio()).lower()}"