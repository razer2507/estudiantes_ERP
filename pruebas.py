from basedatos import db
import pytest

def test_probar_insercion_auto():
    tabla = 'estudiantes'
    base = db(':memory:')
    cursor = base.conn.cursor()
    
    tabla_nombre = 'carreras'
    datos = ('Sistemas',)
    dato_modificar = 'nom'
    dato_nuevo = "Ingenieria de sistemas"
    id = 1
    base.insertar_datos_tabla(tabla_nombre,datos)
    cursor.execute("SELECT *FROM carreras")
    print('\nresultados:',cursor.fetchall())

    base.modificar_datos_tabla(tabla_nombre,dato_modificar,dato_nuevo,id)

    cursor.execute("SELECT *FROM carreras WHERE id=?",(id,))
    resultados = cursor.fetchone()
    print(f'resultados: {resultados}')
    assert resultados[1] == dato_nuevo
    