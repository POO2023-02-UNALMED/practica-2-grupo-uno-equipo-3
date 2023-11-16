import tkinter as tk
from tkinter import messagebox

class FieldFrame(tk.Frame):
    def __init__(self, ventana, tituloCriterio, criterios, tituloValores, valores=None, habilitado=None):
        super().__init__(ventana,width=500,height=500)
        
        self.tituloCriterio = tituloCriterio
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = valores
        self.habilitado = habilitado
        self.pulsado = False
        self.Valores = None
        self.pack()


        #self.config(width=300,height=300)

        if self.habilitado is None:
            self.habilitado = [True] * len(self.criterios)

        if self.valores is None:
            self.valores = [""] * len(self.criterios)

        # Crear una etiqueta para el título de criterios
        label_titulo_criterio = tk.Label(self, text=self.tituloCriterio,font=("Arial",10))
        label_titulo_criterio.grid(row=0, column=0,columnspan=6,sticky="w")

        # Crear una etiqueta para el título de valores
        label_titulo_valores = tk.Label(self, text=self.tituloValores,font=("Arial",10))
        label_titulo_valores.grid(row=0, column=6,columnspan=6,sticky="w")

        # Iterar sobre los títulos de los criterios
        for i, titulo_criterio in enumerate(self.criterios, start=1):
            # Crear una etiqueta para el título del criterio
            label_criterio = tk.Label(self, text=titulo_criterio)
            label_criterio.grid(row=i, column=0,columnspan=6,sticky="w")

            # Crear una entrada con el valor inicial
            entry = tk.Entry(self, state='normal' if self.habilitado[i-1] else 'disabled')
            entry.insert(0, self.valores[i-1])
            entry.grid(row=i, column=6,columnspan=6,sticky="w")

        # Botón para aceptar y guardar los valores
        boton_aceptar = tk.Button(self, text="Aceptar", command=self.guardarValores)
        boton_aceptar.grid(row=i + 4, column=0, columnspan=6, padx=10,pady=10,sticky="w")

        # Botón para limpiar el texto de las entradas
        boton_clear = tk.Button(self, text="Clear", command=self.limpiarTextos)
        boton_clear.grid(row=i + 4, column=6, columnspan=6, padx=10,pady=10,sticky="w")
    
    def getPulsado(self):
        return self.pulsado
    # Funciones para los Botones
    def limpiarTextos(self):
        for entry_widget in self.grid_slaves(column=6):
            if isinstance(entry_widget, tk.Entry):
                entry_widget.delete(0, tk.END)

    def guardarValores(self):
        self.Valores = []
        for criterio in self.criterios:
            valor = self.getValue(criterio)
            self.Valores.append(valor)
            print(criterio, type(valor) )
        self.pulsado = True
        self.limpiarTextos()
        print(self.pulsado)
        return self.Valores
            

    def getValue(self, criterio):
        index = self.criterios.index(criterio)
        entry_widget = self.grid_slaves(row=index + 1, column=6)[0]
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