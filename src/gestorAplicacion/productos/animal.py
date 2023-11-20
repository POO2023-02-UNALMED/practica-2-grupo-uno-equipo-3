from gestorAplicacion.productos.producto import Producto


class Animal(Producto):
    class tipoAnimal:
        PERRO = "PERRO"
        GATO = "GATO"
        CABALLO = "CABALLO"
        VACA = "VACA"
        LORO = "LORO"
        HAMSTER = "HAMSTER"
    
    class tamanoAnimal:
        PEQUENO = "PEQUENO"
        MEDIANO = "MEDIANO"
        GRANDE = "GRANDE"

        
    def __init__(self, nombre, edad, peso, tipo):
        super().__init__(Producto.generarCodigo(), peso)
        self._nombre = nombre
        self._edad = edad
        self._tipo = tipo
        self._peligroso = False
        self._tamano = None
        self.asignarVolumen()
        self.asignarTamano()
        self.asignarPeligro()
        self.asignarCostoDelPedido()

    def asignarPeligro(self):
        if self._tipo == Animal.tipoAnimal.PERRO or self._tipo == Animal.tipoAnimal.CABALLO or self._tipo == Animal.tipoAnimal.VACA:
            self.peligroso = True
        else:
            self.peligroso = False

    def asignarTamano(self):
        if self._tipo == Animal.tipoAnimal.PERRO:
            self._tamano = Animal.tamanoAnimal.MEDIANO
        elif self._tipo == Animal.tipoAnimal.GATO:
            self._tamano = Animal.tamanoAnimal.PEQUENO
        elif self._tipo == Animal.tipoAnimal.CABALLO or self._tipo == Animal.tipoAnimal.VACA:  # Corregir aquí
            self._tamano = Animal.tamanoAnimal.GRANDE
        else:
            self._tamano = Animal.tamanoAnimal.PEQUENO


    def asignarVolumen(self):
        if self._tamano == Animal.tamanoAnimal.PEQUENO:
            self._volumen = 1
        elif self._tamano == Animal.tamanoAnimal.MEDIANO:
            self._volumen = 3
        elif self._tamano == Animal.tamanoAnimal.GRANDE:
            self._volumen = 6

    def asignarCostoDelPedido(self):
        if self._tamano == self.tamanoAnimal.PEQUENO:
            self._costoDelPedido = 200000
        elif self._tamano == self.tamanoAnimal.MEDIANO:
            self._costoDelPedido = 350000
        elif self._tamano == self.tamanoAnimal.GRANDE:
            self._costoDelPedido = 500000

        if self._peligroso:
            self._costoDelPedido *= 1.25

    def getNombre(self):
        return self._nombre

    def getEdad(self):
        return self._edad

    def isPeligroso(self):
        return self._peligroso

    def getTipo(self):
        return self._tipo

    def getTamano(self):
        return self._tamano

    def setNombre(self, nombre):
        self._nombre = nombre

    def setEdad(self, edad):
        self._edad = edad

    def setPeligroso(self, peligroso):
        self._peligroso = peligroso

    def setTipo(self, tipo):
        self._tipo = tipo

    def setTamano(self, tamano):
        self._tamano = tamano

    def __str__(self):
        return "---------------------PRODUCTO--------------------\n" + \
            "Tipo de producto: Animal\n" + \
            "Codigo de pedido: " + self._codigo + "\n" + \
            "Nombre: " + self._nombre + "\n" + \
            "Edad: " + str(self._edad) + " años\n" + \
            "Peso: " + str(self._peso) + "kg\n" + \
            "Tamaño: " + self._tamano.name.lower() + "\n" + \
            "Peligroso: " + ("Sí" if self._peligroso else "No")




