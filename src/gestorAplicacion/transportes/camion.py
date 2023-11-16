from gestorAplicacion.transportes.transporte import Transporte
from gestorAplicacion.productos.producto import Producto
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.administracion.sucursal import Sucursal

import threading

class Camion(Transporte):
    def __init__(self, sucursalOrigen, capacidadVolumen, capacidadPeso, matricula):
        super().__init__(sucursalOrigen, capacidadVolumen, capacidadPeso, matricula)

    def asignarRuta(self):
        sucursales = Sucursal.getTodasLasSucursales()

        for i in range(len(sucursales)):
            if sucursales[i] == self.getSucursalOrigen():
                for j in range(i, len(sucursales)):
                    self.ruta.append(sucursales[j])

                for k in range(i + 1):
                    self.ruta.append(sucursales[k])

    def entrarASucursal(self, sucursal):
        self.ubicacionActual = sucursal
        sucursal.agregarCamion(self)
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
        sucursal.removerCamion(self)
        self.enSucursal = False

    def iniciarRecorrido(self):
        for producto in self.inventario:
            producto.getGuia().setEstado(Guia.estado.ENTRANSITO)

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
                   f"que contiene su pedido en este momento se encuentra en la sucursal {self.ubicacionActual.getNombre()}"
        else:
            return f"El Camión de matrícula {self.matricula} que contiene su pedido\n" \
                   f"en este momento se encuentra entre la sucursal de\n" \
                   f"{self.ubicacionAnterior.getNombre()} y la sucursal de {self.ubicacionSiguiente.getNombre()}"
