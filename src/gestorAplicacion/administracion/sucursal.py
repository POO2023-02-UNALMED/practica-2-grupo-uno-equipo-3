from gestorAplicacion.productos.animal import Animal



class Sucursal:
    todasLasSucursales = []

    def __init__(self, nombre, capacidadVolumen, capacidadPeso, longitud, latitud, camionesEnSucursal, avionesEnSucursal):
        self.nombre = nombre
        palabras = nombre.split()
        self.ciudad = palabras[0]
        self.capacidadVolumen = capacidadVolumen
        self.capacidadPeso = capacidadPeso
        self.longitud = longitud
        self.latitud = latitud
        self.camionesEnSucursal = camionesEnSucursal
        self.avionesEnSucursal = avionesEnSucursal
        self.cantidadJaulasPequenas = 5
        self.cantidadJaulasMedianas = 3
        self.cantidadJaulasGrandes = 2
        self.opinionSucursal = None
        self.inventario = []
        Sucursal.todasLasSucursales.append(self)

    def disponibilidadJaulas(self, animal):
        disponibilidad = False

        if animal.getTamano() == "PEQUENO" and self.cantidadJaulasPequenas > 0:
            disponibilidad = True
        elif animal.getTamano() == "MEDIANO" and self.cantidadJaulasMedianas > 0:
            disponibilidad = True
        elif animal.getTamano() == "GRANDE" and self.cantidadJaulasGrandes > 0:
            disponibilidad = True

        return disponibilidad

    def agregarCamion(self, camion):
        self.camionesEnSucursal.append(camion)

    def agregarAvion(self, avion):
        self.avionesEnSucursal.append(avion)

    def removerCamion(self, camion):
        self.camionesEnSucursal.remove(camion)

    def removerAvion(self, avion):
        self.avionesEnSucursal.remove(avion)

    def agregarProducto(self, nuevoProducto):
        seAgrega = False

        if isinstance(nuevoProducto, Animal):
            nuevoAnimal = nuevoProducto

            if self.disponibilidadJaulas(nuevoAnimal) and self.capacidadVolumen > nuevoAnimal.getVolumen() and self.capacidadPeso > nuevoAnimal.getPeso():
                self.inventario.append(nuevoAnimal)
                self.capacidadVolumen -= nuevoAnimal.getVolumen()
                self.capacidadPeso -= nuevoAnimal.getPeso()
                seAgrega = True

                if nuevoAnimal.getTamano() == "PEQUENO":
                    self.cantidadJaulasPequenas -= 1
                elif nuevoAnimal.getTamano() == "MEDIANO":
                    self.cantidadJaulasMedianas -= 1
                elif nuevoAnimal.getTamano() == "GRANDE":
                    self.cantidadJaulasGrandes -= 1
        else:
            if self.capacidadVolumen > nuevoProducto.getVolumen() and self.capacidadPeso > nuevoProducto.getPeso():
                self.inventario.append(nuevoProducto)
                self.capacidadVolumen -= nuevoProducto.getVolumen()
                self.capacidadPeso -= nuevoProducto.getPeso()
                seAgrega = True

        return seAgrega

    def verificarProductoCliente(self, producto):
        if producto in self.inventario:
            return f"El paquete con código {producto.getCodigo()} se encuentra en la sucursal y está listo para ser recogido."
        else:
            return f"Lo sentimos, paquete con código {producto.getCodigo()} no está en la sucursal."

    def verificarProducto(self, producto):
        return producto in self.inventario

    def verificarDisponibilidad(self, producto):
        return self.capacidadVolumen > producto.getVolumen() and self.capacidadPeso > producto.getPeso()

    def ubicar(self, producto):
        for sucursal1 in producto.getGuia().getRuta():
            if sucursal1.verificarProducto(producto):
                return sucursal1.getNombre()
        return f"El producto está en reparto, se encuentra entre {producto.getGuia().getVehiculo()}"

    def getNombre(self):
        return self.nombre

    def getCiudad(self):
        return self.ciudad

    def getLatitud(self):
        return self.latitud

    def getLongitud(self):
        return self.longitud

    @classmethod
    def getTodasLasSucursales(cls):
        return cls.todasLasSucursales

    @classmethod
    def setTodasLasSucursales(cls, lista):
        cls.todasLasSucursales = lista

    def getInventario(self):
        return self.inventario

    def getCorreminas(cls):
        return cls.correminas

    def getCamionesEnSucursal(self):
        return self.camionesEnSucursal

    def getAvionesEnSucursal(self):
        return self.avionesEnSucursal

    def getCapacidadVolumen(self):
        return self.capacidadVolumen

    def getCapacidadPeso(self):
        return self.capacidadPeso

    def setCapacidadPeso(self, numero):
        self.capacidadPeso = numero

    def setNombre(self, nombre):
        self.nombre = nombre

    def getOpinionSucursal(self):
        return self.opinionSucursal

    def setOpinionSucursal(self, opinionSucursal):
        self.opinionSucursal = opinionSucursal
