from interfaz.pantallas.socios import *
from interfaz.pantallas.prestadores import *
from interfaz.pantallas.facturacion import *
from interfaz.pantallas.carga_facturacion import *
from interfaz.style import *
from tkinter import *
import tkinter as tk


class ContenedorPantallas(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.config(background=fondo['filas'])
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #---- PANTALLAS
        self.pantalla_socios = PantallaSocios(self)
        self.pantalla_socios.grid(row=0, column=0, sticky='news')
        self.pantalla_prestadores = PantallaPrestadores(self)
        self.pantalla_prestadores.grid(row=0, column=0, sticky='news')
        self.pantalla_facturacion = PantallaFacturacion(self)
        self.pantalla_facturacion.grid(row=0, column=0, sticky='news')
        self.pantalla_carga = PantallaCarga(self)
        self.pantalla_carga.grid(row=0,column=0, sticky='news')
        self.pantallas = {'socios': self.pantalla_socios,
                          'prestadores': self.pantalla_prestadores,
                          'facturacion':self.pantalla_facturacion,
                          'cargar': self.pantalla_carga}
        
        self.pantalla_socios.tkraise()


    def mostrar_pantalla(self, nombre):
        self.pantallas[nombre].tkraise()






