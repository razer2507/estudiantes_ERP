from basedatos import db
import pytest

def test_probar_insercion_auto():
    tabla = 'estudiantes'
    base = db(':memory:')
    cursor = base.conn.cursor()



    cursor.execute(f'''PRAGMA table_info({tabla})''')
    tabla_info = cursor.fetchall()
    print(tabla_info)
    nombre_columnas = [i[1] for i in tabla_info]
    print(nombre_columnas)

    columnas_formateadas = ",".join(nombre_columnas)
    placeholders = ",".join(['?' for i in range(len(nombre_columnas))])
    print(placeholders)
  


   
    assert len(tabla_info)>0
    