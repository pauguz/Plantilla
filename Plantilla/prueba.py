from Interfaz import ventor, vista
from Ficha import ficha
#from Ficha import ficha
from Juego import juego
import tkinter as tk
import grafiqueria as grf
import matematiqueria as mat
#Creando fichas 
#dama=ficha(mt.diagonal, 'circulo.png')


#Creando fichas
soldado=ficha(mat.MovimientosPosibles)
rey=ficha(mat.MovimientosPosibles)
#Disposicion
dispin=mat.listador(11)
j=juego(coors=dispin,fichas=[rey, soldado], v=11)
imgs=[ {1:'vikingonegro.png'} , {0:'reg.png', 1:'vikingoblanco.png'} ]
v=vista(j, imgs=imgs)
v.ventana.mainloop()

#v=tk.Tk()
#ventor(v)
#grf.etiquetados(v, None, (5,5))
#v.mainloop()