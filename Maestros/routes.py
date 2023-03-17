from flask import Blueprint
from flask import Flask, redirect, render_template, request, url_for
from Maestros.actions import maestrosActions
import forms

maestros = Blueprint('maestros',__name__)

@maestros.route('/ABCMaestros', methods=['GET'])
def ABCMaestros():
    maestros=  maestrosActions.getMaestros()
    return render_template('ABCMaestro.html', maestros=maestros)

@maestros.route('/newMaestro', methods=['GET','POST'])
def newMaestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        maestrosActions.insertMaestro(
            create_form.nombre.data, 
            create_form.apellidos.data, 
            create_form.materia.data,
            create_form.horasSem.data,
            create_form.email.data
        )
        return redirect(url_for('maestros.ABCMaestros'))
    return render_template('insertMaestro.html', form=create_form)

@maestros.route("/deleteMaestro", methods=['GET', 'POST'])
def deleteMaestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maestro = maestrosActions.getMaestro(id)
        create_form.id.data = maestro[0][0]
        create_form.nombre.data = maestro[0][1]
        create_form.apellidos.data = maestro[0][2]
        create_form.materia.data = maestro[0][3]
        create_form.horasSem.data = maestro[0][4]
        create_form.email.data = maestro[0][5]
        
    if request.method == 'POST':
        id = create_form.id.data
        maestrosActions.deleteMaestro(id)
        return redirect(url_for('maestros.ABCMaestros'))
    
    return render_template('eliminarMaestro.html', form=create_form)

@maestros.route("/updateMaestro", methods=['GET', 'POST'])
def updateMaestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        maestro = maestrosActions.getMaestro(id)
        create_form.id.data = maestro[0][0]
        create_form.nombre.data = maestro[0][1]
        create_form.apellidos.data = maestro[0][2]
        create_form.materia.data = maestro[0][3]
        create_form.horasSem.data = maestro[0][4]
        create_form.email.data = maestro[0][5]
        
    if request.method == 'POST':
        id = create_form.id.data
        nombre = create_form.nombre.data
        apellido = create_form.apellidos.data
        materia = create_form.materia.data
        horas = create_form.horasSem.data
        correo = create_form.email.data
        maestrosActions.updateMaestro(id, nombre, apellido, materia, horas, correo)
        return redirect(url_for('maestros.ABCMaestros'))
    
    return render_template('modificarMaestro.html', form=create_form)
