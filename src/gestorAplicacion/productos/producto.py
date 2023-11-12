import random

class Producto:
    contador_productos = 0
    todos_los_productos = []

    def __init__(self, codigo, volumen, peso):
        self.codigo = codigo
        self.peso = peso
        self.volumen = volumen
        self.costo_del_pedido = 0  # Este no es el costo definitivo del producto
        self.guia = None

        Producto.todos_los_productos.append(self)
        Producto.contador_productos += 1
        self.asignar_costo_del_pedido()

    def __str__(self):
        return "Código: {}, Peso: {}, Volumen: {}, Costo del Pedido: {}".format(
            self.codigo, self.peso, self.volumen, self.costo_del_pedido
        )

    def asignar_costo_del_pedido(self):
        pass  # Implementa la lógica para asignar el costo del pedido en las clases derivadas

    @classmethod
    def generar_codigo(cls):
        codigo_aleatorio = random.randint(10000, 99999)
        return codigo_aleatorio

    # Getters y setters
    def get_peso(self):
        return self.peso

    def get_codigo(self):
        return self.codigo

    def get_volumen(self):
        return self.volumen

    def get_costo_del_pedido(self):
        return self.costo_del_pedido

    def get_guia(self):
        return self.guia

    @classmethod
    def get_contador_productos(cls):
        return cls.contador_productos

    @classmethod
    def get_todos_los_productos(cls):
        return cls.todos_los_productos

    def set_peso(self, peso):
        self.peso = peso

    def set_volumen(self, volumen):
        self.volumen = volumen

    def set_costo_del_pedido(self, costo_del_pedido):
        self.costo_del_pedido = costo_del_pedido

    def set_guia(self, guia):
        self.guia = guia

    @classmethod
    def set_todos_los_productos(cls, todos_los_productos):
        cls.todos_los_productos = todos_los_productos

class ProductoAnimal(Producto):
    def __init__(self, codigo, volumen, peso, nombre_animal, edad_animal, tipo_animal):
        super().__init__(codigo, volumen, peso)
        self.nombre_animal = nombre_animal
        self.edad_animal = edad_animal
        self.tipo_animal = tipo_animal

    def __str__(self):
        return super().__str() + ", Nombre del Animal: {}, Edad del Animal: {}, Tipo del Animal: {}".format(
            self.nombre_animal, self.edad_animal, self.tipo_animal
        )

    def asignar_costo_del_pedido(self):
        pass  # Implementa la lógica para asignar el costo del pedido específica para ProductoAnimal

class ProductoProducto(Producto):
    def __init__(self, codigo, volumen, peso, fragilidad, valor_declarado, altura_paquete, ancho_paquete, largo_paquete, instrucciones_especiales):
        super().__init__(codigo, volumen, peso)
        self.fragilidad = fragilidad
        self.valor_declarado = valor_declarado
        self.altura_paquete = altura_paquete
        self.ancho_paquete = ancho_paquete
        self.largo_paquete = largo_paquete
        self.instrucciones_especiales = instrucciones_especiales

    def __str__(self):
        return super().__str() + ", Fragilidad: {}, Valor Declarado: {}, Altura: {}, Ancho: {}, Largo: {}, Instrucciones Especiales: {}".format(
            self.fragilidad, self.valor_declarado, self.altura_paquete, self.ancho_paquete, self.largo_paquete, self.instrucciones_especiales
        )

    def asignar_costo_del_pedido(self):
        pass  # Implementa la lógica para asignar el costo del pedido específica para ProductoProducto