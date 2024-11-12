from Interfaz import ventor, vista
from Ficha import ficha
#from Ficha import ficha
from Juego import juego
import tkinter as tk
import grafiqueria as grf
import matematiqueria as mat
#Creando fichas 
#dama=ficha(mt.diagonal, 'circulo.png')

def pruebavikinga(d=11):
#Creando fichas
    soldado=ficha(mat.MovimientosPosibles)
    rey=ficha(mat.MovimientosPosibles)
    #Disposicion
    dispin=mat.vikilista(d)
    j=juego(coors=dispin,fichas=[rey, soldado], v=d)
    imgs=[ {1:'vikingonegro.png'} , {0:'reg.png', 1:'vikingoblanco.png'} ]
    v=vista(j, imgs=imgs)
    v.ventana.mainloop()

def pruebainca():
    v=tk.Tk()
    ventor(v)
    grf.etiquetados(v, None, (7,5))
    k=v.winfo_children()
    for c in k:
        coor=(c.grid_info().get('row', None), c.grid_info().get('column', None))
        if coor[0]==1 and (coor[1]==0 or coor[1]==4):
            c.destroy()
    v.mainloop()

def pruebagreca(d=8):
    hoplita=ficha(mat.MovimientosPosibles)
    dispin=mat.grecolista(d)
    j=juego(coors=dispin, fichas=[hoplita], v=8, h=d )
    imgs=[ {1:'vikingonegro.png'} , {1:'vikingoblanco.png'} ]
    v=vista(j, imgs=imgs)
    v.ventana.mainloop()

pruebavikinga()

