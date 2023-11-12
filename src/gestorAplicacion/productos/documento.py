import random

class Producto:
    contador_productos = 0

    def __init__(self, codigo, volumen, peso):
        self.codigo = codigo
        self.volumen = volumen
        self.peso = peso
        self.costo_del_pedido = 0  # Este no es el costo definitivo del producto

    @classmethod
    def generar_codigo(cls):
        codigo_aleatorio = random.randint(10000, 99999)
        return codigo_aleatorio

    def asignar_costo_del_pedido(self):
        pass

class Documento(Producto):
    def __init__(self):
        codigo = self.generar_codigo()
        super().__init__(codigo, 0.1, 0.1)

    def asignar_costo_del_pedido(self):
        self.costo_del_pedido = 10000

    def __str__(self):
        return "---------------------PRODUCTO--------------------\n" + \
               "Tipo de producto: Documento\n" + \
               f"Codigo de pedido: {self.codigo}"

if __name__ == "__main__":
    documento = Documento()
    documento.asignar_costo_del_pedido()
    print(documento)