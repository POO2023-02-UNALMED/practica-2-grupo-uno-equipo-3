from transportes import Transporte
from productos import Producto
import time
import threading

class Camion(Transporte):
    def __init__(self, sucursalOrigen, capacidadVolumen, capacidadPeso, matricula):
        super().__init__(sucursalOrigen, capacidadVolumen, capacidadPeso, matricula)

    def asignarRuta(self):
        sucursales = Sucursal.todasLasSucursales

        for i in range(len(sucursales)):
            if sucursales[i] == self._sucursalOrigen():
                for j in range(i, len(sucursales)):
                    self.ruta.append(sucursales[j])

                for k in range(i + 1):
                    self.ruta.append(sucursales[k])

    def entrarASucursal(self, sucursal):
        self.ubicacionActual = sucursal
        sucursal.agregarCamion(self)
        for producto in self.inventario:
            if producto._guia()._sucursalLlegada() == sucursal:
                if sucursal._capacidadVolumen() > producto._volumen() and sucursal._capacidadPeso() > producto._peso():
                    sucursal._inventario().append(producto)
                    producto._guia._estado = Guia.estado.ENESPERA

        for producto in sucursal._inventario():
            if producto in self.inventario:
                self.inventario.remove(producto)
        self.enSucursal = True

    def salirDeSucursal(self, sucursal):
        self.ubicacionAnterior = self.ubicacionActual
        self.ubicacionActual = None

        for i in range(len(self.ruta) - 1):
            if self.ruta[i] == self.ubicacionAnterior:
                self.ubicacionSiguiente = self.ruta[i + 1]

        sucursal.removerCamion(self)
        self.enSucursal = False

    def iniciarRecorrido(self):
        for producto in self.inventario:
            producto._guia._estado = Guia.estado.ENTRANSITO

        self.ubicacionAnterior = self.sucursalOrigen
        self.ubicacionActual = None
        self.ubicacionSiguiente = self.ruta[1]

        def simulacion_thread():
            for i in range(1, len(self.ruta) - 1):
                try:
                    time.sleep(5)
                except KeyboardInterrupt:
                    raise RuntimeError()
                entrarASucursal(self.ruta[i])
                try:
                    time.sleep(5)
                except KeyboardInterrupt:
                    raise RuntimeError()
                salirDeSucursal(self.ruta[i])
            try:
                time.sleep(5)
            except KeyboardInterrupt:
                raise RuntimeError()
            entrarASucursal(self.ruta[-1])

        simulacionThread = threading.Thread(target=simulacion_thread)
        simulacionThread.start()

    def ubicarTransporte(self):
        if self.enSucursal:
            return f"El Camión de matrícula {self.matricula}\n" \
                   f"que contiene su pedido en este momento se encuentra en la sucursal {self.ubicacionActual._nombre()}"
        else:
            return f"El Camión de matrícula {self.matricula} que contiene su pedido\n" \
                   f"en este momento se encuentra entre la sucursal de\n" \
                   f"{self.ubicacionAnterior._nombre()} y la sucursal de {self.ubicacionSiguiente._nombre()}"

