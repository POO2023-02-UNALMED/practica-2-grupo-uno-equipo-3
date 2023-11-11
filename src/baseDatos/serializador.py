import pickle


class Serializador:

    @classmethod
    def serializarSucursales(cls, lista_objetos):
        with open("../baseDatos/temp/Sucursales.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)

    @classmethod
    def serializarOpiniones(cls, lista_objetos):
        with open("../baseDatos/temp/Opiniones.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)    

    @classmethod
    def serializarTransportes(cls, lista_objetos):
        with open("../baseDatos/temp/Transportes.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)

    @classmethod
    def serializarCuentaBancarias(cls, lista_objetos):
        with open("../baseDatos/temp/CuentaBancarias.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)

    @classmethod
    def serializarProductos(cls, lista_objetos):
        with open("../baseDatos/temp/Productos.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)    

    @classmethod
    def serializarGuias(cls, lista_objetos):
        with open("../baseDatos/temp/Guias.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)

    @classmethod
    def serializarPersonas(cls, lista_objetos):
        with open("../baseDatos/temp/Personas.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)