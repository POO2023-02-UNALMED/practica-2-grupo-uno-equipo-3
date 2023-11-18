import tkinter as tk
from tkinter import *

class Pagar(Frame): 
    def __init__(self, ventana):
        super().__init__(ventana)
        self.config(highlightbackground="#085870", highlightthickness=3)
        self.pack(expand=True)
    
        self.Label_Titulo = tk.Label(self, text="Pagar", font=("Arial", 30))
        self.Label_Titulo.grid(row=0, column=0, columnspan=2, pady=10)

        self.Label_descripcion = tk.Label(self, text="En esta funcionalidad podrás escoger la manera de pagar tu envío")
        self.Label_descripcion.grid(row=1, column=0, columnspan=2, pady=10)