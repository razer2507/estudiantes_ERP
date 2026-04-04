from basedatos import db

class logica():
    def __init__(self,base_datos:db):
        self.base_datos = base_datos

   
 

    def validar_nombre(self,nom:str):
            if len(nom)>35:
                return False
            if not nom.replace(" ","").isalpha():
                return False
            return True
    
    def validar_cedula(self,cedula:str):
             if len(cedula) <3 or len(cedula) >9:
                 return False
             return True
     
    def validar_correo(self,correo:str):
            if not correo.endswith('@gmail.com'):
                return False
            return True
    
    def validar_curso(self,curso):
        # Validación simple: que no esté vacío y no sea demasiado largo
            return len(curso) > 2 and len(curso) < 50
     
    def validar_telefono(self,telefono):
            if len(telefono)>15:
                return False
            if not telefono.isdigit():
                return False
            return True
    
    def verificar_alumno_duplicado(self,cedula):
            datos = self.base_datos.obtener_datos_tabla('estudiantes',cedula)
            if datos:
                return False
            return True
         
    def registrar_alumno(self,cedula,nom,correo,curso,telefono,estatus='pendiente'):
    
        verificacion = {
        'duplicado': self.verificar_alumno_duplicado(cedula),
        'cedula': self.validar_cedula(cedula),
        'nombre': self.validar_nombre(nom),
        'correo': self.validar_correo(correo),
        'curso': self.validar_curso(curso),
        'telefono': self.validar_telefono(telefono)
    }
        
        if all(verificacion.values()):
            datos = (cedula, nom, correo, telefono, curso, estatus)
            self.base_datos.insertar_datos_tabla('estudiantes',datos)
            return {dato:valor for dato,valor in verificacion.items()}
        else:
            return {dato:valor for dato,valor in verificacion.items() if valor == False}
            
        

    def obtener_datos_alumno(self,cedula):
        datos = self.base_datos.obtener_datos_tabla('estudiantes',cedula)
        if datos:
            return datos
        else:
            return False
        

    def modificar_datos_alumno(self,cedula,dato_ob,dato_nuevo):

        def modificar_nombre(nombre):
            if self.validar_nombre(nombre):
                 self.base_datos.modificar_datos_tabla('estudiantes','nom',nombre,cedula)
                 return True
            else:
                 return False
            
        def modificar_correo(correo):
             if self.validar_correo(correo):
                  self.base_datos.modificar_datos_tabla('estudiantes','correo',correo,cedula)
                  return True
             else:
                  return False

        def modificar_telefono(telefono):
             if self.validar_telefono(telefono):
                  self.base_datos.modificar_datos_tabla('estudiantes','telefono',telefono,cedula)
        def modificar_curso(curso):
             if self.validar_curso(curso):
                  self.base_datos.modificar_datos_tabla('estudiantes','curso_inscrito',curso,cedula)
                  return True
             else:
                  return False
             
        def modificar_estatus():
             datos = self.base_datos.obtener_datos_tabla('estudiantes',cedula)
             if datos:
                estatus = datos['estatus_pago']
                if estatus == 'pendiente':
                  self.base_datos.modificar_datos_tabla('estudiantes','estatus_pago','pagado',cedula)
                  return True
                else:
                  self.base_datos.modificar_datos_tabla('estudiantes','estatus_pago','pendiente',cedula)
                  return True
             else:
                return False
                
        datos = self.base_datos.obtener_datos_tabla('estudiantes',cedula)
        if datos:
             match dato_ob:
                  case 'nom':
                       modificar_nombre(dato_nuevo)
                      
                  case 'correo':
                       modificar_correo(dato_nuevo)
                     
                  case 'telefono':
                       modificar_correo(dato_nuevo)
                       
                  case 'curso_inscrito':
                       modificar_curso(dato_nuevo)
                       
                  case 'telefono':
                       modificar_telefono(dato_nuevo)
                    
                  case 'estatus_pago':
                       modificar_estatus()
                       
    def eliminar_alumno(self,cedula):
        datos = self.base_datos.obtener_datos_tabla('estudiantes',cedula)
        if datos:
             self.base_datos.eliminar_datos_tabla('estudiantes',cedula)
             return True
        else:
             return False
             
             
             
             
           
        


        
         





    