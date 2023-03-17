from db import get_connection

class maestrosActions():
    def getMaestros():
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call obtener_maestros()')
                resultset=cursor.fetchall()
            connection.close()
            return resultset
        except Exception as e:
            print("error: ", e)

    def getMaestro(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call consultar_maestro(%s)',(id))
                resultset=cursor.fetchall()
            connection.close()
            return resultset
        except Exception as e:
            print("error: ", e)

    def insertMaestro(nombre, apellido, materia, horas, correo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call insertar_maestro(%s,%s,%s,%s,%s)',(nombre, apellido, materia, horas, correo))
                connection.commit()
            connection.close()
        except Exception as e:
            print("error: ", e)
    
    def deleteMaestro(id):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call eliminar_maestro(%s)',(id))
                connection.commit()
            connection.close()
        except Exception as e:
            print("error: ", e)
    
    def updateMaestro(id, nombre, apellido, materia, horas, correo):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute('call actualizar_maestro(%s,%s,%s,%s,%s,%s)',(id, nombre, apellido, materia, horas, correo))
                connection.commit()
            connection.close()
        except Exception as e:
            print("error: ", e)
