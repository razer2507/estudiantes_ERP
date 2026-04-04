import sqlite3
import os
class db:
    def __init__(self,directo_archivo_db='datos/academia.db'):

        self.conn = sqlite3.connect(directo_archivo_db)
        self.iniciar_tablas()


    def iniciar_tablas(self):
        cursor = self.conn.cursor()
    
        query1_estudiantes = '''
                    CREATE TABLE IF NOT EXISTS estudiantes(
                    id INTEGER PRIMARY KEY,
                    nom TEXT NOT NULL,
                    correo TEXT,
                    telefono TEXT,
                    curso_inscrito TEXT,
                    estatus_pago TEXT
                    );
                '''
        cursor.execute(query1_estudiantes)

    def consultar_metadatos_tabla(self,tabla_nombre):
        cursor = self.conn.cursor()
        cursor.execute(f'''PRAGMA table_info({tabla_nombre})''')
        tabla_info = cursor.fetchall()
        return [i[1] for i in tabla_info]
    '''C'''
    def insertar_datos_tabla(self,tabla_nombre:str,datos:tuple):
         '''​"
         Se consultan los metadatos de la tabla para automatizar la inserción 
         y permitir que el sistema sea escalable a cualquier tabla nueva sin modificar el código.
         '''
         cursor = self.conn.cursor()
       
         columnas_nombre = self.consultar_metadatos_tabla(tabla_nombre)     
         columnas_formateadas = ",".join(columnas_nombre)
         placeholders = ','.join(["?" for i in range(len(columnas_nombre))])

         query = f'''INSERT INTO {tabla_nombre}({columnas_formateadas}) VALUES({placeholders})'''
         cursor.execute(query,datos)
         self.conn.commit()
    '''R'''
    def obtener_datos_tabla(self,tabla_nombre,id):
        print(f'{tabla_nombre}\n{id}')
        cursor = self.conn.cursor()
        cursor.execute(f'''SELECT *FROM {tabla_nombre} WHERE id=?''',(id,))
        datos = cursor.fetchone()
        nom_columnas = self.consultar_metadatos_tabla(tabla_nombre)
        if not datos:
            return None
        return dict(zip(nom_columnas,datos))

             
    '''U'''
    def modificar_datos_tabla(self,tabla_nombre,dato_modificar,dato_nuevo,id):
        print(f'{tabla_nombre}\n{dato_modificar}\n{dato_nuevo}\n{id}')
        cursor = self.conn.cursor()
        query = f'UPDATE {tabla_nombre} SET {dato_modificar}=? WHERE id=?'
        cursor.execute(query,(dato_nuevo,id))
        self.conn.commit()
    '''D''' 
    def eliminar_datos_tabla(self,tabla_nombre,id):
        print(f'{tabla_nombre}\n{id}')
        cursor = self.conn.cursor()
        cursor.execute(f'''DELETE FROM {tabla_nombre} WHERE id=?''',(id,))
        self.conn.commit()


