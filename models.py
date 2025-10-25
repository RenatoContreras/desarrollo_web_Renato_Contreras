from sqlalchemy import Column, Integer, String, ForeignKey, BigInteger, DateTime, Enum, Text
from sqlalchemy.orm import relationship
from database.db import Base



#-------------------- Models --------------------#


class Aviso(Base):
    __tablename__ = 'aviso_adopcion' 
    
    id = Column(Integer, primary_key=True)
    fecha_ingreso = Column(DateTime, nullable=False)
    comuna_id = Column(Integer, ForeignKey('comuna.id'))
    sector = Column(String(100))
    nombre = Column(String(100))
    email = Column(String(100))
    celular = Column(String(20))
    tipo = Column(String(50))
    cantidad = Column(Integer)
    edad = Column(Integer)
    unidad_medida = Column(String(10))
    fecha_entrega = Column(DateTime)
    descripcion = Column(Text)

    #relationship
    comuna = relationship('Comuna', backref='avisos')
    contactos = relationship('ContactarPor', backref='aviso')
    fotos = relationship('Foto', backref='avisos')  


class Comentario (Base):
    __tablename__ = 'comentario'
    id = Column(BigInteger, primary_key=True, autoincrement = True)
    nombre = Column(String(100))
    texto = Column(Text)
    fecha = Column(DateTime, nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    aviso = relationship('Aviso', backref='comentarios')




class Foto (Base):
    __tablename__ = 'foto'

    id = Column(BigInteger, primary_key=True, autoincrement = True)
    ruta_archivo = Column(String(300), nullable=False)
    nombre_archivo = Column(String(300), nullable=False)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)

    # relationship

class ContactarPor(Base):
    __tablename__ = 'contactar_por' 
    
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))  
    identificador = Column(String(100))  
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id')) 



class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)

    comunas = relationship('Comuna', backref='region', lazy=True)

class Comuna(Base):
    __tablename__ = 'comuna'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

