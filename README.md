<h1 align="center">Roomba</h1>

<h3 align="center">Perfiles de GitHub de los autores de este proyecto:</h3>

1. [@jmedina28](https://github.com/jmedina28)
2. [@diegodesantos1](https://github.com/Diegodesantos1)

---
En este [repositorio](https://github.com/jmedina28/Proyecto_Roomba) quedan resuelta la práctica del Roomba con interfaz gráfica implementada.
***
<h1 align="center">Plano de la habitación</h1>

![image](https://user-images.githubusercontent.com/91721855/217007202-9db6ed32-7abc-49f4-9fbc-7a6f7ed2a66c.png)

Para la realización de este proyecto hemos tenido que estudiar la documentación de Tkinter para luego poder desarrollar nuestra interfaz gráfica.

El código empleado para resolverlo es el siguiente:

<h1 align="center">Main</h1>

```python
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
```

<h1 align="center">Ventana principal</h1>

```python
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
```


<h1 align="center">Pestaña para introducir tamaños</h1>

```python
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
```

<h1 align="center">Clase Robot</h1>

```python
class Robot():
  def __init__(self, nombre,tiempo):
    self.nombre=nombre
    self.tiempo=tiempo
  def tiempoLimpiezaEnMinutos(self,superficieALimpiar):
    return round(superficieALimpiar*self.tiempo)
```

<h1 align="center">Cálculo de las zonas</h1>

![image](https://user-images.githubusercontent.com/91721855/219479894-7963c022-7eaa-43d9-a1a3-29426cf18b80.png)

```python
class Lugar():
    def __init__(self,dimension,posicion={"posx":0,"posy":0}):
        self.posicion=posicion
        self.dimension=dimension

class Sala(Lugar):
    def __init__(self,dimension,obstaculo):
        Lugar.__init__(self,dimension)
        self.obstaculo=obstaculo
    def crear_zonas(self):
        zona1=Zona({"ancho":self.obstaculo.posicion.get("posx")-self.posicion.get("posx"),"largo":self.dimension.get("largo")})
        zona2=Zona({"ancho":self.obstaculo.dimension.get("ancho"),"largo":self.obstaculo.posicion.get("posy")-self.posicion.get("posy")},{"posx":self.obstaculo.posicion.get("posx"),"posy":0})
        zona3=Zona({"ancho":self.obstaculo.dimension.get("ancho"),"largo":self.dimension.get("largo")-(self.obstaculo.posicion.get("posy")+self.obstaculo.dimension.get("largo"))},{"posx":self.obstaculo.posicion.get("posx"),"posy":self.obstaculo.posicion.get("posy")+self.obstaculo.dimension.get("largo")})
        zona4=Zona({"ancho":self.dimension.get("ancho")-(self.obstaculo.posicion.get("posx")+self.obstaculo.dimension.get("ancho")),"largo":self.dimension.get("largo")},{"posx":self.obstaculo.posicion.get("posx")+self.obstaculo.dimension.get("ancho"),"posy":0})
        zonas=[]
        if zona1.area() !=0:
            zonas.append(zona1)
        if zona2.area() !=0:
            zonas.append(zona2)
        if zona3.area() !=0:
            zonas.append(zona3)
        if zona4.area() !=0:
            zonas.append(zona4)
        return zonas


class Zona(Lugar):
    def __init__(self,dimension,posicion={"posx":0,"posy":0}):
        Lugar.__init__(self,dimension,posicion)
    def area(self):
        area=self.dimension.get("ancho")*self.dimension.get("largo")
        return area
```
<h1 align="center">Tamaño de la Interfaz Gráfica</h1>

![image](https://user-images.githubusercontent.com/91721855/219479841-a2597ccd-21e3-4c8a-af0f-af97f6b1a678.png)

```python
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
```
<h1 align="center">Ejemplo y resultados</h1>
En este ejemplo tomando 5 zonas con medidas aleatorias y estableciendo un tiempo de limpieza por metro cuadrado de 2 minutos obtenemos los siguientes resultados.

![image](https://user-images.githubusercontent.com/91721855/219480082-d67fbdd2-0b94-4952-ae56-a00433aad156.png)

![image](https://user-images.githubusercontent.com/91721855/219480186-131d651b-7e37-47e2-9a3f-d3a5724e3b76.png)

![image](https://user-images.githubusercontent.com/91721855/219480217-e141e2c5-1e20-4a3a-acfa-4679e5a8aa4d.png)

![image](https://user-images.githubusercontent.com/91721855/219480249-33f85440-12f1-4da7-922c-f1cdb668cdc0.png)

![image](https://user-images.githubusercontent.com/91721855/219480292-a4ab759b-077f-4ed2-96e3-57df7fe81b88.png)

![image](https://user-images.githubusercontent.com/91721855/219480350-3a64bc8b-dd81-422d-9586-5326bf35d774.png)

![image](https://user-images.githubusercontent.com/91721855/219480381-c6cdadbc-cb59-4d0f-b5ae-038beb3231be.png)






