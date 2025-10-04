import tkinter as tk
import grafiqueria as grf 

# Crear la ventana principal
root = tk.Tk()
root.title("Barra de Herramientas con Menú")

# Crear la barra de menú
menu_bar = tk.Menu(root)

# Crear los menús desplegables
archivo_menu = tk.Menu(menu_bar, tearoff=0)
archivo_menu.add_command(label="Nuevo")
archivo_menu.add_command(label="Abrir")
archivo_menu.add_separator()
archivo_menu.add_command(label="Salir", command=root.quit)

edicion_menu = tk.Menu(menu_bar, tearoff=0)
edicion_menu.add_command(label="Cortar")
edicion_menu.add_command(label="Copiar")
edicion_menu.add_command(label="Pegar")

# Agregar menús desplegables a la barra
menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
menu_bar.add_cascade(label="Edición", menu=edicion_menu)

# Configurar la ventana para usar la barra de menú
root.config(menu=menu_bar)

root.mainloop()