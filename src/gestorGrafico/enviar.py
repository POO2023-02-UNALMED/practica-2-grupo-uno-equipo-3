import tkinter as tk
from tkinter import *

class Enviar(Frame):
    pass

# 361 - 886
#  public static void enviarPaquete(Sucursal sucursalOrigen) {
#         Scanner scanner = new Scanner(System.in);
#         boolean exit = false;

#         println("---------------DATOS DEL PRODUCTO----------------");
#         println("Ingrese el tipo de producto:");
#         println("1) Paquete");
#         println("2) Animal");
#         println("3) Documento");
#         println("4) Volver al menú");
#         print("Elige una opción: ");


#         Producto producto = null;
#         boolean numeroValido = false;

#         while (!numeroValido) {
#             int tipoDeProducto = scanner.nextInt();
#             scanner.nextLine();

#             switch (tipoDeProducto) {
#                 case 1: //Paquete
#                     println("-------------------------------------------------");
#                     print("Peso del paquete: ");
#                     double peso = scanner.nextDouble();
#                     print("Alto del paquete: ");
#                     double alto = scanner.nextDouble();
#                     print("Ancho del paquete: ");
#                     double ancho = scanner.nextDouble();
#                     print("Largo del paquete: ");
#                     double largo = scanner.nextDouble();

#                     println("-------------------------------------------------");
#                     println("¿El paquete es fragil?");
#                     println("1) Sí");
#                     println("2) No");
#                     print("Elige una opcion: ");

#                     boolean numeroValido2 = false;
#                     boolean fragil = false;

#                     while (!numeroValido2) {
#                         int fragilEntrada = scanner.nextInt();
#                         switch (fragilEntrada) {
#                             case 1:
#                                 fragil = true;
#                                 numeroValido2 = true;
#                                 break;
#                             case 2:
#                                 fragil = false;
#                                 numeroValido2 = true;
#                                 break;
#                             default:
#                                 print("Número no válido. Inténtalo de nuevo: ");
#                         }
#                     }
#                     println("-------------------------------------------------");
#                     print("Valor declarado: ");
#                     double valorDeclarado = scanner.nextDouble();
#                     scanner.nextLine();

#                     producto = new Paquete(peso, alto, ancho, largo, fragil, valorDeclarado);
#                     Paquete paquete = (Paquete) producto;
#                     println(producto);
#                     numeroValido = true;
#                     break;

#                 case 2: //Animal
#                     println("-------------------------------------------------");
#                     print("Nombre del animal: ");
#                     String nombre = scanner.nextLine();
#                     print("Edad del animal: ");
#                     int edad = scanner.nextInt();
#                     print("Peso del animal: ");
#                     double peso1 = scanner.nextDouble();

#                     println("-------------------------------------------------");
#                     println("Ingrese el tipo del animal:");
#                     println("1) Perro");
#                     println("2) Gato");
#                     println("3) Hamster");
#                     println("4) Loro");
#                     println("5) Caballo");
#                     println("6) Vaca");
#                     print("Elige una opción: ");

#                     tipoAnimal tipoAnimal = null;
#                     boolean numeroValido3 = false;

#                     while (!numeroValido3) {
#                         int tipoAnimalEntrada = scanner.nextInt();
#                         scanner.nextLine();

#                         switch (tipoAnimalEntrada) {
#                             case 1: //Perro
#                                 tipoAnimal = Animal.tipoAnimal.PERRO;
#                                 numeroValido3 = true;
#                                 break;
#                             case 2:
#                                 tipoAnimal = Animal.tipoAnimal.GATO;
#                                 numeroValido3 = true;
#                                 break;
#                             case 3:
#                                 tipoAnimal = Animal.tipoAnimal.HAMSTER;
#                                 numeroValido3 = true;
#                                 break;
#                             case 4:
#                                 tipoAnimal = Animal.tipoAnimal.LORO;
#                                 numeroValido3 = true;
#                                 break;
#                             case 5:
#                                 tipoAnimal = Animal.tipoAnimal.CABALLO;
#                                 numeroValido3 = true;
#                                 break;
#                             case 6:
#                                 tipoAnimal = Animal.tipoAnimal.VACA;
#                                 numeroValido3 = true;
#                                 break;
#                             default:
#                                 print("Número no válido. Inténtalo de nuevo: ");
#                         }
#                     }

#                     producto = new Animal(nombre, edad, peso1, tipoAnimal);
#                     Animal animal = (Animal) producto;
#                     println(animal);
#                     numeroValido = true;
#                     break;
#                 case 3:
#                     producto = new Documento();
#                     Documento documento = (Documento) producto;
#                     numeroValido = true;
#                     break;
#                 case 4:
#                     Main.menuPrincipal(sucursalOrigen);

#                 default:
#                     print("Número no válido. Inténtalo de nuevo: ");
#                     break;
#             }
###         }


#         println("----------------DATOS DEL USUARIO----------------");

#         print("Nombre del remitente: ");
#         String nombreRemitente = scanner.nextLine();
#         print("Cédula del remitente: ");
#         long cedulaRemitente = scanner.nextLong();
#         print("Telefono del remitente: ");
#         long telefonoRemitente = scanner.nextLong();
#         scanner.nextLine();

#         Cliente remitente = new Cliente(nombreRemitente, cedulaRemitente, telefonoRemitente);

#         println("-------------------------------------------------");
#         print("Nombre del destinatario: ");
#         String nombreDestinatario = scanner.nextLine();
#         print("Cédula del destinatario: ");
#         long cedulaDestinatario = scanner.nextLong();
#         print("Telefono del destinatario: ");
#         long telefonoDestinatario = scanner.nextLong();

#         Destinatario destinatario = new Destinatario(nombreDestinatario, cedulaDestinatario, telefonoDestinatario);

#         String[] palabra = sucursalOrigen.getNombre().split(" ");
#         println("------------------DATOS DE ENVÍO-----------------");

#         println("Ciudad de origen: " + sucursalOrigen.getCiudad());
#         println("Sucursal: " + palabra[1]);

#         ArrayList<Sucursal> ciudadesDestino = new ArrayList<>();

#         for (Sucursal sucursal : Sucursal.getTodasLasSucursales()) {
#             if (!Objects.equals(sucursal.getCiudad(), sucursalOrigen.getCiudad())) {
#                 ciudadesDestino.add(sucursal);
#             }
#         }

#         String ciudades = String.format("Seleccione la ciudad de destino: \n" +
#                 "1) %s\n" +
#                 "2) %s\n" +
#                 "3) %s", ciudadesDestino.get(0).getCiudad(), ciudadesDestino.get(2).getCiudad(), ciudadesDestino.get(4).getCiudad());

#         println("-------------------------------------------------");
#         println(ciudades);
#         print("Elige una opción: ");

#         Sucursal sucursalDestino = null;
#         boolean numeroValido4 = false;

#         while (!numeroValido4) {
#             int destinoEntrada = scanner.nextInt();

#             switch (destinoEntrada) {
#                 case 1:
#                     String sucursales = String.format("Seleccione la Sucursal de preferencia:\n" +
#                             "1) %s\n" +
#                             "2) %s", ciudadesDestino.get(0).getNombre(), ciudadesDestino.get(1).getNombre());

#                     println("-------------------------------------------------");
#                     println(sucursales);
#                     print("Elige una opción: ");

#                     boolean numeroValido5 = false;

#                     while (!numeroValido5) {
#                         int sucursalEntrada = scanner.nextInt();

#                         switch (sucursalEntrada) {
#                             case 1:
#                                 sucursalDestino = ciudadesDestino.get(0);
#                                 numeroValido5 = true;
#                                 break;
#                             case 2:
#                                 sucursalDestino = ciudadesDestino.get(1);
#                                 numeroValido5 = true;
#                                 break;
#                             default:
#                                 print("Número no válido. Inténtalo de nuevo: ");
#                         }
#                     }
#                     numeroValido4 = true;
#                     break;
#                 case 2:
#                     String sucursales1 = String.format("Seleccione la Sucursal de preferencia:\n" +
#                             "1) %s\n" +
#                             "2) %s", ciudadesDestino.get(2).getNombre(), ciudadesDestino.get(3).getNombre());

#                     println("-------------------------------------------------");
#                     println(sucursales1);
#                     print("Elige una opción: ");

#                     boolean numeroValido6 = false;

#                     while (!numeroValido6) {
#                         int sucursalEntrada = scanner.nextInt();

#                         switch (sucursalEntrada) {
#                             case 1:
#                                 sucursalDestino = ciudadesDestino.get(2);
#                                 numeroValido6 = true;
#                                 break;
#                             case 2:
#                                 sucursalDestino = ciudadesDestino.get(3);
#                                 numeroValido6 = true;
#                                 break;
#                             default:
#                                 print("Número no válido. Inténtalo de nuevo: ");
#                         }
#                     }
#                     numeroValido4 = true;
#                     break;
#                 case 3:
#                     String sucursales2 = String.format("Seleccione la Sucursal de preferencia:\n" +
#                             "1) %s\n" +
#                             "2) %s", ciudadesDestino.get(4).getNombre(), ciudadesDestino.get(5).getNombre());

#                     println("-------------------------------------------------");
#                     println(sucursales2);
#                     print("Elige una opción: ");

#                     boolean numeroValido7 = false;

#                     while (!numeroValido7) {
#                         int sucursalEntrada = scanner.nextInt();

#                         switch (sucursalEntrada) {
#                             case 1:
#                                 sucursalDestino = ciudadesDestino.get(4);
#                                 numeroValido7 = true;
#                                 break;
#                             case 2:
#                                 sucursalDestino = ciudadesDestino.get(5);
#                                 numeroValido7 = true;
#                                 break;
#                             default:
#                                 print("Número no válido. Inténtalo de nuevo: ");
#                         }
#                     }
#                     numeroValido4 = true;
#                     break;
#                 default:
#                     print("Número no válido. Inténtalo de nuevo: ");
#             }
#         }

#         boolean disponibilidadSucursal = false;
#         boolean disponibilidadTransporte = false;

#         if (producto instanceof Paquete || producto instanceof Documento) {
#             if (sucursalOrigen.verificarDisponibilidad(producto)) {
#                 disponibilidadSucursal = true;
#             }
#         } else if (producto instanceof Animal) {
#         	if (sucursalOrigen.verificarDisponibilidad(producto)) {
#                 if (sucursalOrigen.disponibilidadJaulas((Animal) producto)) {
#                     disponibilidadSucursal = true;
#                 }
#             }
#         }

#         Transporte vehiculo = null;

#         if (disponibilidadSucursal) {

#             println("---------------DATOS DE TRANSPORTE---------------");
#             println("Ingrese el tipo de tranporte de su preferencia:");
#             println("1) Camión");
#             println("2) Avión (Envío directo y más rápido)");
#             print("Elige una opción: ");

#             boolean numeroValido5 = false;

#             while (!numeroValido5) {
#                 int transporteEntrada = scanner.nextInt();

#                 switch (transporteEntrada) {
#                     case 1:
#                         if (!sucursalOrigen.getCamionesEnSucursal().isEmpty()) {
#                             vehiculo = sucursalOrigen.getCamionesEnSucursal().get(0);
#                             numeroValido5 = true;
#                             disponibilidadTransporte = true;
#                             break;
#                         } else {
#                             println("Lo sentimos no tenemos disponibilidad de camiones en este momento");
#                             println("");
#                             print("1) Volver al menú principal: ");

#                             boolean numerovalido = false;

#                             while (!numerovalido) {
#                                 int menuPrincipalEntrada = scanner.nextInt();
#                                 switch (menuPrincipalEntrada) {
#                                     case 1:
#                                         Main.menuPrincipal(sucursalOrigen);
#                                         numerovalido = true;
#                                         break;
#                                     default:
#                                         print("Número no válido. Inténtalo de nuevo: ");
#                                 }
#                             }
#                             numeroValido5 = true;
#                             break;
#                         }
#                     case 2:
#                         if (!sucursalOrigen.getAvionesEnSucursal().isEmpty()) {
#                             for (Avion aviones : sucursalOrigen.getAvionesEnSucursal()) {
#                                 if (aviones.getSucursalDestino() == sucursalDestino) {
#                                     vehiculo = aviones;
#                                     disponibilidadTransporte = true;
#                                     break;
#                                 }
#                                 if (vehiculo == null) {
#                                     println("Lo sentimos no tenemos disponibilidad de aviones que se dirigen a esa sucursal en este momento");
#                                     println("");
#                                     print("1) Volver al menú principal: ");

#                                     boolean numerovalido = false;

#                                     while (!numerovalido) {
#                                         int menuPrincipalEntrada = scanner.nextInt();
#                                         switch (menuPrincipalEntrada) {
#                                             case 1:
#                                                 Main.menuPrincipal(sucursalOrigen);
#                                                 numerovalido = true;
#                                                 break;
#                                             default:
#                                                 print("Número no válido. Inténtalo de nuevo: ");
#                                         }
#                                     }
#                                 }
#                             }
#                             numeroValido5 = true;
#                             break;
#                         } else {
#                             println("Lo sentimos no tenemos disponibilidad de aviones en este momento");
#                             println("");
#                             print("1) Volver al menú principal: ");

#                             boolean numerovalido = false;

#                             while (!numerovalido) {
#                                 int menuPrincipalEntrada = scanner.nextInt();
#                                 switch (menuPrincipalEntrada) {
#                                     case 1:
#                                         Main.menuPrincipal(sucursalOrigen);
#                                         numerovalido = true;
#                                         break;
#                                     default:
#                                         print("Número no válido. Inténtalo de nuevo: ");
#                                 }
#                             }
#                             numeroValido5 = true;
#                             break;
#                         }
#                     default:
#                         print("Número no válido. Inténtalo de nuevo: ");
#                 }
#             }


#         } else {
#             println("Lo sentimos, no tenemos disponibilidad en la sucursal");
#             println("");
#             print("1) Volver al menú principal: ");

#             boolean numerovalido = false;

#             while (!numerovalido) {
#                 int menuPrincipalEntrada = scanner.nextInt();
#                 switch (menuPrincipalEntrada) {
#                     case 1:
#                         Main.menuPrincipal(sucursalOrigen);
#                         numerovalido = true;
#                         break;
#                     default:
#                         print("Número no válido. Inténtalo de nuevo: ");
#                 }
#             }
#         }

#         if (disponibilidadTransporte) {
#             println("------------------FORMA DE PAGO------------------");
#             println("Seleccione el pago de su preferencia para el pedido:");
#             println("1) Pago total");
#             println("2) Pago fraccionado");
#             println("3) Pago contraentrega");
#             print("Elige una opción: ");

#             boolean numeroValido6 = false;

#             tipoDePago tipoDePago = null;

#             while (!numeroValido6) {
#                 int pagoEntrada = scanner.nextInt();

#                 Guia guia = null;

#                 switch (pagoEntrada) {
#                     case 1:
#                         tipoDePago = Guia.tipoDePago.REMITENTE;
#                         guia = new Guia(producto, remitente, destinatario, sucursalOrigen, sucursalDestino, tipoDePago, vehiculo);
#                         println(guia.toString());

#                         println("Diríjase a la pestaña principal para pagar su servicio.");
#                         println("");

#                         print("1) Volver al menú principal: ");

#                         boolean numerovalido7 = false;

#                         while (!numerovalido7) {
#                             int menuPrincipalEntrada = scanner.nextInt();
#                             switch (menuPrincipalEntrada) {
#                                 case 1:
#                                     Main.menuPrincipal(sucursalOrigen);
#                                     numerovalido7 = true;
#                                     break;
#                                 default:
#                                     print("Número no válido. Inténtalo de nuevo: ");
#                             }
#                         }

#                         numeroValido6 = true;
#                         break;
#                     case 2:
#                         tipoDePago = Guia.tipoDePago.FRACCIONADO;
#                         guia = new Guia(producto, remitente, destinatario, sucursalOrigen, sucursalDestino, tipoDePago, vehiculo);
#                         println(guia.toString());

#                         println("Diríjase a la pestaña principal para pagar su servicio.");
#                         println("");
#                         print("1) Volver al menú principal: ");

#                         boolean numerovalido8 = false;

#                         while (!numerovalido8) {
#                             int menuPrincipalEntrada = scanner.nextInt();
#                             switch (menuPrincipalEntrada) {
#                                 case 1:
#                                     Main.menuPrincipal(sucursalOrigen);
#                                     numerovalido8 = true;
#                                     break;
#                                 default:
#                                     print("Número no válido. Inténtalo de nuevo: ");
#                             }
#                         }

#                         numeroValido6 = true;
#                         break;
#                     case 3:
#                         tipoDePago = Guia.tipoDePago.DESTINATARIO;
#                         guia = new Guia(producto, remitente, destinatario, sucursalOrigen, sucursalDestino, tipoDePago, vehiculo);
#                         println(guia.toString());

#                         sucursalOrigen.agregarProducto(producto);

#                         Random random = new Random();
#                         println("Muchas gracias por usar nuestro servicio, favor acerquese \na la caja #" +
#                                 (random.nextInt(5) + 1) + " para entregar el " + guia.getProducto().getClass().getSimpleName());
#                         println("");
#                         print("1) Volver al menú principal: ");

#                         boolean numerovalido9 = false;

#                         while (!numerovalido9) {
#                             int menuPrincipalEntrada = scanner.nextInt();
#                             switch (menuPrincipalEntrada) {
#                                 case 1:
#                                     Main.menuPrincipal(sucursalOrigen);
#                                     numerovalido9 = true;
#                                     break;
#                                 default:
#                                     print("Número no válido. Inténtalo de nuevo: ");
#                             }
#                         }
#                         numeroValido6 = true;
#                         break;
#                     default:
#                         print("Número no válido. Inténtalo de nuevo: ");
#                 }
#             }
#         }
#         scanner.close();
#     }