from wtforms import Form
from wtforms import StringField, IntegerField
from wtforms import EmailField

class AlumnForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    edad = IntegerField('Edad')
    cuatrimestre= IntegerField('Cuatrimestre')
    email = EmailField('Correo')

class MaestroForm(Form):
    id = IntegerField('Id')
    nombre = StringField('Nombre')
    apellidos = StringField('Apellidos')
    materia = StringField('Materia')
    horasSem = IntegerField('Horas Semanales')
    email = EmailField('Correo')
