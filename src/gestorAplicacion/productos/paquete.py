import random

class Producto:
    contador_productos = 0

    def __init__(self, codigo, peso, volumen=0):
        self.codigo = codigo
        self.peso = peso
        self.volumen = volumen
        self.costo_del_pedido = 0

        Producto.contador_productos += 1

    def asignar_costo_del_pedido(self):
        pass

class Paquete(Producto):
    def __init__(self, peso, alto, ancho, largo, fragil, valor_declarado):
        codigo = Paquete.generar_codigo()
        volumen = alto * ancho * largo
        super().__init__(codigo, peso, volumen)
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        self.fragil = fragil
        self.valor_declarado = valor_declarado
        self.roto = False

    @staticmethod
    def generar_codigo():
        return random.randint(10000, 99999)

    def asignar_costo_del_pedido(self):
        tarifa_base_por_kg = 1000
        tarifa_base_por_metro_cubico = 4000
        tarifa_adicional_fragil = 1.25

        costo_pedido = (tarifa_base_por_metro_cubico * self.volumen) + (tarifa_base_por_kg * self.peso) + self.valor_declarado * 0.3

        if not self.fragil:
            self.costo_del_pedido = costo_pedido
        else:
            self.costo_del_pedido = costo_pedido * tarifa_adicional_fragil

    def __str__(self):
        return f"---------------------PRODUCTO--------------------\n" \
               f"Tipo de producto: Paquete\n" \
               f"Código de pedido: {self.codigo}\n" \
               f"Peso: {self.peso} kg\n" \
               f"Altura: {self.alto} m\n" \
               f"Ancho: {self.ancho} m\n" \
               f"Largo: {self.largo} m\n" \
               f"Volumen: {self.volumen} m^3\n" \
               f"Fragil: {'Sí' if self.fragil else 'No'}\n" \
               f"Valor declarado: {self.valor_declarado}"

paquete = Paquete(5, 0.5, 0.3, 0.4, True, 100)
paquete.asignar_costo_del_pedido()
print(paquete)
print(f"Costo del pedido: {paquete.costo_del_pedido}")