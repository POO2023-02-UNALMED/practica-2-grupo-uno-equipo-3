import pickle
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.administracion.opinion import Opinion
from gestorAplicacion.personas.persona import Persona
from gestorAplicacion.productos.producto import Producto
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.administracion.cuentaBancaria import CuentaBancaria
from gestorAplicacion.transportes.transporte import Transporte


class Deserializador:

    @classmethod
    def deserializarSucursales(cls):
            with open('src\\baseDatos\\temp\\Sucursales.pkl', 'rb') as file:
                lista_objetos = pickle.load(file)
            Sucursal.setTodasLasSucursales(lista_objetos)

    @classmethod
    def deserializarOpiniones(cls):
            with open('src\\baseDatos\\temp\\Opiniones.pkl', 'rb') as file:
                lista_objetos = pickle.load(file)
            Opinion.setTodasLasOpiniones(lista_objetos)

    @classmethod
    def deserializarTransportes(cls):
            with open('src\\baseDatos\\temp\\Transportes.pkl', 'rb') as file:
                  lista_objetos = pickle.load(file)
            Transporte.setTodosLosTransportes(lista_objetos)

    @classmethod
    def deserializarCuentasBancarias(cls):
            with open('src\\baseDatos\\temp\\CuentaBancarias.pkl', 'rb') as file:
                lista_objetos = pickle.load(file)
            CuentaBancaria.setTodasLasCuentasBancarias(lista_objetos)

    @classmethod
    def deserializarProductos(cls):
            with open('src\\baseDatos\\temp\\Productos.pkl', 'rb') as file:
                lista_objetos = pickle.load(file)
            Producto.setTodosLosProductos(lista_objetos)

    @classmethod
    def deserializarGuias(cls):
            with open('src\\baseDatos\\temp\\Guias.pkl', 'rb') as file:
                lista_objetos = pickle.load(file)
            Guia.setTodasLasGuias(lista_objetos)

    @classmethod
    def deserializarPersonas(cls):
            with open('src\\baseDatos\\temp\\Personas.pkl', 'rb') as file:
                lista_objetos = pickle.load(file)
            Persona.setTodasLasPersonas(lista_objetos)
    
    @classmethod
    def deserializar(cls):
          Deserializador.deserializarCuentasBancarias()
          Deserializador.deserializarGuias()
          Deserializador.deserializarOpiniones()
          Deserializador.deserializarPersonas()
          Deserializador.deserializarProductos()
          Deserializador.deserializarSucursales()
          Deserializador.deserializarTransportes()