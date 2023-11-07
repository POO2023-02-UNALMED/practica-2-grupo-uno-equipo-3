import pickle
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion

class Serializador:

    @classmethod
    def serializarSucursales(cls, lista_objetos):
        with open("../baseDatos/temp/sucursales.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)

    @classmethod
    def serializarOpiniones(cls, lista_objetos):
        with open("../baseDatos/temp/Opiniones.pkl", 'wb') as file:
            pickle.dump(lista_objetos, file)    


