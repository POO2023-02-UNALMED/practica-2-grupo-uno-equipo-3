import random

class Producto:
    contador_productos = 0  

    def __init__(self, codigo, volumen, peso):
        self.codigo = codigo
        self.peso = peso
        self.volumen = volumen
        self.costo_del_pedido = 0.0  
        self.guia = None  

        Producto.contador_productos += 1
        self.asignar_costo_del_pedido()

    @classmethod
    def generar_codigo(cls):
        return random.randint(10000, 99999)

    def asignar_costo_del_pedido(self):
        pass

    def __str__(self):
        return ""

    def set_peso(self, peso):
        self.peso = peso

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_costo_del_pedido(self, costo_del_pedido):
        self.costo_del_pedido = costo_del_pedido

    def set_guia(self, guia):
        self.guia = guia

    @property
    def costo_del_pedido(self):
        return self.costo_del_pedido

    @property
    def codigo(self):
        return self.codigo

    @property
    def peso(self):
        return self.peso

    @property
    def volumen(self):
        return self.volumen

    @property
    def guia(self):
        return self.guia

    @classmethod
    def contador_productos(cls):
        return cls.contador_productos

    @classmethod
    def todos_los_productos(cls):
        return [] 

    @classmethod
    def set_todos_los_productos(cls, productos):
        pass