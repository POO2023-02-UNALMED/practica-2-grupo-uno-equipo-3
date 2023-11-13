from productos.producto import Producto

class Documento(Producto):
    def __init__(self):
        super().__init__(self.generar_codigo(), 0.1, 0.1)

    def __str__(self):
        return "---------------------PRODUCTO--------------------\n" + \
               "Tipo de producto: Documento\n" + \
               "Codigo de pedido: " + str(self.codigo)

    def asignar_costo_del_pedido(self):
        self.costo_del_pedido = 10000