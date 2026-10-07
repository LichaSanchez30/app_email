from tkinter import *
import tkinter as tk


class PantallaFacturacion(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        label = tk.Label(self, text='Facturación')
        label.grid(row=0, column=0)