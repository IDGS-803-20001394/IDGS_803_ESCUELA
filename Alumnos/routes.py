from flask import Blueprint
from flask import Flask, redirect, render_template, request, url_for
from Alumnos.actions import alumnosActions
import forms

alumnos = Blueprint('alumnos',__name__)

@alumnos.route('/ABCAlumnos', methods=['GET'])
def ABCAlumnos():
    alumnos=  alumnosActions.getAlumnos()
    return render_template('ABCAlumno.html', alumnos=alumnos)

@alumnos.route('/newAlumno', methods=['GET','POST'])
def newAlumno():
    create_form = forms.AlumnForm(request.form)
    if request.method == 'POST':
        alumnosActions.insertAlumno(
            create_form.nombre.data, 
            create_form.apellidos.data, 
            create_form.edad.data,
            create_form.cuatrimestre.data,
            create_form.email.data
        )
        return redirect(url_for('alumnos.ABCAlumnos'))
    return render_template('insertAlumno.html', form=create_form)

@alumnos.route("/deleteAlumno", methods=['GET', 'POST'])
def deleteAlumno():
    create_form = forms.AlumnForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alumn = alumnosActions.getAlumno(id)
        create_form.id.data = alumn[0][0]
        create_form.nombre.data = alumn[0][1]
        create_form.apellidos.data = alumn[0][2]
        create_form.edad.data = alumn[0][3]
        create_form.cuatrimestre.data = alumn[0][4]
        create_form.email.data = alumn[0][5]
        
    if request.method == 'POST':
        id = create_form.id.data
        alumnosActions.deleteAlumno(id)
        return redirect(url_for('alumnos.ABCAlumnos'))
    
    return render_template('eliminarAlumno.html', form=create_form)

@alumnos.route("/updateAlumno", methods=['GET', 'POST'])
def updateAlumno():
    create_form = forms.AlumnForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alumn = alumnosActions.getAlumno(id)
        create_form.id.data = alumn[0][0]
        create_form.nombre.data = alumn[0][1]
        create_form.apellidos.data = alumn[0][2]
        create_form.edad.data = alumn[0][3]
        create_form.cuatrimestre.data = alumn[0][4]
        create_form.email.data = alumn[0][5]
        
    if request.method == 'POST':
        id = create_form.id.data
        nombre = create_form.nombre.data
        apellido = create_form.apellidos.data
        edad = create_form.edad.data
        cuatimestre = create_form.cuatrimestre.data
        correo = create_form.email.data
        alumnosActions.updateAlumno(id, nombre, apellido, edad, cuatimestre, correo)
        return redirect(url_for('alumnos.ABCAlumnos'))
    
    return render_template('modificarAlumno.html', form=create_form)
