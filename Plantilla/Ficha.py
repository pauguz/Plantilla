from PIL import Image
class ficha:
    def __init__(self, func):
        self.Movimiento=func()
    
    def puntuar(self, p:int):
        self.puntos=p
    
    