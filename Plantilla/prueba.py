from Interfaz import ventor
#from Ficha import ficha
from Juego import juego
import tkinter as tk
import grafiqueria as grf
#Creando fichas 
#dama=ficha(mt.diagonal, 'circulo.png')

#Creando fic
#j=juego([dama], , 8)
#v=vista(j, turn=0)
v=tk.Tk()
ventor(v)
grf.etiquetados(v, None, (5,5))
v.mainloop()
