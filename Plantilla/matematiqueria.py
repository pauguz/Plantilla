import tkinter as tk

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
def vikilista(dim:int):
    lisB=[]
    lisN=[]
    media=dim//2
    medium=(dim**2)//2
    #Llenar con Fichas negras
    for i in range(media-2, media+3):
        k=i*dim
        lisN.extend(coordenarEnlistado(dim, i, medium*2-i, k, medium*2-k))
    lisN.extend(coordenarEnlistado(dim, dim+media, 2*medium-media*3-1, (media)*dim+1, (media+1)*dim-2) )
    lisN={0:lisN}
    #Llenar con Fichas blancas  
    for i in range(-2,3):
        j=2-abs(i)
        for k in range (medium+i*dim-j,medium+i*dim+j+1):
            lisB.append(coordenar(k, dim))
    r=lisB.pop(6)
    lisB={0:lisB, 1:[r]}
    return [lisN, lisB]

def grecolista(d, l=False):
    lisB=[]
    lisN=[]
    for i in range(d):
        lisN.append((0, i) )
        lisB.append((7,i))
    lisB={0:lisB}
    lisN={0:lisN}
    if l:
        lisB.update({1:[(6, 1)]})
        lisN.update({1:[(1, d-1)]})
    return [lisN, lisB]

@staticmethod
def ubicar(labels, dup:tuple):
    return labels[dup[0]][dup[1]]

@staticmethod
def obtener_Contenido(lab: tk.Label):
    return list(map (int, lab.cget("text").split()))

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

def Extraer(labels:list, m):
    struct=m
    for i in range(labels.__len__):
        for j in range(len(i)):
            t=obtener_Contenido(labels[i][j])
            if t :
                labels[t[0]][t[1]]=(i,j)
    return struct

#Los siguientes 4 metodos determinan el movimiento hacia una casilla, hacia una linea o hacia un conjunto de lineas rectas respectivamente
@staticmethod
def MovimientoUnico(d, inicio, func):
        fin = SumaDupla(inicio, d)
        # Verificar si se puede mover al nuevo fin
        puedoAgregar = not func(fin)
        if puedoAgregar:
            return [fin] 
        return []

@staticmethod
def MovimientosRectos(d, inicio, func, r=None):
    if r:
        return MovimientosRectosRango(d, inicio, func, r)
    movs=[]
    puedoAgregar = True
    while puedoAgregar:
        fin=MovimientoUnico(d, inicio, func)
        puedoAgregar=bool(fin)
        if puedoAgregar:
            movs.extend(fin)
            inicio=fin[0]
    return movs

def MovimientosRectosRango(d, inicio, func, r:int):
    movs=[]
    puedoAgregar = True
    while puedoAgregar and len(movs) <r:
        fin=MovimientoUnico(d, inicio, func)
        puedoAgregar=bool(fin)
        if puedoAgregar:
            movs.extend(fin)
            inicio=fin[0]
    return movs  

@staticmethod
def MovimientosPosibles(inicio, funcprueba, d=None, funcdireccion=MovimientosRectos, r=None):
    if(d is None):
        d=direccionales[0]+direccionales[1]
    movs = []
    for direccion in d:
        movs.extend(funcdireccion(direccion, inicio, funcprueba, r))
    return movs

@staticmethod
def Dimendor(d):
    if d.isdigit():
        d=int(d)
        return d>=9 and d%2==1
    return False