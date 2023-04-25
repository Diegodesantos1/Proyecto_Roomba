from tkinter import *
from tkinter import ttk

class Ventana(Tk):
    def __init__(self,titulo,color ="white",geometria="537x250"):
        Tk.__init__(self)
        self.title(titulo)
        self.geometry(geometria)
        self.configure(background=color)
    def ocultar(self):
        self.withdraw()
    def mostrar(self):
        self.deiconify()