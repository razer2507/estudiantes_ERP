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
                        id INTEGER PRIMARY KEY,
                        nom TEXT,
                        profesion TEXT
                        );
                        '''

        cursor.execute(query5_profesores)


    '''C'''
    def insertar_datos_tabla(self,tabla_nombre:str,datos:tuple):
        cursor = self.conn.cursor()
        cursor.execute(f'''PRAGMA tabla_info({tabla_nombre})''')
        columnas = cursor.fetchall()
        




    
    



        
        

#TODO: completar crud de profesores (para mi yo del futuro)

        