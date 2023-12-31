from gestorAplicacion.productos.producto import Producto
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.transportes.transporte import Transporte
import time
import threading

class Avion(Transporte):
    def __init__(self, sucursalOrigen, sucursalDestino, capacidadVolumen, capacidadPeso, matricula):
        super().__init__(sucursalOrigen, capacidadVolumen, capacidadPeso, matricula, sucursalDestino)
        self.sucursalOrigen.getAvionesEnSucursal().append(self)
    def asignarRuta(self):
        self.ruta.append(self.sucursalOrigen)
        self.ruta.append(self.sucursalDestino)
        self.ruta.append(self.sucursalOrigen)

    def entrarASucursal(self, sucursal):
        self.ubicacionActual = sucursal
        sucursal.agregarAvion(self)
        for producto in self.inventario:
            if producto.getGuia().getSucursalLlegada() == sucursal:
                if sucursal.getCapacidadVolumen() > producto.getVolumen() and \
                   sucursal.getCapacidadPeso() > producto.getPeso():
                    sucursal.getInventario().append(producto)
                    producto.getGuia().setEstado(Guia.estado.ENESPERA)
        for producto in sucursal.getInventario():
            if producto in self.inventario:
                self.inventario.remove(producto)
        self.enSucursal = True

    def salirDeSucursal(self, sucursal):
        self.ubicacionAnterior = self.ubicacionActual
        self.ubicacionActual = None
        for i in range(len(self.ruta) - 1):
            if self.ruta[i] == self.ubicacionAnterior:
                self.ubicacionSiguiente = self.ruta[i + 1]
        sucursal.removerAvion(self)
        self.enSucursal = False

    def iniciarRecorrido(self):
        self.enSucursal = False
        for producto in self.inventario:
            producto.getGuia().setEstado(Guia.estado.ENTRANSITO)

        self.ubicacionAnterior = self.sucursalOrigen
        self.ubicacionActual = None
        self.ubicacionSiguiente = self.ruta[1]

        def simulacion_thread():
            try:
                time.sleep(30)
            except KeyboardInterrupt:
                raise RuntimeError()
            self.entrarASucursal(self.ruta[1])

            try:
                time.sleep(10)
            except KeyboardInterrupt:
                raise RuntimeError()
            self.salirDeSucursal(self.ruta[1])

            try:
                time.sleep(30)
            except KeyboardInterrupt:
                raise RuntimeError()
            self.entrarASucursal(self.ruta[2])

        simulacionThread = threading.Thread(target=simulacion_thread)
        simulacionThread.start()

    def ubicarTransporte(self):
        if self.enSucursal:
            return f"El Avión de matrícula {self.matricula} que contiene su pedido en este momento se encuentra:\n" \
                   f"En la sucursal {self.ubicacionActual.getNombre()}"
        else:
            return f"El Avión de matrícula {self.matricula} que contiene su pedido en este momento se encuentra volando entre:\n" \
                   f"La sucursal de {self.ubicacionAnterior.getNombre()} y la sucursal de {self.ubicacionSiguiente.getNombre()}"

    def getSucursalDestino(self):
        return self.sucursalDestino
