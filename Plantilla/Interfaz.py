import tkinter as tk
import grafiqueria as grf
import matematiqueria as mat
from PIL import Image
from Juego import juego
#array letras
letras=list(['a','b','c','d','e','f','g','h','i','j','k'])

class vista:
    seleccion=None  
    movimientos_graficados = []    
    #pantalla=tk.Frame()

    def __init__(self, jue:juego, imgs, nombre='Mi ventana'):
        self.ventana = tk.Toplevel()
        self.j = jue
        self.imagos= [{clave: Image.open(ruta) for clave, ruta in dic.items()} for dic in imgs]
        grf.ventor(self.ventana, txt=nombre)
        self.n=self.j.coors.__len__
        self.Inicio()
        self.llenar()
    
    def Inicio(self, event=None, t=0):
        self.turno=t
        self.labels=grf.etiquetados(self.ventana, self.Seleccionar, self.j.dim )
        grf.graficar(self.j, self.labels, self.imagos)
        
    def llenar(self):
        self.nuncio=tk.Label(self.ventana, width=8, height=2, borderwidth=1, relief="solid")
        re = tk.Label(self.ventana, text=" RETVRN ", borderwidth=1, relief="solid")
        re.place(x=self.j.dim[1]*37.5, y=60)
        re.bind("<Button-1>", self.Inicio )
        self.nuncio.place(x=self.j.dim[1]*37.5, y=6)
    
    def validar(self, dup):
        d=self.j.dim
        return dup[0]>=0 and dup[0]<d[0] and dup[1]>=0 and dup[1]<d[1]    
    
    def obtenerContNum(self, dup:tuple):
        if(self.validar(dup)):
            return mat.obtener_Contenido(mat.ubicar(self.labels, dup))
        return [None]
    
    def Comparar(self, dup, b):
        d=self.obtenerContNum(dup)
        if(d):
            d=d[0]
            if(d):
                return d==b
        return d
    
    def funcFicha(self, dup):
        c=self.obtenerContNum(dup)
        return self.j.fichero[c[1]].Movimiento
        
    #Devuelve verdadero si y solo si las dos duplas son coordenadas de casillas con fichas de distinto color o si hay una ficha y una direccion invalida
    def Discriminante(self, dup1, dup2):
        a=self.obtenerContNum(dup1)
        if(not self.validar(dup2)):
            return True
        b=self.obtenerContNum(dup2)
        if b and a:
            return not a[0]==b[0]
        else: return False
    

#Esta funcion devuelve la tupla con las 2 coordenadas de la casilla seleccionada
    def ObtenerUbicación(self, label:tk.Label):
    # Get the grid info of the widget
        grid_info = label.grid_info()
    # Extract the row and column from the grid info
        row = grid_info.get('row', None)  # Default to None if not found
        column = grid_info.get('column', None)  # Default to None if not found
    # Return the position as a tuple
        return (row, column)
    
    def Terminar(self, st):
        for i in self.labels:
            for j in i:
                j.unbind("<Button-1>")
        grf.fin(st)
    
    def GenerarJuego(self):
        d=mat.Extraer(self.labels, self.imagos)
        return juego(self.j.fichero, d, *self.j.dim)

    def Selegir(self, u:tuple):
        self.seleccion=u
        f=self.obtenerContNum(u)[1]
        self.movimientos_graficados = self.j.fichero[f].Movimiento(u, self.obtenerContNum)
        movimientos = self.movimientos_graficados
        grf.graficarMovimientosPosibles(self.labels, movimientos)

    def Mover(self, sel, destino):
            l=self.obtenerContNum(sel)
            ub=self.ObtenerUbicación(destino)
            print("Destino: ", end=" ")
            print(ub)
            grf.restaurarMovimientos(self.labels, self.movimientos_graficados)
            #comprobar si el movimiento es posible
            if(ub in self.movimientos_graficados):      
                self.turno+=1
                self.turno%=self.n
                #Parte Mejorable//Vaciar label
                self.labels[sel[0]][sel[1]]=grf.etiquetado(sel[0], sel[1], self.ventana, self.Seleccionar)
                grf.asignarImagen(ub, self.labels, l )
                self.Pruebas(ub)
                self.blanquear(l, ub)
                print("----------------------------------------------------------------")
            self.seleccion=None


    def funcionar(self ):
        def func(event:tk.Event):
            l=mat.obtener_Contenido(event.widget)
            sel=self.seleccion
            #Si ya hay una seleccion
            if sel:
                self.Mover(sel, event.widget)
            #Si aun no hay seleccion
            elif(l[0]==self.turno):
                self.Selegir(self.ObtenerUbicación(event.widget))

    def Seleccionar(self, event:tk.Event):
        #sel es None cuando se hace el primer clic y es una tupla cuando se hace el segundo
        sel=self.seleccion
        l=mat.obtener_Contenido(event.widget)
        boola=(sel==None)
        boolb=(l==[])
        if (boola and not boolb):
            if (self.turno==l[0]):
                self.seleccion=self.ObtenerUbicación(event.widget) 
                print("Contenido:", end=" ")
                print(l)
                print("Inicio: ", end=" ")
                print(self.seleccion)
                f=self.funcFicha(self.seleccion )
                self.movimientos_graficados = f(self.seleccion, self.obtenerContNum)
                movimientos = self.movimientos_graficados
                grf.graficarMovimientosPosibles(self.labels, movimientos)

        if(not boola and boolb):
        #inicio y destino guardados en variables
            l=self.obtenerContNum(sel)
            destino=event.widget
            ub=self.ObtenerUbicación(destino)
            grf.restaurarMovimientos(self.labels, self.movimientos_graficados)
        #comprobar si el movimiento es posible
            if(ub in self.movimientos_graficados):      
            #Parte Mejorable//Vaciar label
                print("Destino: ", end=" ")
                print(ub)
                self.turno+=1
                self.turno%=2
                self.labels[sel[0]][sel[1]]=grf.etiquetado(sel[0], sel[1], self.ventana, self.Seleccionar)
                grf.asignarImagen( mat.ubicar(self.labels, ub), mat.ubicar(self.imagos, l), l )
                self.Pruebas(ub)
                self.blanquear(l, ub)
                print("----------------------------------------------------------------")
            self.seleccion=None

##################################################################################################################################
    #Funciones Vikingas
    def blanquear(self, lis, destino):
        #Codigo por si gana el blanco
        comp=[self.j.dim[0]-1, 0]
        if(lis==[1, 0] and destino[0] in comp and destino[1] in comp):
            self.Terminar('BLANCAS')

    def Prueba(self,pos, eje, p=False, n=False):
        if mat.Comprobar(pos, eje, self.Discriminante, p, n):
            l=self.obtenerContNum(pos)
            if l==[1, 0]:
                self.Terminar('NEGRAS')
            self.labels[pos[0]][pos[1]]=grf.etiquetado(pos[0], pos[1], self.ventana, self.Seleccionar)
            return True
            
    def Pruebas(self, pos):
        if self.Prueba(pos, 0) or self.Prueba(pos, 1):
            return
        l=mat.direccionales
        for i in l: 
            for j in i:
                c=mat.SumaDupla(j, pos)
                if(self.validar(c)):
                    self.Prueba(c, abs(j[1]))


# Ejecutar el bucle principal de la aplicación
#jue=juego(15, None)
#jue.dibujar()
#v=vista(jue)
#v.ventana.mainloop()