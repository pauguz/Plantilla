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
v=vista(j, turn=0)
v.ventana.mainloop()

#v=tk.Tk()
#ventor(v)
#grf.etiquetados(v, None, (5,5))
#v.mainloop()
