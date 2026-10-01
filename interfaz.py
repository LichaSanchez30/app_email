from backend import *
from tkinter import *
import tkinter as tk
from ttkbootstrap import *
import ttkbootstrap as ttk


dataBase = DataBase('facturacion.db')

class Interfaz:
    def __init__(self):
        self.root = ttk.App()
        self.tablas = {}
        

    def frame(self,f,c='white'):
        miFrame = tk.Frame(f, background=c)
        miFrame.propagate(False)
        return miFrame
    
    def table(self, hcolum, dataRow, frame):

        tabla = ttk.Tableview(
                frame,
                coldata=hcolum,
                rowdata= dataRow,
                bootstyle="primary",
            )
        
        for column in tabla.view["columns"]:
            tabla.view.column(column, anchor="center", stretch=True)
            tabla.view.heading(column, anchor="center")

        tabla.pack(fill="both", expand=True)

        return tabla
    

    def button(self,frame,t):
        miButton = ttk.Button(frame, text=t, bootstyle="primary")
        return miButton


    def mostrarFrame(self, dato, frame):
        frame.tkraise()
        datos, columnas = dataBase.todos_los(dato)
        filas = [list(fila) for fila in datos]

        if dato not in self.tablas:
            self.tablas[dato] = self.table(columnas, filas, frame)
        else:
            tabla = self.tablas[dato]
            tabla.delete_rows()
            tabla.insert_rows("end", filas)
            tabla.load_table_data()


interfazUno = Interfaz()
interfazUno.root.geometry('1280x1000')
interfazUno.root.columnconfigure(0, weight=0)
interfazUno.root.columnconfigure(1, weight=1)
interfazUno.root.columnconfigure(2, weight=1)
interfazUno.root.columnconfigure(3, weight=1)

interfazUno.root.rowconfigure(0, weight=0)
interfazUno.root.rowconfigure(1, weight=1)
interfazUno.root.rowconfigure(2, weight=1)




##--------------FRAME BUTTON----------------------------------------------------------------
frameMenu = interfazUno.frame(interfazUno.root,'red')
frameMenu.columnconfigure(0,weight=1)
frameMenu.rowconfigure(0, weight=0)
frameMenu.rowconfigure(1, weight=0)
frameMenu.config(width=200)
frameMenu.grid_propagate(False)
frameMenu.grid(row=0, column=0, sticky='ns', rowspan=3)

##--------------FRAME TABLA SOCIOS/PRESTADOREs-----------------------------------------------

frameTabla = interfazUno.frame(interfazUno.root)
frameTabla.config(padx=10, pady=10)
frameTabla.grid(row=2, column=1,sticky='news', columnspan=3)
frameTabla.columnconfigure(0, weight=1)
frameTabla.rowconfigure(0, weight=1)

listSocios = interfazUno.frame(frameTabla)
listSocios.grid(row=0, column=0, sticky='news', columnspan=1, rowspan=1)

listPrestadores = interfazUno.frame(frameTabla)
listPrestadores.grid(row=0, column=0, sticky='news', columnspan=1, rowspan=1)


frameDos = interfazUno.frame(interfazUno.root,'green')
frameDos.grid(row=1, column=1,sticky='news', columnspan=3)

#--------------- BOTONES Y FUNCIONALIDAD BOTONES---------------------------------------------

verFacturacion = interfazUno.button(frameMenu,'Ver facturacion')
verFacturacion.grid(row=0, column=0,sticky ='ew',padx=16, pady=4)

verSocios = interfazUno.button(frameMenu,'Ver socios')
verSocios.config(command=lambda: interfazUno.mostrarFrame('socios',listSocios))
verSocios.grid(row=1, column=0, sticky ='ew',padx=16, pady=4)

verPrestadores = interfazUno.button(frameMenu,'Ver prestadores')
verPrestadores.config(command=lambda: interfazUno.mostrarFrame('prestadores',listPrestadores))
verPrestadores.grid(row=2, column=0,sticky ='ew',padx=16, pady=4)






interfazUno.root.mainloop()




