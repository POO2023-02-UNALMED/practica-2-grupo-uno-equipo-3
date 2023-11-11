import pickle

from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.productos.producto import Producto
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
from gestorAplicacion.transportes.transporte import Transporte


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
    
    @classmethod
    def serializar():
        Serializador.serializarCuentaBancarias(CuentaBancaria.getTodasLasCuentasBancarias())
        Serializador.serializarGuias(Guia.getTodasLasGuias())
        Serializador.serializarPersonas(Persona.getTodasLasPersonas())
        Serializador.serializarTransportes(Transporte.getTodasLosTransportes())
        Serializador.serializarOpiniones(Opinion.getTodasLasOpiniones())
        Serializador.serializarProductos(Producto.getTodosLosProductos())
        Serializador.serializarSucursales(Sucursal.getTodasLasSucursales())