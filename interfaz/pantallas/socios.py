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
        
        self.encabezado_socios.config(background= fondo['gral'])
        self.encabezado_socios.grid(row=0, column=0, sticky='ew')

        self.contenido_socios.config(background=fondo['gral'])
        self.contenido_socios.grid(row=1, column=0, sticky='news')

class EncabezadoSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.titulo = tk.Label(self, text='Socios', font=('Arial', 20, 'bold'),background=fondo['gral'], foreground=text['principal'])
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

        self.tabla_socios = TablaSocios(self)
        self.tabla_socios.grid(row=1, column=0, sticky='nswe')

class BarraDeAcciones(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.config(padx=20, pady=20)

        self.socio = tk.StringVar()
        self.busqueda = tk.Label(self, text='Buscar socio:', font=('Arial', 15, 'bold'))
        self.busqueda.config(background=fondo['gral'], foreground=text['principal'])
        self.busqueda.grid(row=0, column=0)
        self.entry_busqueda = tk.Entry(self, textvariable=self.socio, width=25)
        self.entry_busqueda.grid(row=0, column =1, padx = 10, pady=5, sticky='w')
        self.button_buscar = tk.Button(self, text='Buscar', background="#1176C9", foreground=text['principal'], width=15)
        self.button_buscar.config(command=self.buscar)
        self.button_buscar.grid(row=0, column=2, padx= 10, pady=5, sticky='w')
        self.button_ver_todos = tk.Button(self, text='Ver todos', background=color['passed'], foreground=text['principal'],width=15)
        self.button_ver_todos.grid(row=0, column=3, padx=10, pady=5, sticky='w')


    def buscar(self):
        print(self.socio.get())



class TablaSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz,background=color['principal'])
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)

        self.encabezado = EncabezadoTabla(self)
        self.encabezado.config(background=fondo['filas'])
        self.encabezado.grid(row=0, column=0, columnspan=4, sticky='ew')
        self.fila_socio = filaSocio(self)
        self.fila_socio.grid(row=1, column=0, sticky='ew')


class EncabezadoTabla(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.columnconfigure(2,weight=3)
        self.columnconfigure(3,weight=2)
        self.config(padx=5, pady=5)

        self.dni = tk.Label(self, text='DNI')
        self.dni.config(foreground=fondo['btn-principal'], font=('Arial', 10, 'bold'),background=fondo['filas'], anchor='c')
        self.dni.grid(row=0, column=0)

        self.nro_socio = tk.Label(self, text='Nro_socio')
        self.nro_socio.config(foreground=fondo['btn-principal'], font=('Arial', 10, 'bold'),background=fondo['filas'], anchor='c')
        self.nro_socio.grid(row=0, column=1)

        self.nom_ape = tk.Label(self, text='Nombre y Apellido')
        self.nom_ape.config(foreground=fondo['btn-principal'], font=('Arial', 10, 'bold'),background=fondo['filas'], anchor='c')
        self.nom_ape.grid(row=0, column=2)

        self.ooss = tk.Label(self, text='OOSS')
        self.ooss.config(foreground=fondo['btn-principal'], font=('Arial', 10, 'bold'),background=fondo['filas'], anchor='c')
        self.ooss.grid(row=0, column=3)


class filaSocio(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0,weight=1)
        
        self.contenedor_datos = tk.Frame(self)
        self.contenedor_datos.rowconfigure(0, weight=1)
        self.contenedor_datos.columnconfigure(0,weight=1)
        self.contenedor_datos.columnconfigure(1,weight=1)
        self.contenedor_datos.columnconfigure(2,weight=3)
        self.contenedor_datos.columnconfigure(3,weight=2)
        self.config(background='grey')
        self.config(padx=1, pady=1)
        self.contenedor_datos.grid(row=0, column=0)

        self.dni = tk.Label(self.contenedor_datos, text='1234567')
        self.dni.config(foreground=text['btn'], font=('Arial', 10, 'bold'),background=color['principal'], anchor='c')
        self.dni.grid(row=0, column=0, sticky='ew')

        self.nro_socio = tk.Label(self.contenedor_datos, text='1234567/9')
        self.nro_socio.config(foreground=fondo['btn-principal'], font=('Arial', 10),background=color['principal'], anchor='c')
        self.nro_socio.grid(row=0, column=1, sticky='ew')

        self.nom_ape = tk.Label(self.contenedor_datos, text='Juan Perez')
        self.nom_ape.config(foreground=fondo['btn-principal'], font=('Arial', 10),background=color['principal'], anchor='c')
        self.nom_ape.grid(row=0, column=2, sticky='ew')

        self.ooss = tk.Label(self.contenedor_datos, text='OSPSA')
        self.ooss.config(foreground=fondo['btn-principal'], font=('Arial', 10),background=color['principal'], anchor='c')
        self.ooss.grid(row=0, column=3, sticky='ew')
