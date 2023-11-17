from gestorAplicacion.productos import animal
from gestorAplicacion.productos.animal import Animal



class Sucursal:
    _todasLasSucursales = []

    def __init__(self, nombre, capacidadVolumen, capacidadPeso, longitud, latitud):
        self._nombre = nombre
        palabras = nombre.split()
        self._ciudad = palabras[0]
        self._capacidadVolumen = capacidadVolumen
        self._capacidadPeso = capacidadPeso
        self._longitud = longitud
        self._latitud = latitud
        self._camionesEnSucursal = []
        self._avionesEnSucursal = []
        self._cantidadJaulasPequenas = 5
        self._cantidadJaulasMedianas = 3
        self._cantidadJaulasGrandes = 2
        self._opinionSucursal = None
        self._inventario = []
        Sucursal._todasLasSucursales.append(self)

    def disponibilidadJaulas(self, animal):
        disponibilidad = False

        if animal.getTamano() == "PEQUENO" and self._cantidadJaulasPequenas > 0:
            disponibilidad = True
        elif animal.getTamano() == "MEDIANO" and self._cantidadJaulasMedianas > 0:
            disponibilidad = True
        elif animal.getTamano() == "GRANDE" and self._cantidadJaulasGrandes > 0:
            disponibilidad = True

        return disponibilidad

    def agregarCamion(self, camion):
        self._camionesEnSucursal.append(camion)

    def agregarAvion(self, avion):
        self._avionesEnSucursal.append(avion)

    def removerCamion(self, camion):
        self._camionesEnSucursal.remove(camion)

    def removerAvion(self, avion):
        self._avionesEnSucursal.remove(avion)

    def agregarProducto(self, nuevoProducto):
        seAgrega = False

        if isinstance(nuevoProducto, animal):
            nuevoAnimal = nuevoProducto

            if self._disponibilidadJaulas(nuevoAnimal):
                if self._capacidadVolumen > nuevoAnimal.getVolumen():
                    if self._capacidadPeso > nuevoAnimal.getPeso():
                        self._inventario.append(nuevoAnimal)
                        self._capacidadVolumen -= nuevoAnimal.getVolumen()
                        self._capacidadPeso -= nuevoAnimal.getPeso()
                        seAgrega = True

                        if nuevoAnimal.getTamano() == "PEQUENO":
                            self._cantidadJaulasPequenas -= 1
                        elif nuevoAnimal.getTamano() == "MEDIANO":
                            self._cantidadJaulasMedianas -= 1
                        elif nuevoAnimal.getTamano() == "GRANDE":
                            self._cantidadJaulasGrandes -= 1
        else:
            if self.capacidadVolumen > nuevoProducto.getVolumen():
                if  self._capacidadPeso > nuevoProducto.getPeso():
                    self._inventario.append(nuevoProducto)
                    self._capacidadVolumen -= nuevoProducto.getVolumen()
                    self._capacidadPeso -= nuevoProducto.getPeso()
                    seAgrega = True

        return seAgrega

    def verificarProductoCliente(self, producto):
        if producto in self._inventario:
            return f"El paquete con código {producto.getCodigo()} se encuentra en la sucursal y está listo para ser recogido."
        else:
            return f"Lo sentimos, paquete con código {producto.getCodigo()} no está en la sucursal."

    def verificarProducto(self, producto):
        return producto in self._inventario

    def verificarDisponibilidad(self, producto):
        return self._capacidadVolumen > producto.getVolumen() and self.capacidadPeso > producto.getPeso()

    def ubicar(self, producto):
        for sucursal1 in producto.getGuia().getRuta():
            if sucursal1.verificarProducto(producto):
                return sucursal1.getNombre()
        return f"El producto está en reparto, se encuentra entre {producto.getGuia().getVehiculo()}"

    def getNombre(self):
        return self._nombre

    def getCiudad(self):
        return self._ciudad

    def getLatitud(self):
        return self._latitud

    def getLongitud(self):
        return self._longitud

    @classmethod
    def getTodasLasSucursales(cls):
        return cls._todasLasSucursales

    @classmethod
    def setTodasLasSucursales(cls, lista):
        cls._todasLasSucursales = lista

    def getInventario(self):
        return self._inventario

    def getCorreminas(cls):
        return cls._correminas

    def getCamionesEnSucursal(self):
        return self._camionesEnSucursal

    def getAvionesEnSucursal(self):
        return self._avionesEnSucursal

    def getCapacidadVolumen(self):
        return self._capacidadVolumen
    
    def getCapacidadPeso(self):
        return self._capacidadPeso

    def setCapacidadPeso(self, numero):
        self._capacidadPeso = numero

    def setNombre(self, nombre):
        self._nombre = nombre

    def getOpinionSucursal(self):
        return self._opinionSucursal

    def setOpinionSucursal(self, opinionSucursal):
        self._opinionSucursal = opinionSucursal
        
    def setCamionesEnSucursal(self, camiones):
        self._camionesEnSucursal = camiones
    
    def setAvionesEnSucursal(self, aviones):
        self._avionesEnSucursal = aviones
