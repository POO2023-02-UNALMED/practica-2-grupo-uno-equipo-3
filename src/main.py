import tkinter as tk
from tkinter import *
from gestorGrafico.principal import Principal

from gestorGrafico.inicio import Inicio

class MainWindow(Tk):
    def __init__(self):
        super().__init__()
        self.title("Correminas")
        self.resizable(0,0)
        self.geometry("865x480")
        Inicio(self)
        self.mainloop()

    def abrirPrincipal(self):
        self.destroy()         
        Principal()

if __name__=="__main__":

    MainWindow()