import pickle
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion

class Deserializador:

    @staticmethod
    def deserializarSucursales():
            with open("../baseDatos/temp/sucursales.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            Sucursal.setTodasLasSucursales(lista_objetos)


