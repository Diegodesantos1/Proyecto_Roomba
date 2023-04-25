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