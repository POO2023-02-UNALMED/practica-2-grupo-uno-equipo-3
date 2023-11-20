from gestorAplicacion.productos.producto import Producto

class Paquete(Producto):
    def __init__(self, peso, alto, ancho, largo, fragil, valorDeclarado):
        _volumen = alto * largo * ancho
        super().__init__(Producto.generarCodigo(), _volumen, peso)
        self._valorDeclarado = valorDeclarado
        self._peso = peso
        self._alto = alto
        self._ancho = ancho
        self._largo = largo
        self._fragil = fragil
        self._volumen = alto * largo * ancho
        self._roto = False

    def __str__(self):
        return "---------------------PRODUCTO--------------------\n" + \
               "Tipo de producto: Paquete\n" + \
               "Código de pedido: " + str(self._codigo) + "\n" + \
               "Peso: " + str(self._peso) + "kg\n" + \
               "Altura: " + str(self._alto) + "m\n" + \
               "Ancho: " + str(self._ancho) + "m\n" + \
               "Largo: " + str(self._largo) + "m\n" + \
               "Volumen: " + str(self._alto * self._ancho * self._largo) + "m3\n" + \
               "Fragil: " + ("Sí" if self._fragil else "No") + "\n" + \
               "Valor declarado: " + str(self._valorDeclarado)

    def asignarCostoDelPedido(self):
        tarifa_base_por_kg = 1000
        tarifa_base_por_metro_cubico = 4000
        tarifa_adicional_fragil = 1.25
        costo_pedido = (tarifa_base_por_metro_cubico * self._volumen) + (tarifa_base_por_kg * self._peso) + self._valorDeclarado * 0.3
        if not self._fragil:
            self.costoDelPedido = costo_pedido
        else:
            self.costoDelPedido = costo_pedido * tarifa_adicional_fragil

    def isFragil(self):
        return self._fragil
    
    def getCodigo(self):
        return self._codigo

    def getValorDeclarado(self):
        return self._valorDeclarado

    def isRoto(self):
        return self._roto

    def setRoto(self, roto):
        self._roto = roto