from basedatos import db
import pytest
from logica.helpers import logica

import os

def test_probar_insercion_auto():

    
    nombre_db = "datos/academia.db" # Asegúrate de usar el nombre real de tu archivo

   
    # Verificamos si el archivo existe antes de intentar borrarlo
    if os.path.exists(nombre_db):
        os.remove(nombre_db)
        print(f"Base de datos {nombre_db} eliminada para reiniciar la prueba")

    base = db()
    cursor = base.conn.cursor()
    logic = logica(base)
   


    DATOS_SEMILLA = {
        'estudiantes': [
            # id (cedula), nombre, correo, telefono, curso_inscrito, estatus_pago
            (31143840, 'Luis Paez', 'luis@gmail.com', '5550101', 'Python Pro', 'Pagado'),
            (32143840, 'Maria Sosa', 'maria@gmail.com', '5550202', 'Data Science', 'Pendiente'),
            (33143840, 'Jose Ferrer', 'jose@gmail.com', '5550303', 'Python Pro', 'Pagado')
        ]
    }

    for tabla, filas in DATOS_SEMILLA.items():
        for fila in filas:
            base.insertar_datos_tabla(tabla, fila)
    
    # Verificación rápida
    alumno = base.obtener_datos_tabla('estudiantes', 31143840)
    for key,value in alumno.items(): # pyright: ignore[reportOptionalMemberAccess]
        print(f'{key}:{value}')
    print(alumno)
    assert alumno is not None
