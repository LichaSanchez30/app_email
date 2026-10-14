from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from datos import *
from interfaz.style import *



class PantallaSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.db = DataBase('facturacion.db')
        self.encabezado_socios = EncabezadoSocios(self)
        self.encabezado_socios.config(background= fondo['gral'])
        self.encabezado_socios.grid(row=0, column=0, sticky='ew')
       
        self.contenido_socios = ContenidoSocios(self,self.db)
        self.contenido_socios.config(background=color['principal'])
        self.contenido_socios.grid(row=1, column=0, sticky='news')

class EncabezadoSocios(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.titulo = tk.Label(self, text='Socios', font=('Arial', 20, 'bold'),background=fondo['gral'], foreground=text['principal'])
        self.titulo.grid(row=0, column=0, sticky='w', padx=20, pady=2)



class ContenidoSocios(tk.Frame):
    def __init__(self, raiz, db):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)    
        self.db = db
        self.barra_acciones = BarraDeAcciones(self, self.db)
        self.barra_acciones.config(background=fondo['gral'])
        self.barra_acciones.grid(row=0,column=0, sticky='ew')


        

class BarraDeAcciones(tk.Frame):
    def __init__(self, raiz, db):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)
        self.config(padx=20, pady=20)
        self.db = db
        self.socio = tk.StringVar()
        self.criterio = tk.StringVar(value='dni')
        self.opcion_nro_socio = tk.Radiobutton(
                                self,
                                text='Nro_socio',
                                value='nro_socio',
                                variable=self.criterio,
                                bg=fondo['gral'],
                                fg=text['principal'],
                                activebackground=fondo['gral'],
                                activeforeground=text['btn2'],
                                selectcolor=fondo['gral'],
                                indicatoron=True,
                                bd=0,
                                relief='flat',
                                highlightthickness=0,
                                highlightbackground=fondo['gral'],
                                highlightcolor=fondo['gral'],
                                takefocus=False
                            )
        self.opcion_dni = tk.Radiobutton(
                                        self,
                                        text='DNI',
                                        value='dni',
                                        variable=self.criterio,
                                        bg=fondo['gral'],
                                        fg=text['principal'],
                                        activebackground=fondo['gral'],
                                        activeforeground=text['btn2'],
                                        selectcolor=fondo['gral'],
                                        indicatoron=True,
                                        bd=0,
                                        relief='flat',
                                        highlightthickness=0,
                                        highlightbackground=fondo['gral'],
                                        highlightcolor=fondo['gral'],
                                        takefocus=False
                                    )
                
        self.opcion_dni.grid(row=0, column=2, sticky='w')
        self.opcion_nro_socio.grid(row=0, column=3, sticky='w')
        self.busqueda = tk.Label(self, text='Buscar socio:', font=('Arial', 15, 'bold'))
        self.busqueda.config(background=fondo['gral'], foreground=text['principal'])
        self.busqueda.grid(row=0, column=0)
        
        self.entry_busqueda = tk.Entry(self, textvariable=self.socio, width=18)
        self.entry_busqueda.grid(row=0, column =1, padx = 10, pady=5, sticky='w')
       
        self.button_buscar = tk.Button(self, text='Buscar', background="#1176C9", foreground=text['principal'], width=15)
        self.button_buscar.config(command=lambda:self.buscar(raiz))
        self.button_buscar.grid(row=1, column=0, padx= 10, pady=5, sticky='w')
        
        self.button_ver_todos = tk.Button(self, text='Ver todos', background="#1176C9", foreground=text['principal'],width=15)
        self.button_ver_todos.config(command=lambda:self.ver_todos(raiz))
        self.button_ver_todos.grid(row=1, column=1, padx=10, pady=5, sticky='w')

        self.button_agregar_socio = tk.Button(self, text='+ Agregar/Borrar socio', background=color['passed'],foreground=text['principal'],width=15)
        self.button_agregar_socio.config(command=lambda:self.agregar_socio(raiz, self.db))
        self.button_agregar_socio.grid(row=1, column=2, columnspan=2, pady=5, sticky='w')

    def buscar(self, raiz):
        dato = str(self.socio.get())
        if dato == '':
            messagebox.showerror('ALERTA','INGRESAR CRITERIO DE BUSQUEDA')
        else:
            criterio = self.criterio.get()
            datos, columna = self.db.buscar_por_('Socios',criterio,dato)
            if datos:
                tabla = Tabla(raiz)
                tabla.tabla_busqueda_de_(datos, columna)
            else:
                messagebox.showwarning('ALERTA', 'Socio no encontrado')



    def ver_todos(self, raiz):
        datos, columna = self.db.todos_los('Socios')
        tabla = Tabla(raiz)
        tabla.table(datos, columna)

    def agregar_socio(self, raiz, db):
        agregar = AgregarSocio(raiz, db)
        agregar.grid(row=1, column=0, sticky='nsew')
        agregar.tkraise()


class AgregarSocio(tk.Frame):
    def __init__(self,raiz, db):
        super().__init__(raiz)
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=0)
        self.rowconfigure(2, weight=0)
        self.rowconfigure(3, weight=0)
        self.rowconfigure(4, weight=0)
        self.rowconfigure(5, weight=0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.db = db

        self.titulo = tk.Label(self, text='Cargar nuevo socio:',anchor='center')
        self.titulo.grid(row=0, column=1, columnspan=2, sticky="ew")
        
        self.dni = tk.Label(self, text='DNI:',anchor='e')
        self.dni.grid(row=1, column=1, sticky="ew", padx=10, pady=10)
        self.entry_dni = tk.Entry(self)
        self.entry_dni.grid(row=1, column=2,sticky="ew", padx=10, pady=10)

        self.nro_socio = tk.Label(self, text='Nro_socio:',anchor='e')
        self.nro_socio.grid(row=2, column=1, sticky="ew", padx=10, pady=10)
        self.entry_nro_socio = tk.Entry(self)
        self.entry_nro_socio.grid(row=2, column=2, sticky="ew", padx=10, pady=10)

        self.nom_ape = tk.Label(self, text='Nombre y Apellido:',anchor='e')
        self.nom_ape.grid(row=3, column=1, sticky="ew", padx=10, pady=10)
        self.entry_nom_ape = tk.Entry(self)
        self.entry_nom_ape.grid(row=3, column=2, sticky="ew", padx=10, pady=10)

        self.ooss = tk.Label(self, text='OOSS:',anchor='e')
        self.ooss.grid(row=4, column=1, sticky="ew", padx=10, pady=10)
        self.entry_ooss = tk.Entry(self)
        self.entry_ooss.grid(row=4, column=2, sticky="ew", padx=10, pady=10)


        self.button_cargar = tk.Button(self, text='Cargar socio')
        self.button_cargar.config(command=lambda: self.datos())
        self.button_cargar.grid(row=5, column=1,sticky='ew')

        self.button_borrar = tk.Button(self,text='Borrar socio')
        self.button_borrar.config(command=lambda:self.borrar())
        self.button_borrar.grid(row=5, column=2, sticky='ew',padx=10)

    def datos(self):
        dni = self.entry_dni.get()
        nro_socio = self.entry_nro_socio.get()
        nom_ape = self.entry_nom_ape.get().upper()
        ooss = self.entry_ooss.get().upper()
        datos = {'dni':dni,'nro_socio':nro_socio,'nombYApe':nom_ape,'ooss':ooss}
        self.db.cargar_datos('socios', datos)
        self.entry_dni.delete(0,tk.END)
        self.entry_nro_socio.delete(0,tk.END)
        self.entry_nom_ape.delete(0,tk.END)
        self.entry_ooss.delete(0,tk.END)

    def borrar(self):
        dni = self.entry_dni.get()
        socio, columnas = self.db.buscar_por_('Socios','dni',dni)
        self.entry_nro_socio.insert(0, socio[1])
        self.entry_nom_ape.insert(0, socio[2])
        self.entry_ooss.insert(0, socio[3])
        confirmacion = messagebox.askyesno('Confirmar', '¿Borrar definitivamente?')

        if confirmacion:
            self.db.borrar_dato('socios','dni', dni)
            messagebox.showinfo('Delete',f'Socio {self.entry_nom_ape.get()} borrado correctamente ')
        else:
            messagebox.showwarning('Delete','No se borro socio')

        self.entry_dni.delete(0,tk.END)
        self.entry_nro_socio.delete(0,tk.END)
        self.entry_nom_ape.delete(0,tk.END)
        self.entry_ooss.delete(0,tk.END)



        