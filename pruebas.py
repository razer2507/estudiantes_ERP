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
    'carreras': [
        ('Sistemas',), 
        ('Derecho',),
        ('Medicina',)
    ],
    'profesores': [
        ('Dr. Arreaza', 'Ingeniero de Software'), 
        ('Dra. Mendoza', 'Abogada Penalista'),
        ('Ing. Rodriguez', 'Analista de Datos')
    ],
    'estudiantes': [
        # id_estudiante (auto), nombre, correo, carrera_id, telefono
        ('Luis Paez', 'luis@gmail.com', 1, '5550101'),
        ('Maria Sosa', 'maria@gmail.com', 2, '5550202'),
        ('Jose Ferrer', 'jose@gmail.com', 1, '5550303'),
        ('Ana Ruiz', 'ana@gmail.com', 3, '5550404')
    ],
    'materias': [
        # id_materia (auto), id_profesor, nombre
        (1, 'Programación I'),
        (1, 'Bases de Datos'),
        (2, 'Derecho Romano'),
        (3, 'Estadística')
    ],
    'notas': [
        # id_nota (auto), id_materia, id_estudiante, valor, fecha
        (1, 1, 19.05, '2026-03-15'),
        (1, 3, 15.50, '2026-03-15'),
        (2, 1, 18.00, '2026-03-20'),
        (3, 2, 12.00, '2026-03-22')
    ]
}
    
    for tabla,lista_registros in DATOS_SEMILLA.items():
        for i in lista_registros:
            base.insertar_datos_tabla(tabla,i)

    datos = ('Paul Ramirez','ana@gmail.com',1,'04127279138')
    nom,correo,id_carrera,telefono = datos
    validacion = logic.registrar_alumno(nom,correo,id_carrera,telefono)
    assert 





