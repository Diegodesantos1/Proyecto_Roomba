import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from clases.Pestana import Pestana
from clases.Robot import Robot
from clases.Ventana import Ventana
from clases.Forma1 import Principal2



if __name__=="__main__":
    window=Ventana("Bienvenidos al gestor de Roombas")
    def ejecuccion_Principal2():
        window.withdraw()
        p=Principal2(window)
    btn2 = Button(window, text="Comenzar", command=ejecuccion_Principal2)
    btn2.place(relx=50, rely=100)
    btn2.pack()
    window.mainloop()