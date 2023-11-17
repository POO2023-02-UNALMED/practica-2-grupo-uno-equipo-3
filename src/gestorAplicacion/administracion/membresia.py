import random
from enum import Enum

class Tipo(Enum):
    DEFAULT = ("DEFAULT", 30)
    SILVER = ("SILVER", 20)
    GOLD = ("GOLD", 15)
    PLATINUM = ("PLATINUM", 35)

class Membresia:
    def __init__(self):
        self._beneficio = self.crearMembresia()

    def crearMembresia(self):
        probabilidadTotal = 100
        numeroAleatorio = random.randint(1, probabilidadTotal)

        acumulado = 0
        for membresia in Tipo:
            acumulado += membresia.value[1]  # Acceder a la probabilidad
            if numeroAleatorio <= acumulado:
                return membresia
        return Tipo.DEFAULT

    def getBeneficio(self):
        return self._beneficio

    def setBeneficio(self, beneficio):
        self._beneficio = beneficio

    def __str__(self):
        return f"El cliente tiene el beneficio {str(self.getBeneficio().value[0]).lower()}"

# if __name__ == "__main__":
#     membresia = Membresia()
#     print(membresia)