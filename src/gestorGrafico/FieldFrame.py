import tkinter as tk

class FieldFrame(tk.Frame):
    def __init__(self, ventana, tituloCriterio, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(ventana)
        
        self.tituloCriterio = tituloCriterio
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado

        if self.habilitado is None:
            self.habilitado = [True] * len(self.criterios)

        if self.valores is None:
            self.valores = [""] * len(self.criterios)

        # Crear una etiqueta para el título de criterios
        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio)
        label_titulo_criterio.grid(row=0, column=0)

        # Crear una etiqueta para el título de valores
        label_titulo_valores = tk.Label(self, text=self.tituloValores)
        label_titulo_valores.grid(row=0, column=1)

        # Iterar sobre los títulos de los criterios
        for i, titulo_criterio in enumerate(self.criterios, start=1):
            # Crear una etiqueta para el título del criterio
            label_criterio = tk.Label(self, text=titulo_criterio)
            label_criterio.grid(row=i, column=0)

            # Crear una entrada con el valor inicial
            entry = tk.Entry(self, state='normal' if self.habilitado[i-1] else 'disabled')
            entry.insert(0, self.valores[i-1])
            entry.grid(row=i, column=1)

        # Botón para aceptar y guardar los valores
        boton_aceptar = tk.Button(self, text="Aceptar", command=self.guardarValores)
        boton_aceptar.grid(row=i + 2, column=0, columnspan=1, padx=10)

        # Botón para limpiar el texto de las entradas
        boton_clear = tk.Button(self, text="Clear", command=self.limpiarTextos)
        boton_clear.grid(row=i + 2, column=1, columnspan=1, padx=10)

    def limpiarTextos(self):
        for entry_widget in self.grid_slaves(column=1):
            if isinstance(entry_widget, tk.Entry):
                entry_widget.delete(0, tk.END)

    def guardarValores(self):
        Valores = []
        for criterio in self.criterios:
            valor = self.getValue(criterio)
            Valores.append(valor)
            print(f"{criterio}: {valor}")
            

    def getValue(self, criterio):
        index = self.criterios.index(criterio)
        entry_widget = self.grid_slaves(row=index + 1, column=1)[0]
        return entry_widget.get()
    


                     



if __name__ == "__main__":
    root = tk.Tk()
  
    titulo_criterio = "Criterios"
    criterios = ["Criterio 1", "Criterio 2", "Criterio 3"]
    titulo_valores = "Valores"
    valores = [1234,13254,31235] 
    habilitado = None  
    
    field_frame = FieldFrame(root, titulo_criterio, criterios, titulo_valores, valores, habilitado)
    field_frame.pack()
    valor_criterio_2 = field_frame.getValue("Criterio 2")
    print(valor_criterio_2)
    

    root.mainloop()

