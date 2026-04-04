import tkinter as tk
from tkinter import ttk, messagebox
from logica.helpers import logica
class VentanaPrincipal:
    def __init__(self, log:logica):
        self.log = log
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Registros Completos")
        self.ventana_principal.geometry("700x400")

        self.menu_principal()
        self.bucle_principal()

    def menu_registro(self):

        def guardar_registro():
            val = self.log.registrar_alumno(id.get(),nom.get(),correo.get(),telefono.get(),curso.get())
            if all(val.values()):
                messagebox.showinfo('Exito',"Estudiante guardado con exito")
            else:
                campos_invalidos = "\n".join(val.keys())
                messagebox.showerror('Error',f'Error en los siguientes datos:\n{campos_invalidos}')
                


        sub_ventana = tk.Toplevel(self.ventana_principal)
        contenedor = tk.LabelFrame(sub_ventana,text="FORMULARIO DE REGISTRO",padx=10,pady=10)
        contenedor.pack(padx=20,pady=20)

        tk.Label(contenedor,text="ID DEL ESTUDIANTE").pack(pady=10,padx=5)
        id = tk.Entry(contenedor)
        id.pack(pady=10,padx=2)

        tk.Label(contenedor,text="NOMBRE DEL ESTUDIANTES").pack(pady=10,padx=5)
        nom = tk.Entry(contenedor)
        nom.pack(pady=10,padx=2)

        tk.Label(contenedor,text="CORREO DEL ESTUDIANTE").pack(pady=10,padx=5)
        correo = tk.Entry(contenedor)
        correo.pack(pady=10,padx=2)
    
        tk.Label(contenedor,text="TELEFONO DEL ESTUDIANTE").pack(pady=10,padx=5)
        telefono = tk.Entry(contenedor)
        telefono.pack(pady=10,padx=2)

    
        tk.Label(contenedor,text="CURSO INSCRITO").pack(pady=10,padx=5)
        curso = tk.Entry(contenedor)
        curso.pack(pady=10,padx=2)

        tk.Button(contenedor,text="REGISTRAR",width=25,command=lambda:guardar_registro()).pack(pady=10,padx=1)


        

        


    def menu_principal(self):
        tk.Label(self.ventana_principal,text="GESTION DE INSCRITOS 1.0",font=('Arial',16,'bold')).pack(pady=20)

        tk.Button(self.ventana_principal,text="REGISTRAR ESTUDIANTE",width=25,command=lambda:self.menu_registro()).pack(pady=10)

        tk.Button(self.ventana_principal,text="VISUALIZAR REGISTRO",width=25).pack(pady=10)

        tk.Button(self.ventana_principal,text="GESTION DE REGISTROS",width=25).pack(pady=10)

        tk.Button(self.ventana_principal,text="CERRAR",width=25).pack(pady=10)

    def bucle_principal(self):
        self.ventana_principal.mainloop()

