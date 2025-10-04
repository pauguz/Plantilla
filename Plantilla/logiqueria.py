import matematiqueria as mat

#Motorizador
def expansion(d, fd=mat.MovimientosRectos, ra=None):
    def respuesta(i, prueba):
        return mat.MovimientosPosibles(i, prueba, d, fd, ra)
    return respuesta