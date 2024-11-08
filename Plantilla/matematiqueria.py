direccionales=[[(1,0), (-1,0)], [(0,1), (0,-1)]]

@staticmethod
def coordenar(numero:int, unidad:int):
    return (numero//unidad, numero%unidad)

@staticmethod
def coordenarEnlistado(unidad:int, *args ):
    lis=[]
    for i in args:
        lis.append(coordenar(i, unidad))
    return lis

@staticmethod
def listador(dim:int):
    lisB=[]
    lisN=[]
    media=dim//2
    medium=(dim**2)//2
    #Llenar con Fichas negras
    for i in range(media-2, media+3):
        k=i*dim
        lisN.extend(coordenarEnlistado(dim, i, medium*2-i, k, medium*2-k))
    lisN.extend(coordenarEnlistado(dim, dim+media, 2*medium-media*3-1, (media)*dim+1, (media+1)*dim-2) )
    lisN={1:lisN}

    #Llenar con Fichas blancas  
    for i in range(-2,3):
        j=2-abs(i)
        for k in range (medium+i*dim-j,medium+i*dim+j+1):
            lisB.append(coordenar(k, dim))
    r=lisB.pop(6)
    lisB={1:lisB, 0:[r]}
    return [lisN, lisB]

@staticmethod
def ubicar(labels, dup:tuple):
    return labels[dup[0]][dup[1]]

@staticmethod
def SumaDupla(dup1:tuple, dup2:tuple):
    return tuple(a + b for a, b in zip(dup1, dup2))

@staticmethod
def MultDupla(dup:tuple, f:float):
    return tuple( int(x*f) for x in dup)

@staticmethod
def getPaso(dup1:tuple, dup2:tuple):
    paso= SumaDupla( MultDupla(dup1, -1), dup2 )
    a=(paso[0]==0) or (paso[1]==0)
    b=(paso[0]!=paso[1])
    if (a and b):
        while(abs(paso[0]+paso[1])!=1):
            paso=MultDupla(paso, 0.5)
        return paso
    
@staticmethod
def Comprobar(pos:tuple, eje:int, func, p:bool=False,n:bool=False):
    vec=[SumaDupla(pos, i) for i in direccionales[eje]]
    if not p:
        p=func(pos, vec[0])
    if not n:
        n=func(pos, vec[1])
    return p and n 
    
@staticmethod
def Mover(inicio, destino, func):
    paso=getPaso(inicio, destino)
    if(paso!=None):
        while(inicio != destino):
            inicio=SumaDupla(inicio, paso)
            if (func(inicio) ):
                return False
        print("Destino: ")
        print(inicio)
        return True



@staticmethod
def MovimientosPosibles(inicio, func):
    d=direccionales[0] + direccionales[1]
    movimientosPosibles = []
    for direccion in d:
        puedoAgregar = True
        i = 1  # Para ir avanzando en la dirección
        while puedoAgregar:
            # Calcular el nuevo fin sumando la dirección multiplicada por la iteración
            fin = SumaDupla(inicio, MultDupla(direccion, i))
            # Verificar si se puede mover al nuevo fin
            puedoAgregar = not func(fin)
            if puedoAgregar:
                movimientosPosibles.append(fin)  # Agregar el movimiento posible
            i += 1  # Aumentar la distancia en esa dirección
    return movimientosPosibles

@staticmethod
def Dimendor(d):
    if d.isdigit():
        d=int(d)
        return d>=9 and d%2==1
    return False