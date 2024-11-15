from Interfaz import vista
from Ficha import ficha
from Juego import juego
import tkinter as tk
import grafiqueria as grf
import matematiqueria as mat
import logiqueria as log

#Creando fichas 
#dama=ficha(mt.diagonal, 'circulo.png')

def pruebavikinga(d=11):
#Creando fichas
    soldado=ficha(mat.MovimientosPosibles)
    rey=ficha(mat.MovimientosPosibles)
    #Disposicion
    dispin=mat.vikilista(d)
    j=juego(coors=dispin,fichas=[rey, soldado], v=d)
    imgs=[  {1:'vikingonegro.png'}, {0:'reg.png', 1:'vikingoblanco.png'}  ]
    v=vista(j, imgs, 'Hnefatafl')
    v.ventana.mainloop()

def pruebainca():
    v=tk.Tk()
    grf.ventor(v, 'Taptana')
    grf.etiquetados(v, None, (7,5))
    k=v.winfo_children()
    for c in k:
        coor=(c.grid_info().get('row', None), c.grid_info().get('column', None))
        if coor[0]==1 and (coor[1]==0 or coor[1]==4):
            c.destroy()
    v.mainloop()

def pruebagreca(d=8):
    dir=[(1,1),(-1,-1),(-1,1),(1,-1)]
    dr=[(2,2),(-2,-2),(-2,2),(2,-2)]
    m=log.expansion(dir)
    hoplita=ficha(m)
    dispin=mat.grecolista(d)
    j=juego(coors=dispin, fichas=[hoplita], v=8, h=d )
    imgs=[ {0:'vikingonegro.png'} , {0:'vikingoblanco.png'} ]
    v=vista(j, imgs=imgs, nombre='Petteia')
    v.ventana.mainloop()



pruebagreca(12)