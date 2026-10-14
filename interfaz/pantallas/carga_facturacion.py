from tkinter import *
import tkinter as tk


class PantallaCarga(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        label = tk.Label(self, text='Carga facturación')
        label.grid(row=0, column=0)

