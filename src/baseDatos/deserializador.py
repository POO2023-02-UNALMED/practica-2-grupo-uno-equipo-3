import pickle
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.productos.producto import Producto
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
from gestorAplicacion.transportes.transporte import Transporte


class Deserializador:

    @staticmethod
    def deserializarSucursales():
            with open("../baseDatos/temp/Sucursales.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            Sucursal.setTodasLasSucursales(lista_objetos)

    @staticmethod
    def deserializarOpiniones():
            with open("../baseDatos/temp/Opiniones.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            Opinion.setTodasLasOpiniones(lista_objetos)

    @staticmethod
    def deserializarTransportes():
            with open("../baseDatos/temp/Transportes.pkl", 'rb') as file:
                  lista_objetos = pickle.load(file)
            Transporte.setTodosLosTransportes(lista_objetos)

    @staticmethod
    def deserializarCuentasBancarias():
            with open("../baseDatos/temp/CuentaBancarias.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            CuentaBancaria.setTodasLasCuentasBancarias(lista_objetos)

    @staticmethod
    def deserializarProductos():
            with open("../baseDatos/temp/Productos.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            Producto.setTodosLosProductos(lista_objetos)

    @staticmethod
    def deserializarGuias():
            with open("../baseDatos/temp/Guias.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            Guia.setTodasLasGuias(lista_objetos)

    @staticmethod
    def deserializarPersonas():
            with open("../baseDatos/temp/Personas.pkl", 'rb') as file:
                lista_objetos = pickle.load(file)
            Persona.setTodasLasPersonas(lista_objetos)