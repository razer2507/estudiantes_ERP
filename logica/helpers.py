from basedatos import db

class logica():
    def __init__(self,base_datos:db):
        self.base_datos = base_datos


 

    def registrar_alumno(self,nom,correo,carrera_id,telefono):

        def validar_alumno_existente(correo):
            existencia = self.base_datos.buscar_estudiante_correo(correo)
            if existencia:
                return False
            return True
        
        def validar_nombre(nom:str):
            if len(nom)>35:
                return False
            if not nom.replace(" ","").isalpha():
                return False
            return True
        
        def validar_correo(correo:str):
            if not correo.endswith('@gmail.com'):
                return False
            return True
        
        def validar_carrera(carrera_id):
            info = self.base_datos.obtener_datos_tabla('carreras',carrera_id)
            if not info:
                return False
            return True

        def validar_telefono(telefono):
            if len(telefono)>15:
                return False
            if not telefono.isdigit():
                return False
            return True
        


        '''Evalua todas las funciones y devuelve un valor booleano cada una'''
        bool_validar_alumno_existente = validar_alumno_existente(correo)
        bool_nom = validar_nombre(nom)
        bool_correo = validar_correo(correo)
        bool_carrera = validar_carrera(carrera_id)
        bool_telefono = validar_telefono(telefono)
        
        

        '''
        validacion completa={
                            Nombre : True
                            Correo: False
                            Carrera: True
                            Telefono : False
                            }
        '''                  
        validacion_completa = {'nombre':bool_nom,
                               'correo':bool_correo,
                               'carrera':bool_carrera,
                               'telefono':bool_telefono,
                               'correo_duplicado':bool_validar_alumno_existente
                               }
        if all(validacion_completa.values()):
            '''Empaqueta todos los datos en una tupla'''
            datos = (nom,correo,carrera_id,telefono)
            self.base_datos.insertar_datos_tabla('estudiantes',datos)
            print("EXITO")
            return {dato:valor for dato,valor in validacion_completa.items()}
        else:
            print("ERROR")
            return {dato:valor for dato,valor in validacion_completa.items()}
        