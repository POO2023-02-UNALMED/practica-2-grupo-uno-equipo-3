from gestorAplicacion.productos.producto import Producto

class Documento(Producto):
    def __init__(self):
        super().__init__(Producto.generarCodigo(), 0.1, 0.1)

    def __str__(self):
        return "---------------------PRODUCTO--------------------\n" + \
               "Tipo de producto: Documento\n" + \
               "Codigo de pedido: " + str(self._codigo)

    def asignarCostoDelPedido(self):
        self._costoDelPedido = 10000