from datetime import datetime
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.personas.cliente import Cliente
from enum import Enum
#Ya importe avion y camion dentro de los metodos que se usan, no se puede poner aqui por importacion circular
#falta importar cosas
class Guia:
    class tipoDePago(Enum):
        REMITENTE = "REMITENTE"
        FRACCIONADO = "FRACCIONADO"
        DESTINATARIO = "DESTINATARIO"

    class estado(Enum):
        ENSUCURSALORIGEN = "ENSUCURSALORIGEN"
        ENTRANSITO = "ENTRANSITO"
        ENESPERA = "ENESPERA"
        ENTREGADO = "ENTREGADO"

    _todasLasGuias = []

    def __init__(self, producto, remitente, destinatario, sucursalOrigen, sucursalLlegada, tipoDePago, vehiculo):
        Guia._todasLasGuias.append(self)
        self._producto = producto
        self._remitente = remitente
        self._destinatario = destinatario
        self._sucursalOrigen = sucursalOrigen
        self._sucursalLlegada = sucursalLlegada
        self._tipoDePago = tipoDePago
        self._vehiculo = vehiculo
        self._ruta = []
        vehiculo.getInventario().append(producto)
        producto.setGuia(self)
        self._estado = Guia.estado.ENSUCURSALORIGEN
        self.progreso = 0
        self._fecha = datetime.now()
        fecha_formatter = "%d/%m/%y %H:%M"
        self._fechaDeEnvio = self._fecha.strftime(fecha_formatter)
        self.asignarRuta()
        self.asignarPrecio()
        self.aplicarDescuento()
        self._pagoPendiente = self._precioTotal
        # if tipoDePago == Guia.tipoDePago.REMITENTE:
        #     self._pagoPendiente = 0
        # elif tipoDePago == Guia.tipoDePago.FRACCIONADO:
        #     self._pagoPendiente = self._precioTotal / 2
        # elif tipoDePago == Guia.tipoDePago.DESTINATARIO:
        #     self._pagoPendiente = self._precioTotal

    def avancePedido(self):
        from gestorAplicacion.transportes.camion import Camion
        if self._estado == Guia.estado.ENSUCURSALORIGEN:
            return 0
        elif self._estado == Guia.estado.ENESPERA or self.estado == Guia.estado.ENTREGADO:
            return 100
        elif self._estado == Guia.estado.ENTRANSITO:
            porcentaje = 30
            if isinstance(self._vehiculo, Camion):
                escalas = 100.0 / (len(self._ruta) - 1)
                camion = self._vehiculo
                if camion.ubicacionActual is not None:
                    porcentaje = escalas * self._ruta.index(camion.ubicacionActual)
                    redondeado = round(porcentaje, 1)
                    return redondeado
                else:
                    porcentaje = (escalas * self._ruta.index(camion.ubicacionAnterior)) + (escalas / 2)
                    redondeado = round(porcentaje, 1)
                    return redondeado
            else:
                return 0
        else:
            return 0

    def asignarPrecio(self):
        from gestorAplicacion.transportes.avion import Avion
        from gestorAplicacion.transportes.camion import Camion

        cantidadDeSucursales = len(self._ruta) - 1
        costoTransporte = 0
        if isinstance(self._vehiculo, Camion):
            costoTransporte = 3000
        elif isinstance(self._vehiculo, Avion):
            costoTransporte = 7000
        self._precioTotal = self._producto._costoDelPedido + cantidadDeSucursales * costoTransporte

    def aplicarDescuento(self):
        if isinstance(self._remitente, Cliente):
            membresia = self._remitente.getMembresia().getBeneficio()
            if membresia == "PLATINUM":
                self._precioTotal *= 0.5
            elif membresia == "GOLD":
                self._precioTotal *= 0.75
            elif membresia == "SILVER":
                self._precioTotal *= 0.9
            elif membresia == "DEFAULT":
                self._precioTotal *= 1

    def asignarRuta(self):
        from gestorAplicacion.transportes.camion import Camion
        from gestorAplicacion.transportes.avion import Avion
        if isinstance(self._vehiculo, Camion):
            sucursales = Sucursal.getTodasLasSucursales()  # La lista sería [Medellin, Cali, Pasto, Florencia, Bogotá]
            i = 0
            while i < len(sucursales):
                if sucursales[i] == self._sucursalOrigen:
                    if i < sucursales.index(self._sucursalLlegada):
                        for j in range(i, sucursales.index(self._sucursalLlegada) + 1):
                            self._ruta.append(sucursales[j])
                    else:
                        for j in range(i, len(sucursales)):
                            self._ruta.append(sucursales[j])
                        for k in range(0, sucursales.index(self._sucursalLlegada) + 1):
                            self._ruta.append(sucursales[k])
                i += 1

        elif isinstance(self.vehiculo, Avion):
            self.ruta.append(self._sucursalOrigen)
            self.ruta.append(self._sucursalLlegada)

    def __str__(self):
        format_str = "| {:<18} | {:<18} |"
        table = "--------------------GUIA-------------------\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Tipo de Producto", str(self._producto.__class__.__name__)) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Código Paquete", str(self._producto.getCodigo())) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Ciudad Origen", str(self._sucursalOrigen.getNombre())) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Ciudad Destino", str(self._sucursalLlegada.getNombre())) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Tipo de Pago", str(self._tipoDePago).lower()) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Precio Total", str(self._precioTotal) + "$") + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Vehículo", str(self._vehiculo.__class__.__name__)) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Fecha de envío", str(self._fechaDeEnvio)) + "\n"
        table += "+--------------------+--------------------+\n"
        return table

    def getVehiculo(self):
        return self._vehiculo

    def getTiempo(self):
        return self._tiempo

    def getProducto(self):
        return self._producto

    def getSucursalOrigen(self):
        return self._sucursalOrigen

    def getSucursalLlegada(self):
        return self._sucursalLlegada

    def getRuta(self):
        return self._ruta

    def getRemitente(self):
        return self._remitente

    def getDestinatario(self):
        return self._destinatario

    def getPagoPendiente(self):
        return self._pagoPendiente

    def getPrecioTotal(self):
        return self._precioTotal

    def getFecha(self):
        return self._fecha

    def getFechaDeEnvio(self):
        return self._fechaDeEnvio

    def getEstado(self):
        return self._estado

    def getTipoDePago(self):
        return self._tipoDePago

    def setVehiculo(self, vehiculo):
        self._vehiculo = vehiculo

    def setProducto(self, producto):
        self._producto = producto

    def setTiempo(self, tiempo):
        self._tiempo = tiempo

    def setSucursalOrigen(self, sucursalOrigen):
        self._sucursalOrigen = sucursalOrigen

    def setSucursalLlegada(self, sucursalLlegada):
        self._sucursalLlegada = sucursalLlegada

    def setRuta(self, ruta):
        self._ruta = ruta

    def setRemitente(self, remitente):
        self._remitente = remitente

    def setDestinatario(self, destinatario):
        self._destinatario = destinatario

    def setPrecioTotal(self, precioTotal):
        self._precioTotal = precioTotal

    def setPagoPendiente(self, pagoPendiente):
        self._pagoPendiente = pagoPendiente

    def setEstado(self, estado):
        self._estado = estado

    def setTipoDePago(self, tipoDePago):
        self._tipoDePago = tipoDePago

    @classmethod
    def getTodasLasGuias(cls):
        return cls._todasLasGuias

    @classmethod
    def setTodasLasGuias(cls, todasLasGuias):
        cls._todasLasGuias = todasLasGuias
