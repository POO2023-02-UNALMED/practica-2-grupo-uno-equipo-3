import tkinter as tk
from tkinter import messagebox

class VentanaEmergente(tk.Toplevel):
    def __init__(self, mensaje):
        super().__init__()
        self.title("Confirmación")
        self.geometry("300x100")
        
        label = tk.Label(self, text=mensaje)
        label.pack(pady=10)

        boton_si = tk.Button(self, text="Sí", command=self.confirmar_si)
        boton_si.pack(side="left", padx=20)

        boton_no = tk.Button(self, text="No", command=self.confirmar_no)
        boton_no.pack(side="right", padx=20)

        self.respuesta = None

    def confirmar_si(self):
        self.respuesta = True
        self.destroy()

    def confirmar_no(self):
        self.respuesta = False
        self.destroy()

class Enviar(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(width=1000, height=1000, highlightbackground="#085870", highlightthickness=3)
        self.pack(expand=True)

        self.frame = tk.Frame(self, width=800, height=800, bg="green", highlightbackground="#085870", highlightthickness=5)
        self.frame.pack(expand=True)

        self.titulo_label = tk.Label(self.frame, text="Enviar Paquete", font=("Helvetica", 16), fg="white", bg="#085870")
        self.titulo_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.texto_bienvenida = "Hola, bienvenido a nuestro programa \"CorreMinas\".\n\nEstás en el apartado de enviar un paquete. ¿Qué tipo de paquete deseas enviar?\n \nElige una de las siguientes opciones:"
        self.bienvenida_label = tk.Label(self.frame, text=self.texto_bienvenida, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label.grid(row=1, column=0, columnspan=2, pady=10)

        self.boton_paquete = tk.Button(self.frame, text="Paquete", command=self.mostrar_ventana_paquete)
        self.boton_paquete.grid(row=2, column=0, columnspan=2, pady=5, padx=5)

        self.boton_animal = tk.Button(self.frame, text="Animal", command=self.enviar_animal)
        self.boton_animal.grid(row=3, column=0, pady=5, padx=5)

        self.boton_documento = tk.Button(self.frame, text="Documento", command=self.enviar_documento)
        self.boton_documento.grid(row=3, column=1, pady=5, padx=5)

        self.info_label = tk.Label(self.frame, text="", font=("Helvetica", 12), fg="white", bg="green")
        self.info_label.grid(row=6, column=0, columnspan=2, pady=10)

    def mostrar_ventana_paquete(self):
        self.bienvenida_label.grid_forget()
        self.boton_paquete.grid_forget()
        self.boton_animal.grid_forget()
        self.boton_documento.grid_forget()

        self.texto_bienvenida = "Has seleccionado Enviar un Paquete, diligencie los siguientes datos: \n\n Tenga en cuenta que los datos son en Kg y Metros respectivamente"
        self.bienvenida_label = tk.Label(self.frame, text=self.texto_bienvenida, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label.grid(row=1, column=0, columnspan=2, pady=10)

        peso_label = tk.Label(self.frame, text="Peso:")
        peso_label.grid(row=2, column=0, pady=(10, 0), sticky="e")

        alto_label = tk.Label(self.frame, text="Alto:")
        alto_label.grid(row=3, column=0, pady=10, sticky="e")

        ancho_label = tk.Label(self.frame, text="Ancho:")
        ancho_label.grid(row=4, column=0, pady=10, sticky="e")

        largo_label = tk.Label(self.frame, text="Largo:")
        largo_label.grid(row=5, column=0, pady=10, sticky="e")

        valor_declarado_label = tk.Label(self.frame, text="Precio Del Paquete:")
        valor_declarado_label.grid(row=6, column=0, pady=10, sticky="e")

        peso_entry = tk.Entry(self.frame)
        peso_entry.grid(row=2, column=1, pady=(10, 0), padx=5, sticky="w")

        alto_entry = tk.Entry(self.frame)
        alto_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        ancho_entry = tk.Entry(self.frame)
        ancho_entry.grid(row=4, column=1, pady=5, padx=5, sticky="w")

        largo_entry = tk.Entry(self.frame)
        largo_entry.grid(row=5, column=1, pady=5, padx=5, sticky="w")

        valor_declarado_entry = tk.Entry(self.frame)
        valor_declarado_entry.grid(row=6, column=1, pady=10, padx=5, sticky="w")

        boton_enviar = tk.Button(self.frame, text="Enviar", command=lambda: self.mostrar_info_emergente(peso_entry.get(), alto_entry.get(), ancho_entry.get(), largo_entry.get(), valor_declarado_entry.get()))
        boton_enviar.grid(row=7, column=0, columnspan=2, pady=10)

#        def cambiar_frame (self):
 #           frame_nuevo = FrameUsuario(self.master) 

# class FrameUsuario(tk.Frame):
#     def __init__(self, ventana):
#         super().__init__(ventana)
#         self.config(bg="#085870")
#         self.pack(fill="both",expand=True)

    def mostrar_info_emergente(self, peso, alto, ancho, largo, valor_declarado):
        if not peso.isdigit() or not alto.isdigit() or not ancho.isdigit() or not largo.isdigit() or not valor_declarado.isdigit():
            messagebox.showerror("Error", "No se permite letras, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return

        mensaje = "¿El paquete es frágil?"
        ventana_emergente = VentanaEmergente(mensaje)
        ventana_emergente.wait_window()

        if ventana_emergente.respuesta is not None:
            tipo_producto = "Paquete"
            es_fragil = "Sí" if ventana_emergente.respuesta else "No"

            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Peso: {peso} Kg\n"
            info_text += f"Alto: {alto} m\n"
            info_text += f"Ancho: {ancho} m\n"
            info_text += f"Largo: {largo} m\n"
            info_text += f"Es frágil: {es_fragil}\n"
            info_text += f"Precio Del Paquete: $ {valor_declarado}"

            messagebox.showinfo("Información del Paquete", info_text)

    def confirmar_envio(self, peso, alto, ancho, largo):
        if not peso.isdigit() or not alto.isdigit() or not ancho.isdigit() or not largo.isdigit():
            messagebox.showerror("Error", "No se permite letras, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return
        
        mensaje = "¿El paquete es frágil?"
        ventana_emergente = VentanaEmergente(mensaje)
        ventana_emergente.wait_window()
        
        if ventana_emergente.respuesta is not None:
            if ventana_emergente.respuesta:
                valor_declarado_label = tk.Label(self.frame, text="Precio Del Paquete:")
                valor_declarado_label.grid(row=7, column=0, pady=10, sticky="e")

                valor_declarado_entry = tk.Entry(self.frame)
                valor_declarado_entry.grid(row=7, column=1, pady=10, padx=5, sticky="w")

                boton_enviar = tk.Button(self.frame, text="Enviar", command=lambda: self.confirmar_envio_con_valor_declarado(peso, alto, ancho, largo, valor_declarado_entry.get()))
                boton_enviar.grid(row=8, column=0, columnspan=2, pady=10)
                print(f"Información del paquete: Peso={peso}, Alto={alto}, Ancho={ancho}, Largo={largo}")
                print("Paquete es frágil")
            else:
                print(f"Información del paquete: Peso={peso}, Alto={alto}, Ancho={ancho}, Largo={largo}")
                print("Paquete no es frágil")

    def confirmar_envio_con_valor_declarado(self, peso, alto, ancho, largo, valor_declarado):
        if not peso.isdigit() or not alto.isdigit() or not ancho.isdigit() or not largo.isdigit() or not valor_declarado.isdigit():
            messagebox.showerror("Error", "No se permite letras, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return

        mensaje = "¿El paquete es frágil?"
        ventana_emergente = VentanaEmergente(mensaje)
        ventana_emergente.wait_window()

        if ventana_emergente.respuesta is not None:
            tipo_producto = "Paquete"
            es_fragil = "Sí" if ventana_emergente.respuesta else "No"

            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Peso: {peso} Kg\n"
            info_text += f"Alto: {alto} m\n"
            info_text += f"Ancho: {ancho} m\n"
            info_text += f"Largo: {largo} m\n"
            info_text += f"Es frágil: {es_fragil}\n"
            info_text += f"Precio Del Paquete: $ {valor_declarado}"

            self.info_label.config(text=info_text)

    def enviar_animal(self):
        print("Has seleccionado enviar un animal.")

    def enviar_documento(self):
        print("Has seleccionado enviar un documento.")
        pass

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