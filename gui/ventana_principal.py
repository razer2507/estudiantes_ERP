import tkinter as tk
from tkinter import ttk, messagebox
from logica.helpers import logica
class VentanaPrincipal:
    def __init__(self, log):
        self.lo = log
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Registros Completos")
        self.ventana_principal.geometry("700x400")

        self.menu_principal()
        self.bucle_principal()
    def menu_principal(self):
        tk.Label(self.ventana_principal,text="GESTION DE INSCRITOS 1.0",font=('Arial',16,'bold')).pack(pady=20)


    def bucle_principal(self):
        self.ventana_principal.mainloop()
