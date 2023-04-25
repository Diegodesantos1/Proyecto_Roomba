import tkinter
from tkinter import *

class Pestana():
    def __init__(self, nb,background="white"):
        self.pl = Frame(nb,background=background)
        self.lblancho = Label(self.pl, text="Ancho en metros")
        self.spinancho = Spinbox(self.pl, from_=1, to=100,increment=1)
        self.lbllargo = Label(self.pl, text="Largo en metros")
        self.spinlargo = Spinbox(self.pl, from_=1, to=100,increment=1)
        self.lbltiempo = Label(self.pl, text="Tiempo de limpieza en minutos por metro cuadrado")
        self.spintiempo = Spinbox(self.pl, from_=1, to=100,increment=1)
        self.lblancho.grid(column=0, row=0)
        self.spinancho.grid(column=1, row=0)
        self.lbllargo.grid(column=0, row=1)
        self.spinlargo.grid(column=1, row=1)
        self.lbltiempo.grid(column=0, row=2)
        self.spintiempo.grid(column=1, row=2)