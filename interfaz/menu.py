from tkinter import *
import tkinter as tk
from interfaz.componentes import *



class Menu_lateral(tk.Frame):
    def __init__(self, raiz, mostrar_pantalla):
        super().__init__(raiz)
        self.config(background=fondo['sec-tarj'])
        self.columnconfigure(0, weight=0, minsize=200)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.mostrar_pantalla= mostrar_pantalla

        #---- BOTONES DE MENU LATERAL -----------------------------------------------------
        self.btn_socios = BotonMenu(self,'Socios', comando= lambda:self.mostrar_pantalla('socios'))
        self.btn_socios.grid(row=0, column=0, sticky='ew', padx=10, pady=10)
        self.btn_prestadores = BotonMenu(self,'Prestadores',comando= lambda:self.mostrar_pantalla('prestadores'))
        self.btn_prestadores.grid(row=1, column=0, sticky='ew', padx=10, pady=10)
        self.btn_facturacion = BotonMenu(self,'Facturación',comando= lambda:self.mostrar_pantalla('facturacion'))
        self.btn_facturacion.grid(row=2, column=0, sticky='ew', padx=10, pady=10)

    