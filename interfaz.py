from backend import *
from tkinter import *
import tkinter as tk
from ttkbootstrap import *
import ttkbootstrap as ttk



dataBase = DataBase('facturacion.db')

class Interfaz:
    def __init__(self):
        self.root = ttk.App()
        self.estado = True
        

    def frame(self,f,w,h):
        miFrame = tk.Frame(f,width=w, height=h, pady=10, padx=10, background='red')
        miFrame.propagate(False)
        return miFrame
    
    def table(self, hcolum, dataRow, frame):
        tabla = Tableview(
                frame,
                coldata=hcolum,
                rowdata= dataRow,
                bootstyle="primary",
            )
        
        for column in tabla.view["columns"]:
            tabla.view.column(column, anchor="center", stretch=True)
            tabla.view.heading(column, anchor="center")
        
        return tabla.pack(fill="both", expand=True, padx=10, pady=10)
    

    def button(self,frame,t):
        miButton = ttk.Button(frame, text=t, bootstyle="primary").pack(padx=16, pady=4)
        return miButton


    def mostrarSocios(self,dato, frame):
        if self.estado:
            self.estado = False
            datos, column = dataBase.todos_los(dato)
            headerColumn = column
            filas =[]
            for dato in datos:
                filas.append(list(dato))
            self.table(headerColumn, filas, frame)


interfazUno = Interfaz()
interfazUno.root.geometry('1280x1000')
interfazUno.root.columnconfigure(0, weight=1)
interfazUno.root.rowconfigure(0, weight=0)
interfazUno.root.rowconfigure(1, weight=1)



##--------------FRAME BUTTON----------------------------------------------------------------
framebutton = interfazUno.frame(interfazUno.root, 1200, 100)
framebutton.columnconfigure(0,weight=1)
framebutton.columnconfigure(1,weight=1)
framebutton.columnconfigure(2,weight=1)
framebutton.rowconfigure(0, weight=1, minsize=100)

framebutton.grid(row=0, column=0)

##--------------FRAME TABLA SOCIOS/PRESTADOREs-----------------------------------------------

frameTabla = interfazUno.frame(interfazUno.root, 1000, 1000)
frameTabla.grid(row=1, column=0,sticky='news')

#--------------- BOTONES Y FUNCIONALIDAD BOTONES---------------------------------------------
verPrestadores = interfazUno.button(framebutton,'Ver prestadores')
verPrestadores.config(command=lambda: interfazUno.mostrarSocios('prestadores',frameTabla))
verPrestadores.grid(row=0, column=2)

verSocios = interfazUno.button(framebutton,'Ver socios')
verSocios.config(command=lambda: interfazUno.mostrarSocios('socios',frameTabla))
verSocios.grid(row=0, column=1)





interfazUno.root.mainloop()




