import random
from gestorAplicacion import transportes, administracion

from main import seleccionSucursal, salirDelSistema, opcionesOpiniones, enviarPaquete, pagarServicio, rastrearPaquete, recogerPaquete

class Main:
    scanner = None  #chat

    @staticmethod
    def print(objeto):
        print(objeto, end='')

    @staticmethod
    def println(objeto):
        print(objeto)

    @staticmethod
    def main(args):
        sucursal = Sucursal.getTodasLasSucursales()[0]
        Main.menuPrincipal(sucursal)

    @staticmethod
    def seleccionSucursal():
        print("--- BIENVENIDO AL SISTEMA DE ENVIOS CORREMINAS ---")
        print("¿Desde qué ciudad se encuentra?")
        print("1) Medellín.")
        print("2) Cali.")
        print("3) Pasto")
        print("4) Bogotá.")
        seleccion = int(input("Elija una opción: "))

        numeroValido = False
        while not numeroValido:
            if seleccion == 1:
                print("1) Medellín Norte.")
                print("2) Medellín Sur.")
                ciudad = int(input("Elija una opción: "))
                numeroValido2 = False
                while not numeroValido2:
                    if ciudad == 1:
                        sucursal = Sucursal.getTodasLasSucursales()[0]
                        Main.menuPrincipal(sucursal)
                        numeroValido2 = True
                    elif ciudad == 2:
                        sucursal = Sucursal.getTodasLasSucursales()[1]
                        Main.menuPrincipal(sucursal)
                        numeroValido2 = True
            elif seleccion == 2:
                print("1) Cali Norte.")
                print("2) Cali Sur.")
                ciudad = int(input("Elija una opción: "))
                numeroValido3 = False
                while not numeroValido3:
                    if ciudad == 1:
                        sucursal = Sucursal.getTodasLasSucursales()[2]
                        Main.menuPrincipal(sucursal)
                        numeroValido3 = True
                    elif ciudad == 2:
                        sucursal = Sucursal.getTodasLasSucursales()[3]
                        Main.menuPrincipal(sucursal)
                        numeroValido3 = True
            elif seleccion == 3:
                print("1) Pasto Norte.")
                print("2) Pasto Sur.")
                ciudad = int(input("Elija una opción: "))
                numeroValido4 = False
                while not numeroValido4:
                    if ciudad == 1:
                        sucursal = Sucursal.getTodasLasSucursales()[4]
                        Main.menuPrincipal(sucursal)
                        numeroValido4 = True
                    elif ciudad == 2:
                        sucursal = Sucursal.getTodasLasSucursales()[5]
                        Main.menuPrincipal(sucursal)
                        numeroValido4 = True
            elif seleccion == 4:
                print("1) Bogotá Norte.")
                print("2) Bogotá Sur.")
                ciudad = int(input("Elija una opción: "))
                numeroValido5 = False
                while not numeroValido5:
                    if ciudad == 1:
                        sucursal = Sucursal.getTodasLasSucursales()[6]
                        Main.menuPrincipal(sucursal)
                        numeroValido5 = True
                    elif ciudad == 2:
                        sucursal = Sucursal.getTodasLasSucursales()[7]
                        Main.menuPrincipal(sucursal)
                        numeroValido5 = True
            else:
                print("Número no válido. Inténtalo de nuevo: ")
                numeroValido = True  # Esto evita un bucle infinito

    @staticmethod
    def menuPrincipal(sucursal):
        # Cada vez que se vuelva al menú principal se pasan los productos del inventario de la sucursal al de los vehículos
        camionesFuera = []  # Esto es para eliminar los camiones que salieron de la lista de la sucursal
        avionesFuera = []  # Eliminar los aviones que salieron de la lista de la sucursal

        for camion in sucursal.getCamionesEnSucursal():
            camion.agregarProductos()
            if camion.getUbicacionActual() == sucursal:
                if len(camion.getInventario()) >= 3:  # Si un camión de la sucursal tiene 3 productos o más, comienza el recorrido
                    camion.iniciarRecorrido()
                    camionesFuera.append(camion)
            else:
                camionesFuera.append(camion)  # Evitar error de duplicación

        for camion in camionesFuera:
            sucursal.getCamionesEnSucursal().remove(camion)

        for avion in sucursal.getAvionesEnSucursal():
            avion.agregarProductos()
            if avion.getUbicacionActual() == sucursal:
                if len(avion.getInventario()) == 5:
                    avion.iniciarRecorrido()
                    avionesFuera.append(avion)
                    Main.println("avion")

        Main.println(f"--- BIENVENIDO AL SISTEMA DE ENVIOS CORREMINAS SEDE {sucursal.getNombre().upper()}---")  # Colocar la sede en la que está
        Main.println("¿Qué operación deseas realizar?")
        Main.println("1) Enviar paquete")
        Main.println("2) Pagar servicio")
        Main.println("3) Rastrear paquete")
        Main.println("4) Recoger paquete")
        Main.println("5) Opiniones")
        Main.println("6) Cambiar Sucursal")
        Main.println("7) Terminar")
        Main.print("Elige una opción: ")

        numeroValido = False
        while not numeroValido:
            opcion = int(input())
            if opcion == 1:
                enviarPaquete(sucursal)
                numeroValido = True
            elif opcion == 2:
                pagarServicio(sucursal)
                numeroValido = True
            elif opcion == 3:
                rastrearPaquete(sucursal)
            elif opcion == 4:
                recogerPaquete(sucursal)
                numeroValido = True
            elif opcion == 5:
                opcionesOpiniones()
                numeroValido = True
            elif opcion == 6:
                Main.seleccionSucursal()
                numeroValido = True
            elif opcion == 7:
                salirDelSistema()
                numeroValido = True
            else:
                Main.print("Número no válido. Inténtalo de nuevo: ")

if __name__ == "__main__":
    Main.scanner = None
    Main.main(None)





#funcionalidad de recoger paquete - KEVIN
  @staticmethod
    def recogerPaquete(sucursal):
        print("-----------------RECOGER PRODUCTO----------------")
        codigoPaquete = int(input("Ingrese el código de la guía: "))
        nombreDestinatario = input("Ingrese su nombre: ")
        cedulaDestinatario = int(input("Ingrese su cédula: "))

        producto = Main.encontrarProductoPorCodigo(codigoPaquete)

        if producto:
            guia = producto.getGuia()
            if Main.verificarDatos(producto, cedulaDestinatario):
                if guia.getSucursalLlegada() == sucursal:
                    if producto in sucursal.getInventario() and guia.getEstado() != Guia.estado.ENTREGADO:
                        if guia.getTipoDePago() == Guia.tipoDePago.REMITENTE:
                            random.seed()
                            fechaEntrega = datetime.now()
                            print("\n************************************* *")
                            print("*  Operación realizada con éxito     *")
                            print("*  Favor acercarse a la caja No. " + str(random.randint(0, 4)) + "  *")
                            print("*  para retirar su paquete.          *")
                            print("*  ¡Muchas gracias por usar nuestro  *")
                            print("*  servicio!                         *")
                            print("**************************************")
                            guia.setEstado(Guia.estado.ENTREGADO)
                            sucursal.getInventario().remove(producto)
                            print("\n1) Volver al menú principal: ")
                            numeroValido = False
                            while not numeroValido:
                                menuPrincipalEntrada = int(input())
                                if menuPrincipalEntrada == 1:
                                    menuPrincipal(sucursal)
                                    numeroValido = True
                                else:
                                    print("Número no válido. Inténtalo de nuevo: ")
                        else:
                            if guia.getPagoPendiente() != 0:
                                print("-------------------------------------------------")
                                print("Para poder recoger este paquete debes pagar la deuda pendiente asociada a este.")
                                print("¿Desea pagar el envío?")
                                print("1) Sí")
                                print("2) Volver al menú principal")
                                confirmaPago = int(input("Elige una opción: "))
                                numeroValido1 = False
                                while not numeroValido1:
                                    if confirmaPago == 1:
                                        Main.pagarServicio(sucursal, guia)
                                    elif confirmaPago == 2:
                                        menuPrincipal(sucursal)
                                    else:
                                        print("Número no válido. Inténtalo de nuevo: ")
                            else:
                                random.seed()
                                fechaEntrega = datetime.now()
                                print("\n************************************* *")
                                print("*  Operación realizada con éxito     *")
                                print("*  Favor acercarse a la caja No. " + str(random.randint(0, 4)) + "  *")
                                print("*  para retirar su paquete.          *")
                                print("*  ¡Muchas gracias por usar nuestro  *")
                                print("*  servicio!                         *")
                                print("**************************************")
                                guia.setEstado(Guia.estado.ENTREGADO)
                                sucursal.getInventario().remove(producto)
                                print("\n1) Volver al menú principal: ")
                                numeroValido = False
                                while not numeroValido:
                                    menuPrincipalEntrada = int(input())
                                    if menuPrincipalEntrada == 1:
                                        menuPrincipal(sucursal)
                                        numeroValido = True
                                    else:
                                        print("Número no válido. Inténtalo de nuevo: ")
                    else:
                        if guia.getEstado() == Guia.estado.ENTREGADO:
                            print("-------------------------------------------------")
                            print("El paquete que busca ya fue entregado.")
                            print("\n1) Volver al menú principal: ")
                            numeroValido = False
                            while not numeroValido:
                                menuPrincipalEntrada = int(input())
                                if menuPrincipalEntrada == 1:
                                    menuPrincipal(sucursal)
                                    numeroValido = True
                                else:
                                    print("Número no válido. Inténtalo de nuevo: ")
                        else:
                            print("-------------------------------------------------")
                            print("El envío no ha llegado")
                            print("¿Desea rastrear el envío?")
                            print("1) Sí")
                            print("2) Volver al menú principal")
                            entrada = int(input("Elige una opción: "))
                            numeroValido = False
                            while not numeroValido:
                                if entrada == 1:
                                    rastrearPaquete(sucursal)
                                    numeroValido = True
                                elif entrada == 2:
                                    menuPrincipal(sucursal)
                                    numeroValido = True
                                else:
                                    print("Número no válido. Inténtalo de nuevo: ")
                else:
                    print("-------------------------------------------------")
                    print("EL envío tiene como destino la sucursal de " + guia.getSucursalLlegada().getNombre())
                    print("¿Desea rastrear el envío?")
                    print("1) Sí")
                    print("2) Volver al menú principal")
                    entrada = int(input("Elige una opción: "))
                    numeroValido = False
                    while not numeroValido:
                        if entrada == 1:
                            rastrearPaquete(sucursal)
                            numeroValido = True
                        elif entrada == 2:
                            menuPrincipal(sucursal)
                            numeroValido = True
                        else:
                            print("Número no válido. Inténtalo de nuevo: ")
            else:
                print("-------------------------------------------------")
                print("Los datos ingresados no corresponden con los del remitente.")
                print("\n1) Volver al menú principal: ")
                numeroValido = False
                while not numeroValido:
                    menuPrincipalEntrada = int(input())
                    if menuPrincipalEntrada == 1:
                        menuPrincipal(sucursal)
                        numeroValido = True
                    else:
                        print("Número no válido. Inténtalo de nuevo: ")
        else:
            print("-------------------------------------------------")
            print("El paquete que intenta buscar no existe.")
            print("\n1) Volver al menú principal: ")
            numeroValido = False
            while not numeroValido:
                menuPrincipalEntrada = int(input())
                if menuPrincipalEntrada == 1:
                    menuPrincipal(sucursal)
                    numeroValido = True
                else:
                    print("Número no válido. Inténtalo de nuevo: ")

        if guia.getEstado() == Guia.estado.ENTREGADO:
            if producto in sucursal.getInventario():
                sucursal.getInventario().remove(producto)

    @staticmethod
    def encontrarProductoPorCodigo(codigo):
        for producto in Producto.getTodosLosProductos():
            if producto.getCodigo() == codigo:
                return producto
        return None

    @staticmethod
    def verificarDatos(producto, cedulaDestinatario):
        guia = producto.getGuia()
        destinatario = guia.getDestinatario()
        if int(destinatario.getCedula()) == cedulaDestinatario:
            return True
        return False
