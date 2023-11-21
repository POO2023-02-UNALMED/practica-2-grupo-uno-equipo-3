import tkinter as tk
from tkinter import PhotoImage, messagebox
from gestorAplicacion.administracion.guia import Guia
from gestorAplicacion.administracion.sucursal import Sucursal
from gestorAplicacion.personas.cliente import Cliente
from gestorAplicacion.personas.destinatario import Destinatario
from gestorAplicacion.productos.animal import Animal
from gestorAplicacion.productos.documento import Documento

from gestorAplicacion.productos.paquete import Paquete
from gestorAplicacion.transportes.avion import Avion
from gestorAplicacion.transportes.camion import Camion
from gestorAplicacion.transportes.transporte import Transporte
valores = []
class VentanaEmergente(tk.Toplevel):
    def __init__(self, mensaje):
        super().__init__()
        self.title("Confirmación")
        self.geometry("300x100")
        
        label = tk.Label(self, text=mensaje)
        label.pack(pady=10)

        boton_si = tk.Button(self, text="Sí", command=self.confirmar_si, bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_si.pack(side="left", padx=20)

        boton_no = tk.Button(self, text="No", command=self.confirmar_no, bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
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

#ESTAS 2 LINEA SERA PARA QUE SIRVIERA. NO SIRVE.
        self.ciudad_origen_var = tk.StringVar()
        self.ciudad_destino_var = tk.StringVar()

        self.config(width=1000, height=1000, bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.pack(expand=True)

        self.frame = tk.Frame(self, width=800, height=800, bg="#739072",highlightbackground="#3A4D39",highlightthickness=3)
        self.frame.pack(expand=True)

        self.titulo_label = tk.Label(self.frame, text="Enviar Pedido", font=("Arial", 30), bg="#739072", foreground="white")
        self.titulo_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.texto_bienvenida = "Hola, bienvenido a nuestro programa \"CorreMinas\".\n\nEstás en el apartado de enviar un paquete. ¿Qué tipo de paquete deseas enviar?\n \nElige una de las siguientes opciones:"
        self.bienvenida_label = tk.Label(self.frame, text=self.texto_bienvenida, justify="left", wraplength=380, font=("Arial", 11), bg="#739072", fg="white")
        self.bienvenida_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.boton_paquete = tk.Button(self.frame, text="Paquete", command=self.mostrar_ventana_paquete, bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        self.boton_paquete.grid(row=2, column=0,  pady=5, padx=5)
        # imagenPaquete = PhotoImage(file=f"src\gestorGrafico\imagenes\iconos\paquete.png")
        # self.boton_paquete.config(image=imagenPaquete)
   

        self.boton_animal = tk.Button(self.frame, text="Animal", command=self.enviar_animal, bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        self.boton_animal.grid(row=2, column=1, pady=5, padx=5)
        # imagenAnimal = PhotoImage(file=f"src\gestorGrafico\imagenes\iconos\animal.png")  
        # self.boton_animal.config(image=imagenAnimal)

        self.boton_documento = tk.Button(self.frame, text="Documento", command=self.enviar_documento, bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        self.boton_documento.grid(row=2, column=2, pady=5, padx=5)
        # imagenDocumento = PhotoImage(file=f"src\gestorGrafico\imagenes\iconos\documento.png")  
        # self.boton_documento.config(image=imagenDocumento)

        self.info_label = tk.Label(self.frame, text="", font=("Helvetica", 12), bg="#739072", fg="white")
        self.info_label.grid(row=6, column=0, columnspan=2, pady=10)


    def mostrar_ventana_paquete(self):
        self.bienvenida_label.grid_forget()
        self.boton_paquete.grid_forget()
        self.boton_animal.grid_forget()
        self.boton_documento.grid_forget()

        self.texto_bienvenida = "Has seleccionado Enviar un Paquete, diligencie los siguientes datos: \n\n Tenga en cuenta que los datos son en Kg y Metros respectivamente"
        self.bienvenida_label = tk.Label(self.frame, text=self.texto_bienvenida, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="#739072")
        self.bienvenida_label.grid(row=1, column=0, columnspan=2, pady=10)

        peso_label = tk.Label(self.frame, text="Peso:", bg="#739072", fg="white")
        peso_label.grid(row=2, column=0, pady=(10, 0), sticky="e")

        alto_label = tk.Label(self.frame, text="Alto:", bg="#739072", fg="white")
        alto_label.grid(row=3, column=0, pady=10, sticky="e")

        ancho_label = tk.Label(self.frame, text="Ancho:", bg="#739072", fg="white")
        ancho_label.grid(row=4, column=0, pady=10, sticky="e")

        largo_label = tk.Label(self.frame, text="Largo:", bg="#739072", fg="white")
        largo_label.grid(row=5, column=0, pady=10, sticky="e")

        valor_declarado_label = tk.Label(self.frame, text="Precio Del Paquete:", bg="#739072", fg="white")
        valor_declarado_label.grid(row=6, column=0, pady=10, sticky="e")

        peso_entry = tk.Entry(self.frame)
        peso_entry.grid(row=2, column=1, sticky="w")

        alto_entry = tk.Entry(self.frame)
        alto_entry.grid(row=3, column=1,  sticky="w")

        ancho_entry = tk.Entry(self.frame)
        ancho_entry.grid(row=4, column=1, sticky="w")

        largo_entry = tk.Entry(self.frame)
        largo_entry.grid(row=5, column=1,  sticky="w")

        valor_declarado_entry = tk.Entry(self.frame)
        valor_declarado_entry.grid(row=6, column=1, sticky="w")

        # fragilLabel = tk.Label(self.frame, text="¿Es fragil?")
        # fragilLabel.grid(row=7,column=0,pady=10, sticky="e")

        # fragilSioNo = ["Si", "No"]
        # fragilSioNo_var = tk.StringVar()
        # fragilSioNo_dropdown = tk.OptionMenu(self.frame, fragilSioNo_var, *fragilSioNo)
        # fragilSioNo_dropdown.grid(row=7, column=1, pady=5, padx=5, sticky="w")


        boton_enviar = tk.Button(self.frame, text="Enviar", command=lambda: self.mostrar_info_emergente(peso_entry.get(), alto_entry.get(), ancho_entry.get(), largo_entry.get(), valor_declarado_entry.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_enviar.grid(row=8, column=0, columnspan=2, pady=10)


    


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
            if es_fragil == "Si":
                fragil = True
            else:
                fragil = False

            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Peso: {peso} Kg\n"
            info_text += f"Alto: {alto} m\n"
            info_text += f"Ancho: {ancho} m\n"
            info_text += f"Largo: {largo} m\n"
            info_text += f"Es frágil: {es_fragil}\n"
            info_text += f"Precio Del Paquete: $ {valor_declarado}"

            peso = int(peso)
            alto = int(alto)
            ancho = int(ancho)
            largo = int(largo)
            valor_declarado = int(valor_declarado)

            #ya se crea el objeto de tipo paquete - Kevin
            paqueteAEnviar = Paquete(peso,alto,ancho,largo,fragil,valor_declarado)
            valores.append(paqueteAEnviar)
            messagebox.showinfo("Información del Paquete", info_text)


            # Oculta el frame actual para poder crear uno ahorita mas adelante
            self.frame.pack_forget()

            # Crea y muestra un nuevo frame  (que bendicion)
            nuevo_frame = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
            nuevo_frame.grid(row=0, column=0, sticky="nsew")

            label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), bg="#739072", fg="white")
            label_nuevo_frame.grid(row=0, column=0, pady=10)

            self.texto_bienvenida2 = "Por favor diligencie los siguientes datos."
            self.bienvenida2_label = tk.Label(nuevo_frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, bg="#739072", fg="white")
            self.bienvenida2_label.grid(row=1, column=0, columnspan=3, pady=10)

            remitente_nombre_label = tk.Label(nuevo_frame, text="Nombre del Remitente:", bg="#739072", fg="white")
            remitente_nombre_label.grid(row=2, column=0, pady=5, sticky="e")

            remitente_cedula_label = tk.Label(nuevo_frame, text="Cédula del Remitente:", bg="#739072", fg="white")
            remitente_cedula_label.grid(row=3, column=0, pady=5, sticky="e")

            remitente_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Remitente:", bg="#739072", fg="white")
            remitente_telefono_label.grid(row=4, column=0, pady=5, sticky="e")

            remitente_nombre_entry = tk.Entry(nuevo_frame)
            remitente_nombre_entry.grid(row=2, column=1,sticky="w")

            remitente_cedula_entry = tk.Entry(nuevo_frame)
            remitente_cedula_entry.grid(row=3, column=1, sticky="w")

            remitente_telefono_entry = tk.Entry(nuevo_frame)
            remitente_telefono_entry.grid(row=4, column=1,sticky="w")

            destinatario_nombre_label = tk.Label(nuevo_frame, text="Nombre del Destinatario:", bg="#739072", fg="white")
            destinatario_nombre_label.grid(row=5, column=0, pady=5, sticky="e")

            destinatario_cedula_label = tk.Label(nuevo_frame, text="Cédula del Destinatario:", bg="#739072", fg="white")
            destinatario_cedula_label.grid(row=6, column=0, pady=5, sticky="e")

            destinatario_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Destinatario:", bg="#739072", fg="white")
            destinatario_telefono_label.grid(row=7, column=0, pady=5, sticky="e")

            destinatario_nombre_entry = tk.Entry(nuevo_frame)
            destinatario_nombre_entry.grid(row=5, column=1, sticky="w")

            destinatario_cedula_entry = tk.Entry(nuevo_frame)
            destinatario_cedula_entry.grid(row=6, column=1, sticky="w")

            destinatario_telefono_entry = tk.Entry(nuevo_frame)
            destinatario_telefono_entry.grid(row=7, column=1, sticky="w")

            boton_enviar_cliente = tk.Button(nuevo_frame, text="Enviar", command=lambda: self.mostrar_info_cliente(remitente_nombre_entry.get(), remitente_cedula_entry.get(), remitente_telefono_entry.get(), destinatario_nombre_entry.get(), destinatario_cedula_entry.get(), destinatario_telefono_entry.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
            boton_enviar_cliente.grid(row=8, column=0, columnspan=2, pady=10)

    def mostrar_info_cliente(self, remitente_nombre, remitente_cedula, remitente_telefono, destinatario_nombre, destinatario_cedula, destinatario_telefono):
        
        if not (remitente_nombre.isalpha() and destinatario_nombre.isalpha()):
            messagebox.showerror("Error", "Los campos de *Nombre* no deben estar vacios y aparta deben ser solo Letras.")
            return
        if not remitente_telefono.isdigit() or not remitente_cedula.isdigit() or not destinatario_cedula.isdigit() or not destinatario_telefono.isdigit():
            messagebox.showerror("Error", "No se permite letras en la casillas de *Cedula* y *Telefono*, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return
        
        info_text_cliente = "\nInformación del Remitente:\n"
        info_text_cliente += f"Nombre: {remitente_nombre}\n"
        info_text_cliente += f"Cédula: {remitente_cedula}\n"
        info_text_cliente += f"Teléfono: {remitente_telefono}\n"

        info_text_cliente += "\nInformación del Destinatario:\n"
        info_text_cliente += f"Nombre: {destinatario_nombre}\n"
        info_text_cliente += f"Cédula: {destinatario_cedula}\n"
        info_text_cliente += f"Teléfono: {destinatario_telefono}"

        remitente = Cliente(remitente_nombre,remitente_cedula,remitente_telefono)

        valores.append(remitente)
        destinatario = Destinatario(destinatario_nombre,destinatario_cedula,destinatario_telefono)

        valores.append(destinatario)

        messagebox.showinfo("Información del Cliente", info_text_cliente)

        self.frame.pack_forget()

        #Segundo Frame Detalles Envio
        nuevo_frame = tk.Frame(self, width=800, height=800, bg="blue", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame.grid(row=0, column=0, pady=10)

        nuevo_frame_2 = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame_2.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Detalles Del Envio", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame_2.grid(row=0, column=0, pady=10, columnspan=2)

        descripcion_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Por favor selecciona la ciudad desde la que envias tu producto y a cual deseas enviarlo.", bg="#739072", fg="white")
        descripcion_nuevo_frame_2.grid(row=1, column=0, pady=10,columnspan=2)

        ciudades_origen = ["Medellin Norte", "Medellin Sur","Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_origen_label = tk.Label(nuevo_frame_2, text="Ciudad de Origen:", bg="#739072", fg="white")
        ciudad_origen_label.grid(row=2, column=0, pady=5, sticky="e")
        ciudad_origen_var = tk.StringVar()
        ciudad_origen_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_origen_var, *ciudades_origen)
        ciudad_origen_dropdown.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        ciudades_destino = ["Medellin Norte", "Medellin Sur","Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_destino_label = tk.Label(nuevo_frame_2, text="Ciudad de Destino:", bg="#739072", fg="white")
        ciudad_destino_label.grid(row=3, column=0, pady=5, sticky="e")
        ciudad_destino_var = tk.StringVar()
        ciudad_destino_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_destino_var, *ciudades_destino)
        ciudad_destino_dropdown.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        labelTransporte = tk.Label(nuevo_frame_2,text="Tipo De Transporte:", bg="#739072", fg="white")
        labelTransporte.grid(row=4,column=0,pady=5,sticky="e")

        Transporte_lista = ["Camión","Avión"]
        Transporte_lista_var = tk.StringVar()
        Transporte_lista_menu = tk.OptionMenu(nuevo_frame_2, Transporte_lista_var, *Transporte_lista)
        Transporte_lista_menu.grid(row=4,column=1,pady=5,padx=5,sticky="w")

        labelPago = tk.Label(nuevo_frame_2,text="Método de pago:", bg="#739072", fg="white")
        labelPago.grid(row=5,column=0,pady=5,sticky="e")

        pago_lista = ["Pago total","Pago Fraccionado", "Pago contraentrega"]
        pago_lista_var = tk.StringVar()
        pago_lista_menu = tk.OptionMenu(nuevo_frame_2, pago_lista_var, *pago_lista)
        pago_lista_menu.grid(row=5,column=1,pady=5,padx=5,sticky="w")

        boton_enviar_2 = tk.Button(nuevo_frame_2, text="Enviar", command=lambda:self.enviar_detalle_envio(ciudad_origen_var.get(),ciudad_destino_var.get(),Transporte_lista_var.get(),pago_lista_var.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_enviar_2.grid(row=6, column=0, columnspan=2, pady=10)

 


#AYUDAR KEVIN

    def enviar_detalle_envio(self,origen,destino,transporte,pago):
        origen = origen
        destino = destino
        transporte = transporte
        pago = pago



        sucursales = Sucursal._todasLasSucursales
        origen = origen
        for i in sucursales:
            if i._nombre == origen:
                valores.append(i)
                camiones = i.getCamionesEnSucursal()

                aviones = i.getAvionesEnSucursal()

            if transporte == "Camión":
                    transporteT = camiones[0]
            if transporte == "Avión":
                    transporteT = aviones[0]
            

        destino = destino
        for k in sucursales:
            if k._nombre == destino:
                valores.append(k)
            
        if pago == "Pago contraentrega":
                pagoTipo = Guia.tipoDePago.DESTINATARIO
        if pago == "Pago total":
                pagoTipo = Guia.tipoDePago.REMITENTE
        if pago == "Pago Fraccionado":
                pagoTipo = Guia.tipoDePago.FRACCIONADO

        valores.append(pagoTipo)


        valores.append(transporteT)





        #Se va crear la guia del paquete que se envió
        guiaPaqueteAEnviar = Guia(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])

        #Se añade el paquete que se creó a la sucursal de origen
        #se verifica si es necesario pagar para enviar

        if (guiaPaqueteAEnviar.getTipoDePago() == Guia.tipoDePago.DESTINATARIO):
            valores[3].getInventario().append(valores[0])


        else:
            if (guiaPaqueteAEnviar.getPagoPendiente == 0):
                  valores[3].getInventario().append(valores[0])
            else:
                 pass
                  
                  




        if origen and destino != None:
             #ACA VA LA GUIA
            tipo_producto = "Paquete"
            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Código del paquete: {valores[0].getCodigo()}\n"
            info_text += f"Ciudad De Origen: {origen} \n"
            info_text += f"Ciudad De Destino: {destino} \n"
            info_text += f"Tipo de pago: {pago} \n"
            info_text += f"Precio total: ${guiaPaqueteAEnviar.getPrecioTotal()}\n"
            info_text += f"Vehículo: {transporte}"

            messagebox.showinfo("Los detalles del envío han sido enviados con éxito.", info_text)
        Enviar.destroy(self)
        valores.clear()

            

    #ENVIAR ANIMAL  
    def enviar_animal(self):
        self.bienvenida_label.grid_forget()
        self.boton_paquete.grid_forget()
        self.boton_animal.grid_forget()
        self.boton_documento.grid_forget()

        self.texto_bienvenida1 = "Has seleccionado Enviar un Animal."
        self.texto_bienvenida2 = "Para continuar deberá diligenciar los siguientes datos: "
        self.bienvenida_label1 = tk.Label(self.frame, text=self.texto_bienvenida1, font=("Helvetica", 12), justify="left", wraplength=380, bg="#739072", fg="white")
        self.bienvenida_label1.grid(row=1, column=0, columnspan=2, pady=10)
        self.bienvenida_label2 = tk.Label(self.frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, bg="#739072", fg="white")
        self.bienvenida_label2.grid(row=2, column=0, columnspan=2, pady=10)

        nombreAnimal_label = tk.Label(self.frame, text="Nombre del animal:", bg="#739072", fg="white")
        nombreAnimal_label.grid(row=3, column=0, pady=(10, 0), sticky="e")

        entryNombreAnimal = tk.Entry(self.frame)
        entryNombreAnimal.grid(row=3, column=1, sticky="w")

        edadAnimal_label = tk.Label(self.frame, text="Edad del animal:", bg="#739072", fg="white")
        edadAnimal_label.grid(row=4, column=0, pady=10, sticky="e")

        entryEdadAnimal = tk.Entry(self.frame)
        entryEdadAnimal.grid(row=4, column=1, sticky="w")

        pesoAnimal_label = tk.Label(self.frame, text="Peso:", bg="#739072", fg="white")
        pesoAnimal_label.grid(row=5, column=0, pady=10, sticky="e")

        entryPesoAnimal = tk.Entry(self.frame)
        entryPesoAnimal.grid(row=5, column=1, sticky="w")
        
        tiposDeAnimales = ["Perro", "Gato", "Hamster", "Loro", "Caballo", "Vaca"]
        tiposDeAnimales_label = tk.Label(self.frame, text="Tipo de animal:", bg="#739072", fg="white")
        tiposDeAnimales_label.grid(row=6, column=0, pady=5, sticky="e")
        tipoDeAnimal_var = tk.StringVar()
        tipoDeAnimal_dropdown = tk.OptionMenu(self.frame, tipoDeAnimal_var, *tiposDeAnimales)
        tipoDeAnimal_dropdown.grid(row=6, column=1, sticky="w")

        botonSiguiente = tk.Button(self.frame,text="Siguiente",bg="#3A4D39", command=lambda:self.enviar_detalle_animal(entryNombreAnimal.get(), entryEdadAnimal.get(), entryPesoAnimal.get(),tipoDeAnimal_var.get()), font=("arial", 11, "bold"),fg="white")
        botonSiguiente.grid(row=7,column=0,columnspan=2,pady=5, padx=5)

    def enviar_detalle_animal(self, nombreAnimal, edadAnimal, pesoAnimal,tipoDeAnimal):  
        tipoDeAnimal = tipoDeAnimal
        if not nombreAnimal.isalpha():
            messagebox.showerror("Error", "Los campos de *Nombre* no deben estar vacios y aparta deben ser solo Letras.")
            return
        if not edadAnimal.isdigit() or not pesoAnimal.isdigit():
            messagebox.showerror("Error", "No se permite letras, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return

        tipo_producto = "Animal"
        info_text = f"Tipo de producto: {tipo_producto}\n"
        info_text += f"Tipo de animal: {tipoDeAnimal} \n"
        info_text += f"Nombre animal:{nombreAnimal} \n"
        info_text += f"Edad animal:{edadAnimal} \n"
        info_text += f"Peso animal:{pesoAnimal} \n"

        edadAnimal = int(edadAnimal)
        pesoAnimal = int(pesoAnimal)

        if tipoDeAnimal == "Perro":
             tipoAnimalT = Animal.tipoAnimal.PERRO
        if tipoDeAnimal == "Gato":
             tipoAnimalT = Animal.tipoAnimal.GATO
        if tipoDeAnimal == "Hamster":
             tipoAnimalT = Animal.tipoAnimal.HAMSTER
        if tipoDeAnimal == "Loro":
             tipoAnimalT = Animal.tipoAnimal.LORO
        if tipoDeAnimal == "Caballo":
             tipoAnimalT = Animal.tipoAnimal.CABALLO
        if tipoDeAnimal == "Vaca":
             tipoAnimalT = Animal.tipoAnimal.VACA

        #se crea el objeto de tipo animal - Kevin
        animalAEnviar = Animal(nombreAnimal,edadAnimal,pesoAnimal,tipoAnimalT)
        valores.append(animalAEnviar)

        messagebox.showinfo("Informacion del paquete", info_text)

        # Oculta el frame actual para poder crear uno ahorita mas adelante
        self.frame.pack_forget()

        # Crea y muestra un nuevo frame  (que bendicion)
        nuevo_frame = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame.grid(row=0, column=0, pady=10)

        self.texto_bienvenida2 = "Por favor diligencie los siguientes datos."
        self.bienvenida2_label = tk.Label(nuevo_frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, bg="#739072", fg="white")
        self.bienvenida2_label.grid(row=1, column=0, columnspan=3, pady=10)

        remitente_nombre_label = tk.Label(nuevo_frame, text="Nombre del Remitente:", bg="#739072", fg="white")
        remitente_nombre_label.grid(row=2, column=0, pady=5, sticky="e")

        remitente_cedula_label = tk.Label(nuevo_frame, text="Cédula del Remitente:", bg="#739072", fg="white")
        remitente_cedula_label.grid(row=3, column=0, pady=5, sticky="e")

        remitente_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Remitente:", bg="#739072", fg="white")
        remitente_telefono_label.grid(row=4, column=0, pady=5, sticky="e")

        remitente_nombre_entry = tk.Entry(nuevo_frame)
        remitente_nombre_entry.grid(row=2, column=1,sticky="w")

        remitente_cedula_entry = tk.Entry(nuevo_frame)
        remitente_cedula_entry.grid(row=3, column=1, sticky="w")

        remitente_telefono_entry = tk.Entry(nuevo_frame)
        remitente_telefono_entry.grid(row=4, column=1,sticky="w")

        destinatario_nombre_label = tk.Label(nuevo_frame, text="Nombre del Destinatario:", bg="#739072", fg="white")
        destinatario_nombre_label.grid(row=5, column=0, pady=5, sticky="e")

        destinatario_cedula_label = tk.Label(nuevo_frame, text="Cédula del Destinatario:", bg="#739072", fg="white")
        destinatario_cedula_label.grid(row=6, column=0, pady=5, sticky="e")

        destinatario_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Destinatario:", bg="#739072", fg="white")
        destinatario_telefono_label.grid(row=7, column=0, pady=5, sticky="e")

        destinatario_nombre_entry = tk.Entry(nuevo_frame)
        destinatario_nombre_entry.grid(row=5, column=1, sticky="w")

        destinatario_cedula_entry = tk.Entry(nuevo_frame)
        destinatario_cedula_entry.grid(row=6, column=1, sticky="w")

        destinatario_telefono_entry = tk.Entry(nuevo_frame)
        destinatario_telefono_entry.grid(row=7, column=1, sticky="w")

        boton_enviar_cliente = tk.Button(nuevo_frame, text="Enviar", command=lambda: self.mostrar_info_cliente2(remitente_nombre_entry.get(), remitente_cedula_entry.get(), remitente_telefono_entry.get(), destinatario_nombre_entry.get(), destinatario_cedula_entry.get(), destinatario_telefono_entry.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_enviar_cliente.grid(row=8, column=0, columnspan=2, pady=10)

    def mostrar_info_cliente2(self, remitente_nombre, remitente_cedula, remitente_telefono, destinatario_nombre, destinatario_cedula, destinatario_telefono):
        
        if not (remitente_nombre.isalpha() and destinatario_nombre.isalpha()):
            messagebox.showerror("Error", "Los campos de *Nombre* no deben estar vacios y aparta deben ser solo Letras.")
            return
        if not remitente_telefono.isdigit() or not remitente_cedula.isdigit() or not destinatario_cedula.isdigit() or not destinatario_telefono.isdigit():
            messagebox.showerror("Error", "No se permite letras en la casillas de *Cedula* y *Telefono*, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return
        
        info_text_cliente = "\nInformación del Remitente:\n"
        info_text_cliente += f"Nombre: {remitente_nombre}\n"
        info_text_cliente += f"Cédula: {remitente_cedula}\n"
        info_text_cliente += f"Teléfono: {remitente_telefono}\n"

        info_text_cliente += "\nInformación del Destinatario:\n"
        info_text_cliente += f"Nombre: {destinatario_nombre}\n"
        info_text_cliente += f"Cédula: {destinatario_cedula}\n"
        info_text_cliente += f"Teléfono: {destinatario_telefono}"

        remitente = Cliente(remitente_nombre,remitente_cedula,remitente_telefono)


        valores.append(remitente)
        destinatario = Destinatario(destinatario_nombre,destinatario_cedula,destinatario_telefono)


        valores.append(destinatario)

        messagebox.showinfo("Información del Cliente", info_text_cliente)

        self.frame.pack_forget()

        #Segundo Frame Detalles Envioooo
        nuevo_frame = tk.Frame(self, width=800, height=800, bg="blue", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame.grid(row=0, column=0, pady=10)

        nuevo_frame_2 = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame_2.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Detalles Del Envio", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame_2.grid(row=0, column=0, pady=10, columnspan=2)

        descripcion_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Por favor selecciona la ciudad desde la que envias tu Animal y a cual deseas enviarlo.", bg="#739072", fg="white")
        descripcion_nuevo_frame_2.grid(row=1, column=0, pady=10,columnspan=2)

        ciudades_origen = ["Medellin Norte", "Medellin Sur","Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_origen_label = tk.Label(nuevo_frame_2, text="Ciudad de Origen:", bg="#739072", fg="white")
        ciudad_origen_label.grid(row=2, column=0, pady=5, sticky="e")
        ciudad_origen_var = tk.StringVar()
        ciudad_origen_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_origen_var, *ciudades_origen)
        ciudad_origen_dropdown.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        ciudades_destino = ["Medellin Norte", "Medellin Sur","Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_destino_label = tk.Label(nuevo_frame_2, text="Ciudad de Destino:", bg="#739072", fg="white")
        ciudad_destino_label.grid(row=3, column=0, pady=5, sticky="e")
        ciudad_destino_var = tk.StringVar()
        ciudad_destino_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_destino_var, *ciudades_destino)
        ciudad_destino_dropdown.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        labelTransporte = tk.Label(nuevo_frame_2,text="Tipo De Transporte:", bg="#739072", fg="white")
        labelTransporte.grid(row=4,column=0,pady=5,sticky="e")

        Transporte_lista = ["Camión","Avión"]
        Transporte_lista_var = tk.StringVar()
        Transporte_lista_menu = tk.OptionMenu(nuevo_frame_2, Transporte_lista_var, *Transporte_lista)
        Transporte_lista_menu.grid(row=4,column=1,pady=5,padx=5,sticky="w")

        labelPago = tk.Label(nuevo_frame_2,text="Método de pago:", bg="#739072", fg="white")
        labelPago.grid(row=5,column=0,pady=5,sticky="e")

        pago_lista = ["Pago total","Pago Fraccionado", "Pago contraentrega"]
        pago_lista_var = tk.StringVar()
        pago_lista_menu = tk.OptionMenu(nuevo_frame_2, pago_lista_var, *pago_lista)
        pago_lista_menu.grid(row=5,column=1,pady=5,padx=5,sticky="w")

        boton_enviar_2 = tk.Button(nuevo_frame_2, text="Enviar", command=lambda:self.enviar_detalle_envioanimal(ciudad_origen_var.get(),ciudad_destino_var.get(),Transporte_lista_var.get(),pago_lista_var.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_enviar_2.grid(row=6, column=0, columnspan=2, pady=10)

 




    def enviar_detalle_envioanimal(self,origen,destino,transporte,pago):
        origen = origen
        destino = destino
        transporte = transporte
        pago = pago



        sucursales = Sucursal._todasLasSucursales
        origen = origen
        for i in sucursales:
            if i._nombre == origen:
                valores.append(i)
                camiones = i.getCamionesEnSucursal()

                aviones = i.getAvionesEnSucursal()

            if transporte == "Camión":
                    transporteT = camiones[0]
            if transporte == "Avión":
                    transporteT = aviones[0]
            

        destino = destino
        for k in sucursales:
            if k._nombre == destino:
                valores.append(k)
            
        if pago == "Pago contraentrega":
                pagoTipo = Guia.tipoDePago.DESTINATARIO
        if pago == "Pago total":
                pagoTipo = Guia.tipoDePago.REMITENTE
        if pago == "Pago Fraccionado":
                pagoTipo = Guia.tipoDePago.FRACCIONADO

        valores.append(pagoTipo)


        valores.append(transporteT)






        #Se va crear la guia del paquete que se envió
        guiaAnimalAEnviar = Guia(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])


        #Se añade el paquete que se creó a la sucursal de origen
        #se verifica si es necesario pagar para enviar
      
        if (guiaAnimalAEnviar.getTipoDePago() == Guia.tipoDePago.DESTINATARIO):
            valores[3].getInventario().append(valores[0])

        else:
            if (guiaAnimalAEnviar.getPagoPendiente == 0):
                  valores[3].getInventario().append(valores[0])
            else:
                 pass
                  
        if origen and destino != None:
             #ACA VA LA GUIA
            tipo_producto = "Animal"
            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Código del paquete: {valores[0].getCodigo()}\n"
            info_text += f"Ciudad De Origen: {origen} \n"
            info_text += f"Ciudad De Destino: {destino} \n"
            info_text += f"Tipo de pago: {pago} \n"
            info_text += f"Precio total: ${guiaAnimalAEnviar.getPrecioTotal()}\n"
            info_text += f"Vehículo: {transporte}"

            messagebox.showinfo("Los detalles del envío han sido enviados con éxito.", info_text)
        Enviar.destroy(self)
        valores.clear()


    def enviar_documento(self):
        self.bienvenida_label.grid_forget()
        self.boton_paquete.grid_forget()
        self.boton_animal.grid_forget()
        self.boton_documento.grid_forget()
        self.frame.pack_forget()

        nuevo_frame = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame.grid(row=0, column=0, pady=10)

        self.texto_bienvenida2 = "Has seleccionado Enviar un Documento.\n\n Por favor diligencie los siguientes datos."
        self.bienvenida2_label = tk.Label(nuevo_frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, bg="#739072", fg="white")
        self.bienvenida2_label.grid(row=1, column=0, columnspan=3, pady=10)

        remitente_nombre_label = tk.Label(nuevo_frame, text="Nombre del Remitente:", bg="#739072", fg="white")
        remitente_nombre_label.grid(row=2, column=0, pady=5, sticky="e")

        remitente_cedula_label = tk.Label(nuevo_frame, text="Cédula del Remitente:", bg="#739072", fg="white")
        remitente_cedula_label.grid(row=3, column=0, pady=5, sticky="e")

        remitente_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Remitente:", bg="#739072", fg="white")
        remitente_telefono_label.grid(row=4, column=0, pady=5, sticky="e")

        remitente_nombre_entry = tk.Entry(nuevo_frame)
        remitente_nombre_entry.grid(row=2, column=1,sticky="w")

        remitente_cedula_entry = tk.Entry(nuevo_frame)
        remitente_cedula_entry.grid(row=3, column=1, sticky="w")

        remitente_telefono_entry = tk.Entry(nuevo_frame)
        remitente_telefono_entry.grid(row=4, column=1,sticky="w")

        destinatario_nombre_label = tk.Label(nuevo_frame, text="Nombre del Destinatario:", bg="#739072", fg="white")
        destinatario_nombre_label.grid(row=5, column=0, pady=5, sticky="e")

        destinatario_cedula_label = tk.Label(nuevo_frame, text="Cédula del Destinatario:", bg="#739072", fg="white")
        destinatario_cedula_label.grid(row=6, column=0, pady=5, sticky="e")

        destinatario_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Destinatario:", bg="#739072", fg="white")
        destinatario_telefono_label.grid(row=7, column=0, pady=5, sticky="e")

        destinatario_nombre_entry = tk.Entry(nuevo_frame)
        destinatario_nombre_entry.grid(row=5, column=1, sticky="w")

        destinatario_cedula_entry = tk.Entry(nuevo_frame)
        destinatario_cedula_entry.grid(row=6, column=1, sticky="w")

        destinatario_telefono_entry = tk.Entry(nuevo_frame)
        destinatario_telefono_entry.grid(row=7, column=1, sticky="w")

 
        boton_enviar_cliente = tk.Button(nuevo_frame, text="Enviar", command=lambda: self.mostrar_info_cliente3(remitente_nombre_entry.get(), remitente_cedula_entry.get(), remitente_telefono_entry.get(), destinatario_nombre_entry.get(), destinatario_cedula_entry.get(), destinatario_telefono_entry.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_enviar_cliente.grid(row=8, column=0, columnspan=2, pady=10)

    def mostrar_info_cliente3(self, remitente_nombre, remitente_cedula, remitente_telefono, destinatario_nombre, destinatario_cedula, destinatario_telefono):
        
        if not (remitente_nombre.isalpha() and destinatario_nombre.isalpha()):
            messagebox.showerror("Error", "Los campos de *Nombre* no deben estar vacios y aparta deben ser solo Letras.")
            return
        if not remitente_telefono.isdigit() or not remitente_cedula.isdigit() or not destinatario_cedula.isdigit() or not destinatario_telefono.isdigit():
            messagebox.showerror("Error", "No se permite letras en la casillas de *Cedula* y *Telefono*, dejar casillas vacías o caracteres especiales, solo números enteros.")
            return
        
        info_text_cliente = "\nInformación del Remitente:\n"
        info_text_cliente += f"Nombre: {remitente_nombre}\n"
        info_text_cliente += f"Cédula: {remitente_cedula}\n"
        info_text_cliente += f"Teléfono: {remitente_telefono}\n"

        info_text_cliente += "\nInformación del Destinatario:\n"
        info_text_cliente += f"Nombre: {destinatario_nombre}\n"
        info_text_cliente += f"Cédula: {destinatario_cedula}\n"
        info_text_cliente += f"Teléfono: {destinatario_telefono}"

        #se crea el objeto de tipo documento
        DocumentoAEnviar = Documento()
  
        valores.append(DocumentoAEnviar)
        remitente = Cliente(remitente_nombre,remitente_cedula,remitente_telefono)

        valores.append(remitente)
        destinatario = Destinatario(destinatario_nombre,destinatario_cedula,destinatario_telefono)
     
        valores.append(destinatario)

        messagebox.showinfo("Información del Cliente", info_text_cliente)

        self.frame.pack_forget()

        #Segundo Frame Detalles Envio
        nuevo_frame = tk.Frame(self, width=800, height=800, bg="blue", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame.grid(row=0, column=0, pady=10)

        nuevo_frame_2 = tk.Frame(self, width=800, height=800, bg="#739072", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame_2.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Detalles Del Envio", font=("Helvetica", 16), bg="#739072", fg="white")
        label_nuevo_frame_2.grid(row=0, column=0, pady=10, columnspan=2)

        descripcion_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Por favor selecciona la ciudad desde la que envias tu Documento y a cual deseas enviarlo.", bg="#739072", fg="white")
        descripcion_nuevo_frame_2.grid(row=1, column=0, pady=10,columnspan=2)

        ciudades_origen = ["Medellin Norte", "Medellin Sur","Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_origen_label = tk.Label(nuevo_frame_2, text="Ciudad de Origen:", bg="#739072", fg="white")
        ciudad_origen_label.grid(row=2, column=0, pady=5, sticky="e")
        ciudad_origen_var = tk.StringVar()
        ciudad_origen_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_origen_var, *ciudades_origen)
        ciudad_origen_dropdown.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        ciudades_destino = ["Medellin Norte", "Medellin Sur","Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_destino_label = tk.Label(nuevo_frame_2, text="Ciudad de Destino:", bg="#739072", fg="white")
        ciudad_destino_label.grid(row=3, column=0, pady=5, sticky="e")
        ciudad_destino_var = tk.StringVar()
        ciudad_destino_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_destino_var, *ciudades_destino)
        ciudad_destino_dropdown.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        labelTransporte = tk.Label(nuevo_frame_2,text="Tipo De Transporte:", bg="#739072", fg="white")
        labelTransporte.grid(row=4,column=0,pady=5,sticky="e")

        Transporte_lista = ["Camión","Avión"]
        Transporte_lista_var = tk.StringVar()
        Transporte_lista_menu = tk.OptionMenu(nuevo_frame_2, Transporte_lista_var, *Transporte_lista)
        Transporte_lista_menu.grid(row=4,column=1,pady=5,padx=5,sticky="w")

        labelPago = tk.Label(nuevo_frame_2,text="Método de pago:", bg="#739072", fg="white")
        labelPago.grid(row=5,column=0,pady=5,sticky="e")

        pago_lista = ["Pago total","Pago Fraccionado", "Pago contraentrega"]
        pago_lista_var = tk.StringVar()
        pago_lista_menu = tk.OptionMenu(nuevo_frame_2, pago_lista_var, *pago_lista)
        pago_lista_menu.grid(row=5,column=1,pady=5,padx=5,sticky="w")

        boton_enviar_2 = tk.Button(nuevo_frame_2, text="Enviar", command=lambda:self.enviar_detalle_documento(ciudad_origen_var.get(),ciudad_destino_var.get(),Transporte_lista_var.get(),pago_lista_var.get()), bg="#3A4D39",font=("arial", 11, "bold"),fg="white")
        boton_enviar_2.grid(row=6, column=0, columnspan=2, pady=10)

 


#AYUDAR KEVIN

    def enviar_detalle_documento(self,origen,destino,transporte,pago):
        origen = origen
        destino = destino
        transporte = transporte
        pago = pago



        sucursales = Sucursal._todasLasSucursales
        origen = origen
        for i in sucursales:
            if i._nombre == origen:
                valores.append(i)
                camiones = i.getCamionesEnSucursal()

                aviones = i.getAvionesEnSucursal()

            if transporte == "Camión":
                    transporteT = camiones[0]
            if transporte == "Avión":
                    transporteT = aviones[0]
            

        destino = destino
        for k in sucursales:
            if k._nombre == destino:
                valores.append(k)
            
        if pago == "Pago contraentrega":
                pagoTipo = Guia.tipoDePago.DESTINATARIO
        if pago == "Pago total":
                pagoTipo = Guia.tipoDePago.REMITENTE
        if pago == "Pago Fraccionado":
                pagoTipo = Guia.tipoDePago.FRACCIONADO

        valores.append(pagoTipo)


        valores.append(transporteT)





        #Se va crear la guia del paquete que se envió
        guiaDocumentoAEnviar = Guia(valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])


        #Se añade el paquete que se creó a la sucursal de origen
        #se verifica si es necesario pagar para enviar

        if (guiaDocumentoAEnviar.getTipoDePago() == Guia.tipoDePago.DESTINATARIO):
            valores[3].getInventario().append(valores[0])


        else:
            if (guiaDocumentoAEnviar.getPagoPendiente == 0):
                  valores[3].getInventario().append(valores[0])
            else:
                 pass
                  
                  




        if origen and destino != None:
             #ACA VA LA GUIA
            tipo_producto = "Documento"
            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Código del paquete: {valores[0].getCodigo()}\n"
            info_text += f"Ciudad De Origen: {origen} \n"
            info_text += f"Ciudad De Destino: {destino} \n"
            info_text += f"Tipo de pago: {pago} \n"
            info_text += f"Precio total: ${guiaDocumentoAEnviar.getPrecioTotal()}\n"
            info_text += f"Vehículo: {transporte}"

            messagebox.showinfo("Los detalles del envío han sido enviados con éxito.", info_text)
        Enviar.destroy(self)
        valores.clear()