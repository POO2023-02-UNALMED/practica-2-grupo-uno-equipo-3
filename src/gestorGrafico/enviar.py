import tkinter as tk
from tkinter import PhotoImage, messagebox

from gestorAplicacion.productos.paquete import Paquete

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

#ESTAS 2 LINEA SERA PARA QUE SIRVIERA. NO SIRVE.
        self.ciudad_origen_var = tk.StringVar()
        self.ciudad_destino_var = tk.StringVar()

        self.config(width=1000, height=1000, highlightbackground="#085870", highlightthickness=3)
        self.pack(expand=True)

        self.frame = tk.Frame(self, width=800, height=800, bg="green", highlightbackground="#085870", highlightthickness=5)
        self.frame.pack(expand=True)

        self.titulo_label = tk.Label(self.frame, text="Enviar Paquete", font=("Helvetica", 16), fg="white", bg="#085870")
        self.titulo_label.grid(row=0, column=0, columnspan=3, pady=10)

        self.texto_bienvenida = "Hola, bienvenido a nuestro programa \"CorreMinas\".\n\nEstás en el apartado de enviar un paquete. ¿Qué tipo de paquete deseas enviar?\n \nElige una de las siguientes opciones:"
        self.bienvenida_label = tk.Label(self.frame, text=self.texto_bienvenida, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label.grid(row=1, column=0, columnspan=3, pady=10)

        self.boton_paquete = tk.Button(self.frame, text="Paquete", command=self.mostrar_ventana_paquete)
        self.boton_paquete.grid(row=2, column=0,  pady=5, padx=5)
        # imagenPaquete = PhotoImage(file=f"src\gestorGrafico\imagenes\iconos\paquete.png")
        # self.boton_paquete.config(image=imagenPaquete)
   

        self.boton_animal = tk.Button(self.frame, text="Animal", command=self.enviar_animal)
        self.boton_animal.grid(row=2, column=1, pady=5, padx=5)
        # imagenAnimal = PhotoImage(file=f"src\gestorGrafico\imagenes\iconos\animal.png")  
        # self.boton_animal.config(image=imagenAnimal)

        self.boton_documento = tk.Button(self.frame, text="Documento", command=self.enviar_documento)
        self.boton_documento.grid(row=2, column=2, pady=5, padx=5)
        # imagenDocumento = PhotoImage(file=f"src\gestorGrafico\imagenes\iconos\documento.png")  
        # self.boton_documento.config(image=imagenDocumento)

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

        fragilLabel = tk.Label(self.frame, text="¿Es fragil?")
        fragilLabel.grid(row=7,column=0,pady=10, sticky="e")

        fragilSioNo = ["Si", "No"]
        fragilSioNo_var = tk.StringVar()
        fragilSioNo_dropdown = tk.OptionMenu(self.frame, fragilSioNo_var, *fragilSioNo)
        fragilSioNo_dropdown.grid(row=7, column=1, pady=5, padx=5, sticky="w")

        boton_enviar = tk.Button(self.frame, text="Enviar", command=lambda: self.mostrar_info_emergente(peso_entry.get(), alto_entry.get(), ancho_entry.get(), largo_entry.get(), valor_declarado_entry.get()))
        boton_enviar.grid(row=8, column=0, columnspan=2, pady=10)

        #NECESITO OBTENER EL VALOR DE LOS ENTRY EN INT O FLOAT PERO ME GENERA ERROR
        paqueteEnviar = Paquete(peso_entry.get(),alto_entry.get(),ancho_entry.get(),largo_entry.get(),fragilSioNo_var.get(), valor_declarado_entry.get())
        print(paqueteEnviar)
    
    # def obtenerValorSioNo():
    #     valorSeleccionado = variable_opcion.get()

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

            # Oculta el frame actual para poder crear uno ahorita mas adelante
            self.frame.pack_forget()

            # Crea y muestra un nuevo frame  (que bendicion)
            nuevo_frame = tk.Frame(self, width=800, height=800, bg="blue", highlightbackground="#085870", highlightthickness=5)
            nuevo_frame.grid(row=0, column=0, sticky="nsew")

            label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), fg="white", bg="blue")
            label_nuevo_frame.grid(row=0, column=0, pady=10)

            self.texto_bienvenida2 = "Por favor diligencie los siguientes datos."
            self.bienvenida2_label = tk.Label(nuevo_frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="blue")
            self.bienvenida2_label.grid(row=1, column=0, columnspan=3, pady=10)

            remitente_nombre_label = tk.Label(nuevo_frame, text="Nombre del Remitente:")
            remitente_nombre_label.grid(row=2, column=0, pady=5, sticky="e")

            remitente_cedula_label = tk.Label(nuevo_frame, text="Cédula del Remitente:")
            remitente_cedula_label.grid(row=3, column=0, pady=5, sticky="e")

            remitente_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Remitente:")
            remitente_telefono_label.grid(row=4, column=0, pady=5, sticky="e")

            remitente_nombre_entry = tk.Entry(nuevo_frame)
            remitente_nombre_entry.grid(row=2, column=1, pady=5, padx=5, sticky="w")

            remitente_cedula_entry = tk.Entry(nuevo_frame)
            remitente_cedula_entry.grid(row=3, column=1, pady=5, padx=5, sticky="w")

            remitente_telefono_entry = tk.Entry(nuevo_frame)
            remitente_telefono_entry.grid(row=4, column=1, pady=5, padx=5, sticky="w")

            destinatario_nombre_label = tk.Label(nuevo_frame, text="Nombre del Destinatario:")
            destinatario_nombre_label.grid(row=5, column=0, pady=5, sticky="e")

            destinatario_cedula_label = tk.Label(nuevo_frame, text="Cédula del Destinatario:")
            destinatario_cedula_label.grid(row=6, column=0, pady=5, sticky="e")

            destinatario_telefono_label = tk.Label(nuevo_frame, text="Teléfono del Destinatario:")
            destinatario_telefono_label.grid(row=7, column=0, pady=5, sticky="e")

            destinatario_nombre_entry = tk.Entry(nuevo_frame)
            destinatario_nombre_entry.grid(row=5, column=1, pady=5, padx=5, sticky="w")

            destinatario_cedula_entry = tk.Entry(nuevo_frame)
            destinatario_cedula_entry.grid(row=6, column=1, pady=5, padx=5, sticky="w")

            destinatario_telefono_entry = tk.Entry(nuevo_frame)
            destinatario_telefono_entry.grid(row=7, column=1, pady=5, padx=5, sticky="w")

            boton_enviar_cliente = tk.Button(nuevo_frame, text="Enviar", command=lambda: self.mostrar_info_cliente(remitente_nombre_entry.get(), remitente_cedula_entry.get(), remitente_telefono_entry.get(), destinatario_nombre_entry.get(), destinatario_cedula_entry.get(), destinatario_telefono_entry.get()))
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

        messagebox.showinfo("Información del Cliente", info_text_cliente)

        self.frame.pack_forget()

        #Segundo Frame Detalles Envio
        nuevo_frame = tk.Frame(self, width=800, height=800, bg="blue", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame = tk.Label(nuevo_frame, text="Informacion Cliente", font=("Helvetica", 16), fg="white", bg="blue")
        label_nuevo_frame.grid(row=0, column=0, pady=10)

        nuevo_frame_2 = tk.Frame(self, width=800, height=800, bg="red", highlightbackground="#085870", highlightthickness=5)
        nuevo_frame_2.grid(row=0, column=0, sticky="nsew")

        label_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Detalles Del Envio", font=("Helvetica", 16), fg="white", bg="red")
        label_nuevo_frame_2.grid(row=0, column=0, pady=10, columnspan=2)

        descripcion_nuevo_frame_2 = tk.Label(nuevo_frame_2, text="Por favor selecciona la ciudad desde la que envias tu producto y a cual deseas enviarlo.", font=("Helvetica", 12), fg="white", bg="red")
        descripcion_nuevo_frame_2.grid(row=1, column=0, pady=10,columnspan=2)

        ciudades_origen = ["Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_origen_label = tk.Label(nuevo_frame_2, text="Ciudad de Origen:")
        ciudad_origen_label.grid(row=2, column=0, pady=5, sticky="e")
        ciudad_origen_var = tk.StringVar()
        ciudad_origen_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_origen_var, *ciudades_origen)
        ciudad_origen_dropdown.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        ciudades_destino = ["Bogota Norte", "Bogota Sur", "Cali Norte", "Cali Sur", "Pasto Norte", "Pasto Sur"]
        ciudad_destino_label = tk.Label(nuevo_frame_2, text="Ciudad de Destino:")
        ciudad_destino_label.grid(row=3, column=0, pady=5, sticky="e")
        ciudad_destino_var = tk.StringVar()
        ciudad_destino_dropdown = tk.OptionMenu(nuevo_frame_2, ciudad_destino_var, *ciudades_destino)
        ciudad_destino_dropdown.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        labelTransporte = tk.Label(nuevo_frame_2,text="Tipo De Transporte:")
        labelTransporte.grid(row=4,column=0,pady=5,sticky="e")

        Transporte_lista = ["Camión","Avíon"]
        Transporte_lista_var = tk.StringVar()
        Transporte_lista_menu = tk.OptionMenu(nuevo_frame_2, Transporte_lista_var, *Transporte_lista)
        Transporte_lista_menu.grid(row=4,column=1,pady=5,padx=5,sticky="w")

        labelPago = tk.Label(nuevo_frame_2,text="Método de pago:")
        labelPago.grid(row=5,column=0,pady=5,sticky="e")

        pago_lista = ["Pago total","Pago Fraccionado", "Pago contraentrega"]
        pago_lista_var = tk.StringVar()
        pago_lista_menu = tk.OptionMenu(nuevo_frame_2, pago_lista_var, *pago_lista)
        pago_lista_menu.grid(row=5,column=1,pady=5,padx=5,sticky="w")

        boton_enviar_2 = tk.Button(nuevo_frame_2, text="Enviar", command=self.enviar_detalle_envio)
        boton_enviar_2.grid(row=6, column=0, columnspan=2, pady=10)



#AYUDAR KEVIN
#NO SIRVE. AYUDA
    def enviar_detalle_envio(self):
        ciudad_origen = self.ciudad_origen_var.get()
        ciudad_destino = self.ciudad_destino_var.get()

        if ciudad_origen and ciudad_destino:
            tipo_producto = "Paquete"
            info_text = f"Tipo de producto: {tipo_producto}\n"
            info_text += f"Ciudad De Origen: {ciudad_origen} \n"
            info_text += f"Ciudad De Destino: {ciudad_destino} \n"

            messagebox.showinfo("Información del Paquete", info_text)
            messagebox.showinfo("Los detalles del envío han sido enviados con éxito.")


    def enviar_animal(self):
        self.bienvenida_label.grid_forget()
        self.boton_paquete.grid_forget()
        self.boton_animal.grid_forget()
        self.boton_documento.grid_forget()

        self.texto_bienvenida1 = "Has seleccionado Enviar un Animal."
        self.texto_bienvenida2 = "Para continuar deberá diligenciar los siguientes datos: "
        self.bienvenida_label1 = tk.Label(self.frame, text=self.texto_bienvenida1, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label1.grid(row=1, column=0, columnspan=2, pady=10)
        self.bienvenida_label2 = tk.Label(self.frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label2.grid(row=2, column=0, columnspan=2, pady=10)

        nombreAnimal_label = tk.Label(self.frame, text="Nombre del animal:")
        nombreAnimal_label.grid(row=3, column=0, pady=(10, 0), sticky="e")

        entryNombreAnimal = tk.Entry(self.frame)
        entryNombreAnimal.grid(row=3, column=1, pady=5, padx=5, sticky="w")

        edadAnimal_label = tk.Label(self.frame, text="Edad del animal:")
        edadAnimal_label.grid(row=4, column=0, pady=10, sticky="e")

        entryEdadAnimal = tk.Entry(self.frame)
        entryEdadAnimal.grid(row=4, column=1, pady=5, padx=5, sticky="w")

        pesoAnimal_label = tk.Label(self.frame, text="Ancho:")
        pesoAnimal_label.grid(row=5, column=0, pady=10, sticky="e")

        entryPesoAnimal = tk.Entry(self.frame)
        entryPesoAnimal.grid(row=5, column=1, pady=5, padx=5, sticky="w")
        
        tiposDeAnimales = ["Perro", "Gato", "Hamster", "Loro", "Caballo", "Vaca"]
        tiposDeAnimales_label = tk.Label(self.frame, text="Tipo de animal:", font=("arial",10))
        tiposDeAnimales_label.grid(row=6, column=0, pady=5, sticky="e")
        tipoDeAnimal_var = tk.StringVar()
        tipoDeAnimal_dropdown = tk.OptionMenu(self.frame, tipoDeAnimal_var, *tiposDeAnimales)
        tipoDeAnimal_dropdown.grid(row=6, column=1, pady=5, padx=5, sticky="w")

        botonSiguiente = tk.Button(self.frame,text="Siguiente", font=("arial",10))
        botonSiguiente.grid(row=7,column=0,columnspan=2,pady=5, padx=5)

        #falta colocar lo del usuario y ciudades después de esto

    def enviar_documento(self):
        self.bienvenida_label.grid_forget()
        self.boton_paquete.grid_forget()
        self.boton_animal.grid_forget()
        self.boton_documento.grid_forget()

        self.texto_bienvenida1 = "Has seleccionado Enviar un Documento."
        self.texto_bienvenida2 = "Para continuar deberá diligenciar los siguientes datos: "
        self.bienvenida_label1 = tk.Label(self.frame, text=self.texto_bienvenida1, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label1.grid(row=1, column=0, columnspan=2, pady=10)
        self.bienvenida_label2 = tk.Label(self.frame, text=self.texto_bienvenida2, font=("Helvetica", 12), justify="left", wraplength=380, fg="white", bg="green")
        self.bienvenida_label2.grid(row=2, column=0, columnspan=2, pady=10)
 

        #qué se pregunta acá? xd
        infoDoc_label = tk.Label(self.frame, text="Documento:")
        infoDoc_label.grid(row=3, column=0, pady=(10, 0), sticky="e")
