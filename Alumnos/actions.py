from db import get_connection

class alumnosActions():
    def getAlumnos():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call obtener_alumnos()')
                resultset=cursor.fetchall()
            connection.close()
            return resultset
        except Exception as e:
            print("error: ", e)

    def getAlumno(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_alumno(%s)',(id))
                resultset=cursor.fetchall()
            connection.close()
            return resultset
        except Exception as e:
            print("error: ", e)

    def insertAlumno(nombre, apellido, edad, cuatrimestre, correo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call insertar_alumno(%s,%s,%s,%s,%s)',(nombre, apellido, edad, cuatrimestre, correo))
                connection.commit()
            connection.close()
        except Exception as e:
            print("error: ", e)
    
    def deleteAlumno(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call eliminar_alumno(%s)',(id))
                connection.commit()
            connection.close()
        except Exception as e:
            print("error: ", e)
    
    def updateAlumno(id, nombre, apellido, edad, cuatimestre, correo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call actualizar_alumno(%s,%s,%s,%s,%s,%s)',(id, nombre, apellido, edad, cuatimestre, correo))
                connection.commit()
            connection.close()
        except Exception as e:
            print("error: ", e)
