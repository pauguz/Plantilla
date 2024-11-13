import matematiqueria as mat

#Motorizador
def expansion(d, fd=mat.MovimientosRectos):
    def respuesta(i, prueba):
        return mat.MovimientosPosibles(i, prueba, d, fd)
    return respuesta