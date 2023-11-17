import random

class Membresia:
    class tipo:
        DEFAULT = "DEFAULT"
        SILVER = "SILVER"
        GOLD = "GOLD"
        PLATINUM = "PLATINUM"

    def __init__(self):
        self._beneficio = Membresia.tipo.PLATINUM
        #self._beneficio = self.crearMembresia()

    def crearMembresia(self):
        probabilidadTotal = 100
        numeroAleatorio = random.randint(1, probabilidadTotal)

        acumulado = 0
        for membresia in Membresia.tipo:
            acumulado += membresia.probabilidad
            if numeroAleatorio <= acumulado:
                return membresia
        return Membresia.tipo.DEFAULT

    def getBeneficio(self):
        return self._beneficio

    def setBeneficio(self, beneficio):
        self._beneficio = beneficio

    def __str__(self):
        return f"El cliente tiene el beneficio {str(self.getBeneficio()).lower()}"