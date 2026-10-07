from tkinter import *
import tkinter as tk
from interfaz.style import *

class BotonMenu(tk.Button):
    def __init__(self,raiz, texto, comando):
        super().__init__(raiz, text=texto, command=comando)
        self.config(background=fondo['btn-principal'], foreground=text['btn'], activebackground=text['secundario'])