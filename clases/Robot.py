class Robot():
  def __init__(self, nombre,tiempo):
    self.nombre=nombre
    self.tiempo=tiempo
  def tiempoLimpiezaEnMinutos(self,superficieALimpiar):
    return round(superficieALimpiar*self.tiempo)