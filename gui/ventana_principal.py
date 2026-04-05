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
                sub_ventana.destroy()
            else:
                campos_invalidos = "\n".join(val.keys())
                messagebox.showerror('Error',f'Error en los siguientes datos:\n{campos_invalidos.upper()}')
                


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
        tk.Button(contenedor,text="SALIR",width=25,command=sub_ventana.destroy).pack(pady=10,padx=1)


        
    def visualizar_registros(self):
        sub_ventana = tk.Toplevel(self.ventana_principal)
        frame_tabla = tk.Frame(sub_ventana)
        frame_tabla.pack(expand=True,fill='both',padx=20,pady=20)
        scroll_bar = ttk.Scrollbar(frame_tabla,orient='vertical')
        

        def eliminar():
            item_selec = vista_tabla.selection()
            if item_selec:
                datos = vista_tabla.item(item_selec[0])['values']
                cedula_borrar = datos[0]
                self.log.eliminar_alumno(cedula_borrar)
                messagebox.showinfo("EXITO",f'Alumno {datos[1]} eliminado.')
                vista_tabla.delete(item_selec[0])
            else:
                messagebox.showerror('ERROR','No se ha seleccionado ningun alumno')

        def modificar():
            
            item_selec = vista_tabla.selection()
            if item_selec:

                datos = vista_tabla.item(item_selec[0])['values']
                ventana_registro = tk.Toplevel(sub_ventana)
                contenedor = tk.LabelFrame(ventana_registro,text="FORMULARIO DE REGISTRO",padx=10,pady=10)
                contenedor.pack(padx=20,pady=20)

                tk.Label(contenedor,text="NOMBRE DEL ESTUDIANTES").pack(pady=10,padx=5)
                nom = tk.Entry(contenedor)
                nom.insert(0,datos[1])
                nom.pack(pady=10,padx=2)

                tk.Label(contenedor,text="CORREO DEL ESTUDIANTE").pack(pady=10,padx=5)
                correo = tk.Entry(contenedor)
                correo.insert(0,datos[2])
                correo.pack(pady=10,padx=2)
    
                tk.Label(contenedor,text="TELEFONO DEL ESTUDIANTE").pack(pady=10,padx=5)
                telefono = tk.Entry(contenedor)
                telefono.insert(0,datos[3])
                telefono.pack(pady=10,padx=2)

    
                tk.Label(contenedor,text="CURSO INSCRITO").pack(pady=10,padx=5)
                curso = tk.Entry(contenedor)
                curso.insert(0,datos[4])
                curso.pack(pady=10,padx=2)

                def boton_guardar():
                    val_nombre = self.log.modificar_datos_alumno(cedula=datos[0],dato_ob='nom',dato_nuevo=nom.get())
                    val_correo = self.log.modificar_datos_alumno(cedula=datos[0],dato_ob='correo',dato_nuevo=correo.get())
                    val_telefono = self.log.modificar_datos_alumno(cedula=datos[0],dato_ob='telefono',dato_nuevo=telefono.get())
                    val_curso = self.log.modificar_datos_alumno(cedula=datos[0],dato_ob='curso_inscrito',dato_nuevo=curso.get())
                

                    dict_validacion = {
                                    'nombre':val_nombre,
                                    'correo':val_correo,
                                    'telefono':val_telefono,
                                    'curso':val_curso}

                    if all(dict_validacion.values()):
                        messagebox.showinfo('EXITO','DATOS MODIFICADOS EXITOSAMENTE')
                        sub_ventana.destroy()

                    else:
                        invalidos = {dato:val for dato,val in dict_validacion.items() if val == False}
                        mensaje_error = "\n".join(invalidos)
                        messagebox.showerror("ERROR",f'ERROR EN LOS SIGUIENTES DATOS\n{mensaje_error}')
            
                tk.Button(contenedor,text="MODIFICAR",command=boton_guardar).pack(pady=20)
                tk.Button(contenedor,text="SALIR",command=ventana_registro.destroy).pack(pady=30)

            else:
                messagebox.showerror('ERROR','No se ha seleccionado ningun alumno')

        columnas = self.log.obtener_datos_columnas()
        vista_tabla = ttk.Treeview(frame_tabla,columns=columnas,show="headings",yscrollcommand=scroll_bar.set)
        datos_columnas = self.log.obtener_datos_totales_tabla()
        scroll_bar.config(command=vista_tabla.yview)
        #configurar headers
        for columna in columnas:
            vista_tabla.heading(columna,text=columna.upper())   
            vista_tabla.column(columna,width=120,anchor='center')

        #eliminar datos residuales
        for item in vista_tabla.get_children():
            vista_tabla.delete(item)

        #insertar datos traidos de la base de datos
        for alumno in datos_columnas:
            vista_tabla.insert("","end",values=alumno)
        
        scroll_bar.pack(side='right',fill='y')
        vista_tabla.pack(side='left',expand=True,fill='both')

        tk.Button(sub_ventana,text="ELIMINAR",command=eliminar).pack(padx=0)
        tk.Button(sub_ventana,text="MODIFICAR",command=modificar).pack(padx=10)
        tk.Button(sub_ventana,text="CERRAR",command=sub_ventana.destroy).pack(padx=20)


    

    def gestionar_inscritos(self):
        def modificar_estatus():
            
            item_selec = tabla.selection()
            if item_selec:
                datos = tabla.item(item_selec[0])['values']
                self.log.modificar_datos_alumno(cedula=datos[0],dato_ob='estatus_pago',dato_nuevo='')
                messagebox.showinfo("EXITO",f"Alumno {datos[1]} modificado")
            else:
                messagebox.showerror("ERROR","NO HAY NINGUN ALUMNO SELECCIONADO")
                
                


        sub_ventana = tk.Toplevel()
        contenedor = tk.Frame(sub_ventana)
        contenedor.pack(expand=True,fill='both',padx=20,pady=20)

        columnas_nombre = ['cedula','nombre','carrera','estatus']


        tabla = ttk.Treeview(contenedor,columns=columnas_nombre,show='headings')
        datos = self.log.obtener_datos_totales_tabla()
        

        for col in columnas_nombre:
            tabla.heading(col,text=col.upper())
            tabla.column(col,width=120,anchor='center')

        #eliminar datos residuales
        for item in tabla.get_children():
            tabla.delete(item)

        #insertar datos traidos de la base de datos
        for alumno in datos:
            tabla.insert("","end",values=(alumno[0],alumno[1],alumno[4],alumno[5]))


        scroll_bar = ttk.Scrollbar(contenedor,orient='vertical')
        scroll_bar.config(command=tabla.yview)
        tabla.pack(side='left',expand=True,fill='both')
        scroll_bar.pack(side='right',fill='y')


        tk.Button(sub_ventana,text="CAMBIAR ESTADO",command=lambda: modificar_estatus()).pack(side='bottom',pady=20)
        
        




    def menu_principal(self):
        tk.Label(self.ventana_principal,text="GESTION DE INSCRITOS 1.0",font=('Arial',16,'bold')).pack(pady=20)

        tk.Button(self.ventana_principal,text="REGISTRAR ESTUDIANTE",width=25,command=lambda:self.menu_registro()).pack(pady=10)

        tk.Button(self.ventana_principal,text="VISUALIZAR REGISTRO",width=25,command=lambda: self.visualizar_registros()).pack(pady=10)

        tk.Button(self.ventana_principal,text="GESTION DE REGISTROS",width=25,command=lambda: self.gestionar_inscritos()).pack(pady=10)

        tk.Button(self.ventana_principal,text="CERRAR",width=25,command=self.ventana_principal.destroy).pack(pady=10)

    def bucle_principal(self):
        self.ventana_principal.mainloop()


#TODO: agregar funcion de actualizar tablas
