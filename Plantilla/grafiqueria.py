import tkinter as tk
from Juego import juego
from PIL import Image, ImageTk 
from matematiqueria import ubicar

@staticmethod
def etiquetado(i:int, j:int, root, func):
    label = tk.Label(root, width=4, height=2, relief="solid", borderwidth=3)
    label.grid(row=i, column=j)
    label.bind("<Button-1>", func)
    return label
@staticmethod
def etiquetados(v, func, d:tuple):
    return [[etiquetado(i,j, v, func) for j in range(d[1] )] for i in range(d[0])]

@staticmethod
def ventor(v, txt='Mi ventana'):
 # Configurar el título de la ventana
    v.title(txt)
# Configurar las dimensiones de la ventana
    v.geometry("800x600")
# Configurar el tamaño mínimo y máximo de la ventana para evitar deformación
    v.minsize(800, 600)
    v.maxsize(1200, 900) 
    v.resizable(True, True)
    v.config(bg="beige")


#Las siguientes 3 funciones llenan las casillas con los iconos de la ficha, a nivel general, ficha-bando e individual respectivamente
@staticmethod
def asignarImagen(casilla, img, t):
    img=img.resize((30,30), Image.LANCZOS )
    img=ImageTk.PhotoImage(image=img)
    #Asignar Imagen y Texto
    casilla.config(image=img, text=t, width=30, height=32)
    casilla.image=img 

@staticmethod
def graficarFicha(labels, img, lis, t):
    for i in lis:
        asignarImagen(ubicar(labels, i), img, t)
    
@staticmethod
def graficar(ju:juego, labels, imagos):
    for i in range(len(imagos)):
        for j in imagos[i].keys():
            graficarFicha(labels, imagos[i][j], ju.coors[i][j], str(i)+' '+str(j) )

@staticmethod
#Cambiar el color 
def recolorear(imago, col):
    pass

@staticmethod
def recolorearEnlistado(imago, cs):
    l=[]
    for c in cs:
        l.append(recolorear(imago, c))
    return l

@staticmethod
def graficarMovimientosPosibles(labels, movimientos):
    for mov in movimientos:
        fila, columna = mov
        casilla = labels[fila][columna]
        casilla.config(bg='turquoise')

@staticmethod
def restaurarMovimientos(labels, movs):
    for mov in movs: #restaurar el estado original de las casillas con posibles movimientos
        fila, columna = mov
        casilla = labels[fila][columna]
        casilla.config(bg="SystemButtonFace")

def fin(st):
        fin=tk.Toplevel()
        fin.title("Fin del Juego")
        fin.geometry("600x450")
        st+=' GANAN'
        label = tk.Label(fin, text=st, bg="lightgreen", font=("Helvetica", 16))
        label.pack(fill=tk.BOTH, expand=True)
        fin.mainloop()
