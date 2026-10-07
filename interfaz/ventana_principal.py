from interfaz.contenedores import *
from interfaz.style import *
from tkinter import *
from interfaz.menu import *
import tkinter as tk




class Ventana_principal:
    def __init__(self):
        self.root = Tk()
        self.root.title('McFarland')
        self.root.minsize(width=500, height=500)
        self.root.columnconfigure(0, weight=0, minsize=200)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.config(background=fondo['gral'])

        self.contenedor_pantallas = ContenedorPantallas(self.root)
        self.bordes_ml = tk.Frame(self.root)
        self.menu_lateral = Menu_lateral(self.bordes_ml, self.contenedor_pantallas.mostrar_pantalla)

        #---- MENU LATERAL ---------------------------------------------------------------
        self.bordes_ml.config(background=color['borde'])
        self.bordes_ml.grid(row=0, column=0, sticky='news')
        self.bordes_ml.columnconfigure(0, weight=0, minsize=200)
        self.bordes_ml.rowconfigure(0, weight=1)
        self.menu_lateral.grid(column=0, row=0, sticky='news', padx=1, pady=1)

        #---- CONTENEDOR DE PANTALLAS (PRINCIPAL) -----------------------------------------
        self.contenedor_pantallas.grid(row=0,column=1, sticky='news')
        #---- LABEL -----------------------------------------------------------------------

        
    def ventana(self, tamaño):
        self.root.geometry(tamaño)

    def inicializar_ventana(self):
        self.root.mainloop()






#        self.root.columnconfigure(0, weight=0, minsize=200)
#        self.root.columnconfigure(1, weight=1)
#        self.root.columnconfigure(2, weight=1)
#        self.root.rowconfigure(0, weight=1)