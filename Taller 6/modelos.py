from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import date

class persona(db.Model):
    __tablename__ = 'Persona'
    id = db.Column(db.Integer, primary_key = True)
    nombres = db.Column(db.String(50))
    apellidos = db.Column(db.String(50))
    idtipodocumento = db.Column(db.Integer, ForeignKey('TipoDocumento.id'))
    documento = db.Column(db.String)
    lugarresidencia = db.Column(db.Integer, ForeignKey('Ciudad.id'))
    fechanacimiento = db.Column(db.Date)
    email = db.Column(db.String(50))
    telefono = db.Column(db.String(50))
    usuario = db.Column(db.String(50))
    password = db.Column(db.String(50))
    tipodocumento = relationship("tipodocumento")
    ciudad = relationship("ciudad")


class tipodocumento(db.Model):
    __tablename__ = 'TipoDocumento'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))


class ciudad(db.Model):
    __tablename__ = 'Ciudad'
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(50))
    descripcion = db.Column(db.String(100))
