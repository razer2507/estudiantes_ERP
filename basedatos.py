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
                FOREIGN KEY(id_profesor) REFERENCES profesores(id)
                );
                '''
        cursor.execute(query2_materias)

        query3_estudiantes = '''
                    CREATE TABLE IF NOT EXISTS estudiantes(
                    id INTEGER PRIMARY KEY,
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
                    id_nota INTEGER PRIMARY KEY AUTOINCREMENT,
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
                        id INTEGER PRIMARY KEY,
                        nom TEXT,
                        profesion TEXT
                        );
                        '''

        cursor.execute(query5_profesores)

    def insertar_datos_estudiantes(self,datos:tuple):
        cursor = self.conn.cursor()
        query = '''INSERT INTO estudiantes(id,nom,correo,carrera_id,telefono) VALUES(?,?,?,?,?)'''
        cursor.execute(query,datos)
        self.conn.commit()

    def ver_datos_estudiante(self,id:int):
        cursor = self.conn.cursor()
        query = '''SELECT *FROM estudiantes WHERE id=?'''
        cursor.execute(query,(id,))
        resultado = cursor.fetchone()
        return resultado

    def eliminar_datos_estudiante(self,id):
        cursor = self.conn.cursor()
        query = '''DELETE FROM estudiantes WHERE id=?'''
        cursor.execute(query,(id,))
        self.conn.commit()

    def modificar_datos_estudiante(self,id,dato_cambiar,dato_nuevo):
        cursor = self.conn.cursor()
        query = f'''UPDATE estudiantes SET {dato_cambiar}=? WHERE id=?'''
        cursor.execute(query,(dato_nuevo,id))
        self.conn.commit()
        
    

        