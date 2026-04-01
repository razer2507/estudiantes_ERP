import sqlite3

class db:
    def __init__(self,directo_archivo_db='datos/academia.db'):
        self.directorio_archivo_db = directo_archivo_db
        self.conn = sqlite3.connect(directo_archivo_db)
        self.iniciar_tablas()


    def iniciar_tablas(self):
        cursor = self.conn.cursor()
        cursor.execute('''PRAGMA foreign_keys = ON;''')


        query1_carreras= '''
                    CREATE TABLE IF NOT EXISTS carreras(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom VARCHAR(30)
                    );
                '''
        cursor.execute(query1_carreras)

        query2_materias= '''
                CREATE TABLE IF NOT EXISTS materias(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_profesor INTEGER,
                nom VARCHAR(30),
                FOREIGN KEY(id_profesor) REFERENCES profesores(id)
                );
                '''
        cursor.execute(query2_materias)

        query3_estudiantes = '''
                    CREATE TABLE IF NOT EXISTS estudiantes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nom VARCHAR(40) NOT NULL,
                    correo VARCHAR(40),
                    carrera_id INTEGER,
                    telefono VARCHAR(13),
                    FOREIGN KEY(carrera_id) REFERENCES carreras(id)
                    );
                '''
        cursor.execute(query3_estudiantes)


        query4_notas = '''
                    CREATE TABLE IF NOT EXISTS notas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_materia INTEGER,
                    id_estudiante INTEGER,
                    valor NUMERIC(10,2) NOT NULL,
                    fecha TEXT,
                    FOREIGN KEY(id_materia) REFERENCES materia(id),
                    FOREIGN KEY(id_estudiante) REFERENCES estudiantes(id)
                    );
                '''
        cursor.execute(query4_notas)


        query5_profesores = '''
                        CREATE TABLE IF NOT EXISTS profesores(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nom TEXT,
                        profesion TEXT
                        );
                        '''

        cursor.execute(query5_profesores)


    '''C'''
    def insertar_datos_tabla(self,tabla_nombre:str,datos:tuple):
         
         '''​"

         Se consultan los metadatos de la tabla para automatizar la inserción 
         y permitir que el sistema sea escalable a cualquier tabla nueva sin modificar el código.
         '''
         cursor = self.conn.cursor()
         
         cursor.execute(f'''PRAGMA table_info({tabla_nombre})''')
         tabla_info = cursor.fetchall()
         ##extrae todos los nombres de las columnas menos el id(porque se incrementa solo)
         columnas_nombre = [i[1] for i in tabla_info if i[5] == 0]

         columnas_formateadas = ",".join(columnas_nombre)
         placeholders = ','.join(["?" for i in range(len(columnas_nombre))])

         query = f'''INSERT INTO {tabla_nombre}({columnas_formateadas}) VALUES({placeholders})'''
         cursor.execute(query,datos)
         self.conn.commit()

    def obtener_datos_tabla(self,tabla_nombre,id):
        cursor = self.conn.cursor()
        cursor.execute(f'''SELECT *FROM {tabla_nombre} WHERE id=?''',(id,))
        datos = cursor.fetchall()
        return datos
    
    def eliminar_datos_tabla(self,tabla_nombre,id):
        cursor = self.conn.cursor()
        cursor.execute(f'''DELETE FROM {tabla_nombre} WHERE id=?''',(id,))
        self.conn.commit()


    def modificar_datos_tabla(self,tabla_nombre,dato_modificar,dato_nuevo,id):
        cursor = self.conn.cursor()
        query = f'UPDATE {tabla_nombre} SET {dato_modificar}=? WHERE id=?'
        cursor.execute(query,(dato_nuevo,id))
    


#TODO: completar capa de db dinamica y evaluar probabilidad de integrar a branch main

