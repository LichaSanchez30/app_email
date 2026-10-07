from tkinter import *
from interfaz.style import *
import tkinter as tk
from ttkbootstrap import *
import ttkbootstrap as ttk

class PantallaSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.encabezado_socios = EncabezadoSocios(self)
        self.contenido_socios = ContenidoSocios(self)
        
        self.encabezado_socios.config(background= color['error'])
        self.encabezado_socios.grid(row=0, column=0, sticky='ew')

        self.contenido_socios.config(background=fondo['gral'])
        self.contenido_socios.grid(row=1, column=0, sticky='news')

class EncabezadoSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.titulo = ttk.Label(self, text='Socios', font=('Arial', 20, 'bold'),bootstyle='primary', icon='file-person', icon_size=20)
        self.titulo.grid(row=0, column=0, sticky='w', padx=20, pady=2)



class ContenidoSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)    
        self.barra_acciones = BarraDeAcciones(self)
        self.barra_acciones.config(background=fondo['gral'])
        self.barra_acciones.grid(row=0,column=0, sticky='ew')

class BarraDeAcciones(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.socio = tk.StringVar()
        self.busqueda = tk.Label(self, text='Buscar socio:', font=('Arial', 15, 'bold'))
        self.busqueda.config(background=fondo['gral'], foreground=text['principal'])
        self.busqueda.grid(row=0, column=0)
        self.entry_busqueda = ttk.Entry(self, textvariable=self.socio)
        self.entry_busqueda.grid(row=0, column =1, padx = 10, pady=5, sticky ='ew')
        self.button_buscar = ttk.Button(self, text='Buscar', bootstyle='primary', icon='search')
        self.button_buscar.config(command=self.buscar)
        self.button_buscar.grid(row=0, column=2, padx= 10, pady=5)


    def buscar(self):
        print(self.socio.get())