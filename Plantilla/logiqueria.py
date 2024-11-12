import matematiqueria as mat

#Motorizador
def expansion(dir):
    def respuesta(i, func):
        return mat.MovimientosPosibles(i, func, dir)
    return respuesta