from basedatos import db
import pytest

def test_probar_insercion_estudiantes():
    '''arrange'''
    base = db(':memory:')
    cursor = base.conn.cursor()

    cursor.execute('''INSERT INTO carreras(nom) VALUES('Informatica') ''')
    base.conn.commit()
    datos = (32143840,'Paul Ramirez Rafael','paul@gmail.com',1,'0412-7279138')

    '''act'''
    base.insertar_datos_estudiantes(datos)

    cursor.execute('''SELECT *FROM estudiantes''')
    resultado = cursor.fetchone()

    '''assert'''
    assert resultado is not None
    assert resultado[0] == 32143840
    assert resultado[1] == 'Paul Ramirez Rafael'
    assert resultado[2] == 'paul@gmail.com'
    assert resultado[3] == 1
    assert resultado[4] == '0412-7279138'
    print('db:prueba de insercion pasada')

def test_probar_visualizar_estudiante():
    base = db(':memory:')
    cursor = base.conn.cursor()



    cursor.execute('''INSERT INTO carreras(nom) VALUES('Informatica') ''')
    base.conn.commit()

    datos = (32143840,'Paul Ramirez Rafael','paul@gmail.com',1,'0412-7279138')
    cursor.execute('''INSERT INTO estudiantes(id,nom,correo,carrera_id,telefono) VALUES(?,?,?,?,?)''',datos)


    resultado = base.ver_datos_estudiante(datos[0])

    assert resultado != None
    print('db:prueba de visualizacion pasada')

def test_probar_eliminar_estudiante():

    '''arrange'''
    base = db(':memory:')
    cursor = base.conn.cursor()
    cursor.execute('''INSERT INTO carreras(nom) VALUES('Informatica')''')
    base.conn.commit()    
    datos = (32143840,'Paul Ramirez Rafael','paul@gmail.com',1,'0412-7279138')
    cursor.execute('''INSERT INTO estudiantes(id,nom,correo,carrera_id,telefono) VALUES(?,?,?,?,?)''',datos)
    

    '''act'''
    base.eliminar_datos_estudiante(datos[0])
    cursor.execute('''SELECT id FROM estudiantes WHERE id=?''',(datos[0],))
    resultados = cursor.fetchone()

    '''assert'''
    assert not resultados
    print('db:prueba de eliminacion pasada')
def test_probar_modificar_estudiante():
    '''arrange'''
    base = db(':memory:')

    cursor = base.conn.cursor()
    cursor.execute('''INSERT INTO carreras(nom) VALUES('Informatica')''')
    base.conn.commit()    

    datos = (32143840,'Paul Ramirez Rafael','paul@gmail.com',1,'0412-7279138')
    cursor.execute('''INSERT INTO estudiantes(id,nom,correo,carrera_id,telefono) VALUES(?,?,?,?,?)''',datos)

    '''act'''
    base.modificar_datos_estudiante(id=32143840,dato_cambiar='nom',dato_nuevo='Saul')
    cursor.execute('''SELECT nom FROM ESTUDIANTES WHERE id=?''',(datos[0],))
    resultado = cursor.fetchone()

    '''assert'''
    assert resultado[0] == 'Saul'
    print('db:prueba de modificacion pasada')

#TODO: Agregar fixtures para eficiencia(para mi yo del futuro)