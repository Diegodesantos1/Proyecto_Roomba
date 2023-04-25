import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from clases.Pestana import Pestana
from clases.Robot import Robot
from clases.Ventana import Ventana

class Principal2():
  def __init__(self,principal):
    self.principal=principal
    self.window=Ventana("Hagamos una Roomba")
    self.window.protocol("WM_DELETE_WINDOW", self.volver)
    self.roomba=Robot("Rumba",2)
    self.pestadicionales = []
    self.zonas=[]
    self.nb = ttk.Notebook(self.window)
    self.nb.pack(fill="both", expand="yes")
    color="white"
    self.pl = Frame(self.nb, background=color)
    self.nb.add(self.pl, text="Zonas")
    self.lbl = Label(self.pl, text="¿Cuántas zonas quieres limpiar?", bg=color,fg="black")
    self.lbl.grid(column=6, row=0)
    self.spin = Spinbox(self.pl, from_=1, to=20)
    self.spin.grid(column=6, row=1)

    self.btn = Button(self.pl, text="Continuar", command=self.creasalas)
    self.btn2 = Button(self.window, text="Calcular", command=self.calcula)
    self.btn.grid(column=6, row=3)
    self.window.mainloop()

  def volver(self):
    self.principal.deiconify()
    self.window.destroy()

  def creasalas(self):
      numerosalas = int(self.spin.get())
      for i in range(numerosalas):
          pestaux = Pestana(self.nb)
          nombre="Sala " + str(i+1)
          self.nb.add(pestaux.pl, text=nombre)
          self.pestadicionales.append(pestaux)
      self.pl.destroy()
      self.btn2.pack()

  def calcula(self):
      superficie=0
      for pest in self.pestadicionales:
          ancho=int(pest.spinancho.get())
          largo=int(pest.spinlargo.get())
          self.zonas.append({"largo":largo,"ancho":ancho})
          superficie+=(ancho*largo)
      messagebox.showinfo(message="La superficie a limpiar es de: " + str(superficie) + " metros cuadrados", title="Superficie total")
      messagebox.showinfo(self.roomba.nombre,"El tiempo estimado es: "+str(self.roomba.tiempoLimpiezaEnMinutos(superficie)) + " minutos")