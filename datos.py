from backend import *
from tkinter import ttk

class Tabla:
    def __init__(self, raiz):
        self.frame = raiz
        self.tabla = None

    def table(self,dato, columnas):
            self.tabla = ttk.Treeview(
                self.frame,
                columns=columnas,
                show="headings"
            )

            # Crear los encabezados
            for columna in columnas:
                self.tabla.heading(columna, text=columna, anchor="center")
                self.tabla.column(columna, anchor="center", stretch=True)

            # Insertar las filas
            for fila in dato:
                self.tabla.insert("", "end", values=fila)

            self.tabla.grid(row=1, column=0, sticky='nswe')
            

            self.tabla.tkraise()

            return self.tabla

    def tabla_busqueda_de_(self, dato, columnas):
        self.tabla= ttk.Treeview(
                self.frame,
                columns=columnas,
                show="headings"
            )
            # Crear los encabezados
        for columna in columnas:
            self.tabla.heading(columna, text=columna, anchor="center")
            self.tabla.column(columna, anchor="center", stretch=True)
        # Insertar las filas
        self.tabla.insert("", "end", values=dato)     
        self.tabla.grid(row=1, column=0, sticky='nswe')
        self.tabla.tkraise()
        return self.tabla