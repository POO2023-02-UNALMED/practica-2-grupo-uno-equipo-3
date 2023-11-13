from productos.producto import Producto

class Paquete(Producto):
    def __init__(self, peso, alto, ancho, largo, fragil, valor_declarado):
        codigo = self.generar_codigo()
        volumen = alto * largo * ancho
        super().__init__(codigo, volumen, peso)
        self.valor_declarado = valor_declarado
        self.peso = peso
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        self.fragil = fragil
        self.volumen = alto * largo * ancho
        self.roto = False

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

    def asignar_costo_del_pedido(self):
        tarifa_base_por_kg = 1000
        tarifa_base_por_metro_cubico = 4000
        tarifa_adicional_fragil = 1.25
        costo_pedido = (tarifa_base_por_metro_cubico * self.volumen) + (tarifa_base_por_kg * self.peso) + self.valor_declarado * 0.3
        if not self.fragil:
            self.costo_del_pedido = costo_pedido
        else:
            self.costo_del_pedido = costo_pedido * tarifa_adicional_fragil

    def is_fragil(self):
        return self.fragil

    def get_valor_declarado(self):
        return self.valor_declarado

    def is_roto(self):
        return self.roto

    def set_roto(self, roto):
        self.roto = roto