from datetime import datetime
#falta importar cosas
class Guia:
    class TipoDePago:
        REMITENTE = "REMITENTE"
        FRACCIONADO = "FRACCIONADO"
        DESTINATARIO = "DESTINATARIO"

    class Estado:
        ENSUCURSALORIGEN = "ENSUCURSALORIGEN"
        ENTRANSITO = "ENTRANSITO"
        ENESPERA = "ENESPERA"
        ENTREGADO = "ENTREGADO"

    todasLasGuias = []

    def __init__(self, producto, remitente, destinatario, sucursalOrigen, sucursalLlegada, tipoDePago, vehiculo):
        self.producto = producto
        self.remitente = remitente
        self.destinatario = destinatario
        self.sucursalOrigen = sucursalOrigen
        self.sucursalLlegada = sucursalLlegada
        self.tipoDePago = tipoDePago
        self.vehiculo = vehiculo
        producto.setGuia(self)
        Guia.todasLasGuias.append(self)
        self.estado = Guia.Estado.ENSUCURSALORIGEN

        self.fecha = datetime.now()
        fecha_formatter = "%d/%m/%y %H:%M"
        self.fechaDeEnvio = self.fecha.strftime(fecha_formatter)
        self.asignarRuta()
        self.asignarPrecio()
        self.aplicarDescuento()
        self.pagoPendiente = self.precioTotal

    def avancePedido(self):
        if self.estado == Guia.Estado.ENSUCURSALORIGEN:
            return 0
        elif self.estado == Guia.Estado.ENESPERA or self.estado == Guia.Estado.ENTREGADO:
            return 100
        elif self.estado == Guia.Estado.ENTRANSITO:
            porcentaje = 0
            if isinstance(self.vehiculo, Camion):
                escalas = 100.0 / (len(self.ruta) - 1)
                camion = self.vehiculo
                if camion.ubicacionActual is not None:
                    porcentaje = escalas * self.ruta.index(camion.ubicacionActual)
                    redondeado = round(porcentaje, 1)
                    return redondeado
                else:
                    porcentaje = (escalas * self.ruta.index(camion.ubicacionAnterior)) + (escalas / 2)
                    redondeado = round(porcentaje, 1)
                    return redondeado
            else:
                return 50
        else:
            return 0

    def asignarPrecio(self):
        cantidadDeSucursales = len(self.ruta) - 1
        costoTransporte = 0
        if isinstance(self.vehiculo, Camion):
            costoTransporte = 3000
        elif isinstance(self.vehiculo, Avion):
            costoTransporte = 7000
        self.precioTotal = self.producto.costoDelPedido + cantidadDeSucursales * costoTransporte

    def aplicarDescuento(self):
        if isinstance(self.remitente, Cliente):
            membresia = self.remitente.getMembresia().getBeneficio()
            if membresia == "PLATINUM":
                self.precioTotal *= 0.5
            elif membresia == "GOLD":
                self.precioTotal *= 0.75
            elif membresia == "SILVER":
                self.precioTotal *= 0.9
            elif membresia == "DEFAULT":
                self.precioTotal *= 1

    def asignarRuta(self):
        if isinstance(self.vehiculo, Camion):
            sucursales = Sucursal.getTodasLasSucursales()  # La lista sería [Medellin, Cali, Pasto, Florencia, Bogotá]
            i = 0
            while i < len(sucursales):
                if sucursales[i] == self.sucursalOrigen:
                    if i < sucursales.index(self.sucursalLlegada):
                        for j in range(i, sucursales.index(self.sucursalLlegada) + 1):
                            self.ruta.append(sucursales[j])
                    else:
                        for j in range(i, len(sucursales)):
                            self.ruta.append(sucursales[j])
                        for k in range(0, sucursales.index(self.sucursalLlegada) + 1):
                            self.ruta.append(sucursales[k])
                i += 1

        elif isinstance(self.vehiculo, Avion):
            self.ruta.append(self.sucursalOrigen)
            self.ruta.append(self.sucursalLlegada)

    def __str__(self):
        format_str = "| {:<18} | {:<18} |"
        table = "--------------------GUIA-------------------\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Tipo de Producto", str(self.producto.__class__.__name__)) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Código Paquete", str(self.producto.getCodigo())) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Ciudad Origen", str(self.sucursalOrigen.getNombre())) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Ciudad Destino", str(self.sucursalLlegada.getNombre())) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Tipo de Pago", str(self.tipoDePago).lower()) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Precio Total", str(self.precioTotal) + "$") + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Vehículo", str(self.vehiculo.__class__.__name)) + "\n"
        table += "+--------------------+--------------------+\n"
        table += format_str.format("Fecha de envío", str(self.fechaDeEnvio)) + "\n"
        table += "+--------------------+--------------------+\n"
        return table

    def getVehiculo(self):
        return self.vehiculo

    def getTiempo(self):
        return self.tiempo

    def getProducto(self):
        return self.producto

    def getSucursalOrigen(self):
        return self.sucursalOrigen

    def getSucursalLlegada(self):
        return self.sucursalLlegada

    def getRuta(self):
        return self.ruta

    def getRemitente(self):
        return self.remitente

    def getDestinatario(self):
        return self.destinatario

    def getPagoPendiente(self):
        return self.pagoPendiente

    def getPrecioTotal(self):
        return self.precioTotal

    def getFecha(self):
        return self.fecha

    def getFechaDeEnvio(self):
        return self.fechaDeEnvio

    def getEstado(self):
        return self.estado

    def getTipoDePago(self):
        return self.tipoDePago

    def setVehiculo(self, vehiculo):
        self.vehiculo = vehiculo

    def setProducto(self, producto):
        self.producto = producto

    def setTiempo(self, tiempo):
        self.tiempo = tiempo

    def setSucursalOrigen(self, sucursalOrigen):
        self.sucursalOrigen = sucursalOrigen

    def setSucursalLlegada(self, sucursalLlegada):
        self.sucursalLlegada = sucursalLlegada

    def setRuta(self, ruta):
        self.ruta = ruta

    def setRemitente(self, remitente):
        self.remitente = remitente

    def setDestinatario(self, destinatario):
        self.destinatario = destinatario

    def setPrecioTotal(self, precioTotal):
        self.precioTotal = precioTotal

    def setPagoPendiente(self, pagoPendiente):
        self.pagoPendiente = pagoPendiente

    def setEstado(self, estado):
        self.estado = estado

    def setTipoDePago(self, tipoDePago):
        self.tipoDePago = tipoDePago

    @classmethod
    def getTodasLasGuias(cls):
        return cls.todasLasGuias

    @classmethod
    def setTodasLasGuias(cls, todasLasGuias):
        cls.todasLasGuias = todasLasGuias
