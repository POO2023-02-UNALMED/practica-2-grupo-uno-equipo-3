class Animal(Producto):
    def __init__(self, nombre, edad, peso, tipo):
        super().__init__(self.generarCodigo(), peso)
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.peligroso = False
        self.tamano = None
        self.asignarTamano()
        self.asignarPeligro()
        self.asignarVolumen()
        self.asignarCostoDelPedido()

    def asignarPeligro(self):
        if self.tipo == self.tipoAnimal.PERRO or self.tipo == self.tipoAnimal.CABALLO or self.tipo == self.tipoAnimal.VACA:
            self.peligroso = True
        else:
            self.peligroso = False

    def asignarTamano(self):
        if self.tipo == self.tipoAnimal.PERRO:
            self.tamano = self.tamanoAnimal.MEDIANO
        elif self.tipo == self.tipoAnimal.GATO:
            self.tamano = self.tamanoAnimal.PEQUENO
        elif self.tipo == self.tipoAnimal.CABALLO or self.tipo == self.tipoAnimal.VACA:
            self.tamano = self.tamanoAnimal.GRANDE
        else:
            self.tamano = self.tamanoAnimal.PEQUENO

    def asignarVolumen(self):
        if self.tamano == self.tamanoAnimal.PEQUENO:
            self.volumen = 1
        elif self.tamano == self.tamanoAnimal.MEDIANO:
            self.volumen = 3
        elif self.tamano == self.tamanoAnimal.GRANDE:
            self.volumen = 6

    def asignarCostoDelPedido(self):
        if self.tamano == self.tamanoAnimal.PEQUENO:
            self.costoDelPedido = 200000
        elif self.tamano == self.tamanoAnimal.MEDIANO:
            self.costoDelPedido = 350000
        elif self.tamano == self.tamanoAnimal.GRANDE:
            self.costoDelPedido = 500000

        if self.peligroso:
            self.costoDelPedido *= 1.25

    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def isPeligroso(self):
        return self.peligroso

    def getTipo(self):
        return self.tipo

    def getTamano(self):
        return self.tamano

    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setPeligroso(self, peligroso):
        self.peligroso = peligroso

    def setTipo(self, tipo):
        self.tipo = tipo

    def setTamano(self, tamano):
        self.tamano = tamano

    def generarCodigo(self):
        # Falta esto xd
        pass

    def __str__(self):
        return "---------------------PRODUCTO--------------------\n" + \
            "Tipo de producto: Animal\n" + \
            "Codigo de pedido: " + self.codigo + "\n" + \
            "Nombre: " + self.nombre + "\n" + \
            "Edad: " + str(self.edad) + " años\n" + \
            "Peso: " + str(self.peso) + "kg\n" + \
            "Tamaño: " + self.tamano.name.lower() + "\n" + \
            "Peligroso: " + ("Sí" if self.peligroso else "No")

    class tipoAnimal(Enum):
        PERRO = 1
        GATO = 2
        CABALLO = 3
        VACA = 4
        LORO = 5
        HAMSTER = 6

    class tamanoAnimal(Enum):
        PEQUENO = 1
        MEDIANO = 2
        GRANDE = 3
