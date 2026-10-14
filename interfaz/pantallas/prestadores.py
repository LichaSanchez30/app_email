from tkinter import *
from tkinter import messagebox
import tkinter as tk
from backend import *
from interfaz.style import *
from datos import *

class PantallaPrestadores(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.db = DataBase('facturacion.db')
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.encabezado = EncabezadoPrestadores(self)
        self.encabezado.config(background=fondo['gral'])
        self.encabezado.grid(row=0, column=0, sticky='ew')

        self.contenidoPrestadores = ContenidoPrestadores(self, self.db)
        self.contenidoPrestadores.grid(row=1, column=0,sticky='nsew')



class EncabezadoPrestadores(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.columnconfigure(0, weight=0)
        self.titulo = tk.Label(self, text='Prestadores', font=('Arial', 20, 'bold'),background=fondo['gral'], foreground=text['principal'])
        self.titulo.grid(row=0, column=0, sticky='w', padx=10, pady=2)



class ContenidoPrestadores(tk.Frame):
    def __init__(self,raiz, db):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0,weight=1)

        self.barra_busqueda = BusquedaPrestadores(self, db)
        self.barra_busqueda.grid(row=0, column=0,sticky='nsew')



class BusquedaPrestadores(tk.Frame):
    def __init__(self, raiz,db):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.config(padx=20, pady=20, background=fondo['gral'])
        self.db = db

        self.titulo = tk.Label(self, text='Buscar Prestador:',font=('Arial', 15,'bold'),background=fondo['gral'], foreground=text['principal'])
        self.titulo.grid(row=0, column=0,sticky='ew')

        self.aclaracion = tk.Label(self, text='(cuit sin guiones)',font=('Arial', 10),background=fondo['gral'], foreground=text['principal'])
        self.aclaracion.config(anchor='w')
        self.aclaracion.grid(row=0, column=2,sticky='ew', padx=5)

        self.entry_busqueda = tk.Entry(self)
        self.entry_busqueda.grid(row=0, column=1,sticky='ew')

        self.btn_buscar_prestador = tk.Button(self, text='Buscar', background=text['btn2'], foreground=color['principal'])
        self.btn_buscar_prestador.config(command= lambda: self.buscar(raiz),width=15)
        self.btn_buscar_prestador.grid(row=1, column=0, padx=5, pady=5)

        self.btn_ver_todos = tk.Button(self, text='Ver todos', background=text['btn2'], foreground=color['principal'])
        self.btn_ver_todos.config(command=lambda: self.ver_todos(raiz),width=15)
        self.btn_ver_todos.grid(row=1, column=1, padx=5, pady=5)        
        
        self.btn_agregar_borrar = tk.Button(self, text='Agregar/Borrar', background=color['passed'], foreground=color['principal'])
        self.btn_agregar_borrar.config(command=lambda: self.agregar_prestador(raiz),width=15)
        self.btn_agregar_borrar.grid(row=1, column=2, padx=5, pady=5)


    def ver_todos(self, raiz):
        prestadores, columnas = self.db.todos_los('prestadores')
        tabla = Tabla(raiz)
        tabla.table(prestadores,columnas)

    def buscar(self, raiz):
        cuit = str(self.entry_busqueda.get())
        if cuit == '':
            messagebox.showerror('ERROR','DEBE INGRESAR CUIT DE PRESTADOR')
        else:
            prestador, columna = self.db.buscar_por_('prestadores','cuit', cuit )
            if prestador:
                tabla = Tabla(raiz)
                tabla.tabla_busqueda_de_(prestador, columna)

            else:
                messagebox.showwarning('ALERTA','SIN RESULTADOS')


    def agregar_prestador(self, raiz):
        agregar = AgregarPrestador(raiz,self.db)
        agregar.grid(row=1, column=0, sticky='nswe')
        agregar.tkraise()




class AgregarPrestador(tk.Frame):
    def __init__(self, raiz, db):
        super().__init__(raiz)
        self.rowconfigure(0,weight=0)
        self.rowconfigure(1,weight=0)
        self.rowconfigure(2,weight=0)
        self.rowconfigure(3,weight=0)
        self.rowconfigure(4,weight=0)
        self.rowconfigure(5,weight=0)


        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.db = db
        self.titulo = tk.Label(self, text='Dato de Prestador:')
        self.titulo.config(font=('Arial', 15, 'bold'), foreground=text['btn'], anchor='w')
        self.titulo.grid(row=0, column=1, columnspan=2, sticky='ew', pady=10)

        self.cuit = tk.Label(self, text='Cuit Prestador:')
        self.cuit.config(font=('Arial',11, 'bold'), anchor='e')
        self.cuit.grid(row=1, column=1,sticky='ew', padx=5, pady=10)
        self.entry_cuit = tk.Entry(self)
        self.entry_cuit.grid(row=1, column=2, sticky='w')

        self.nom_ape = tk.Label(self, text='Nombre y Apellido:')
        self.nom_ape.config(font=('Arial',11, 'bold'), anchor='e', padx=5, pady=10)
        self.nom_ape.grid(row=2, column=1,sticky='ew')
        self.entry_nom_ape = tk.Entry(self)
        self.entry_nom_ape.grid(row=2, column=2, sticky='w')

        self.email = tk.Label(self, text='Email:')
        self.email.config(font=('Arial',11, 'bold'), anchor='e', padx=5, pady=10)
        self.email.grid(row=3, column=1,sticky='ew')
        self.entry_email = tk.Entry(self)
        self.entry_email.grid(row=3, column=2, sticky='w')

        self.especialidad = tk.Label(self, text='Especialidad:')
        self.especialidad.config(font=('Arial',11, 'bold'), anchor='e', padx=5, pady=10)
        self.especialidad.grid(row=4, column=1,sticky='ew')
        self.entry_especialidad = tk.Entry(self)
        self.entry_especialidad.grid(row=4, column=2, sticky='w')

        self.btn_cargar = tk.Button(self, text='Cargar')
        self.btn_cargar.config(background=color['passed'], foreground=color['principal']) 
        self.btn_cargar.config(width=10, command=self.datos)
        self.btn_cargar.grid(row=5, column=1, sticky='e')

        self.btn_borrar = tk.Button(self, text='Borrar')
        self.btn_borrar.config(background=color['error'], foreground=color['principal']) 
        self.btn_borrar.config(width=10, command=self.borrar)
        self.btn_borrar.grid(row=5, column=2, sticky='e')

    def datos(self):
        cuit = self.entry_cuit.get()
        nom_ape = self.entry_nom_ape.get().upper()
        email = self.entry_email.get()
        especialidad = self.entry_especialidad.get().upper()
        datos = {'cuit':cuit,'nomYApe':nom_ape,'email':email,'especialidad':especialidad}
        self.db.cargar_datos('prestadores', datos)
        self.entry_cuit.delete(0,tk.END)
        self.entry_nom_ape.delete(0,tk.END)
        self.entry_email.delete(0,tk.END)
        self.entry_especialidad.delete(0,tk.END)


    def borrar(self):
        cuit = self.entry_cuit.get()
        prestador, columnas = self.db.buscar_por_('prestadores','cuit',cuit)
        self.entry_nom_ape.insert(0, prestador[1])
        self.entry_email.insert(0, prestador[2])
        self.entry_especialidad.insert(0, prestador[3])
        confirmacion = messagebox.askyesno('Confirmar', '¿Borrar definitivamente?')

        if confirmacion:
            self.db.borrar_dato('prestadores','cuit', cuit)
            messagebox.showinfo('Delete',f'Prestador {self.entry_nom_ape.get()} borrado correctamente ')
        else:
            messagebox.showwarning('Delete','No se borro prestador')

        self.entry_cuit.delete(0,tk.END)
        self.entry_nom_ape.delete(0,tk.END)
        self.entry_email.delete(0,tk.END)
        self.entry_especialidad.delete(0,tk.END)