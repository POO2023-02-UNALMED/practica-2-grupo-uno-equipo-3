from productos.producto import Producto

class Paquete(Producto):
    def __init__(self, peso, alto, ancho, largo, fragil, valorDeclarado):
        _volumen = _alto * _largo * _ancho
        super().__init__(Producto.generarCodigo(), volumen, peso)
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
               "Código de pedido: " + str(self.codigo) + "\n" + \
               "Peso: " + str(self.peso) + "kg\n" + \
               "Altura: " + str(self.alto) + "m\n" + \
               "Ancho: " + str(self.ancho) + "m\n" + \
               "Largo: " + str(self.largo) + "m\n" + \
               "Volumen: " + str(self.alto * self.ancho * self.largo) + "m3\n" + \
               "Fragil: " + ("Sí" if self.fragil else "No") + "\n" + \
               "Valor declarado: " + str(self.valor_declarado)

    def asignarCostoDelPedido(self):
        tarifa_base_por_kg = 1000
        tarifa_base_por_metro_cubico = 4000
        tarifa_adicional_fragil = 1.25
        costo_pedido = (tarifa_base_por_metro_cubico * self.volumen) + (tarifa_base_por_kg * self.peso) + self.valor_declarado * 0.3
        if not self.fragil:
            self.costoDelPedido = costo_pedido
        else:
            self.costoDelPedido = costo_pedido * tarifa_adicional_fragil

    def isFragil(self):
        return self._fragil

    def getValorDeclarado(self):
        return self._valorDeclarado

    def isRoto(self):
        return self._roto

    def setRoto(self, roto):
        self._roto = roto