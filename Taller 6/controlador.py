from app import app
from modelos import *
from flask import render_template, request, redirect, url_for
from datetime import datetime


@app.route('/')
def index():
    personas = persona.query.all()
    personass=[]
    for Persona in personas:
        personass += [Persona]
    return render_template('Vista.html',list=personass)


@app.route('/registros', methods=['POST'])
def registros():
    perso = persona(nombres=request.form['nombres'], apellidos=request.form['apellidos'], 
                    idtipodocumento=request.form['tipodocumento'], documento=request.form['documento'],lugarresidencia=request.form['residencia'],
                    email=request.form['email'], telefono=request.form['telefono'], password=request.form['password'])
    db.session.add(perso)
    db.session.commit()
    return redirect(url_for('Vista.html'))

@app.route('/editar/<id>')
def editar(id):
    return render_template('modificar.html')

# @app.route('/actualizar/<id>', methods=['POST'])
# def actualizar(id):
#     actualizar = persona.query.filter_by(id=int(id)).first()
#     perso = persona(nombres=request.form['nombres'], apellidos=request.form['apellidos'], 
#         idtipodocumento=request.form['tipodocumento'], documento=request.form['documento'], lugarresidencia=request.form['residencia'],
#         fechanacimiento=datetime.strptime(request.form['fecha'], '%Y-%m-%d'), email=request.form['email'], telefono=request.form['telefono'], usuario=request.form['usuario'],
#         password=request.form['password'])
#     db.session.update(perso)
#     db.session.commit()
#     return redirect(url_for('Vista.html'))
        

@app.route('/delete/<id>')
def delete(id):
    borrar = persona.query.filter_by(id=int(id)).delete()
    db.session.commit()
    return redirect(url_for('Vista.html'))
