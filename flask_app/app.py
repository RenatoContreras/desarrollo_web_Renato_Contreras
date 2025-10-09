import os
from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify
from datetime import datetime
from database.db import get_db
from models import Region, Comuna, Aviso, ContactarPor, Foto
from utils.validations import validar_email, validar_telefono, validar_nombre, validar_edad, validar_fecha, validar_descripcion, validar_sector, validar_comuna_id, validar_tipo_animal, validar_unidad_medida



UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'programacionweb'

#-------------------- Rutas --------------------#



if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)



@app.route('/')
def index():
    db = next(get_db())
    try:

        ultimos_avisos = db.query(Aviso)\
            .join(Comuna)\
            .join(Region)\
            .order_by(Aviso.fecha_ingreso.desc())\
            .limit(5)\
            .all()
        
        return render_template('index.html', ultimos_avisos=ultimos_avisos)
    finally:
        db.close()


@app.route('/estadisticas')
def estadisticas():
    return render_template('estadísticas.html')


@app.route('/listado')
def listado():
    db = next(get_db())
    try:

        ultimos_avisos = db.query(Aviso)\
            .join(Comuna)\
            .join(Region)\
            .order_by(Aviso.fecha_ingreso.desc())\
            .limit(5)\
            .all()
        
        return render_template('listado.html', ultimos_avisos=ultimos_avisos)
    finally:
        db.close()


@app.route('/informacion/<int:aviso_id>')
def informacion(aviso_id):
    db = next(get_db())
    try:

        ultimos_avisos = db.query(Aviso)\
            .join(Comuna)\
            .join(Region)\
            .outerjoin(ContactarPor)\
            .filter(Aviso.id == aviso_id)\
            .first()
                
        return render_template('informacion.html', ultimos_avisos=ultimos_avisos)

    finally:
        db.close()





@app.route('/agregar')
def agregar():
    session['ultima_pagina'] = 'agregar'
    
    db = next(get_db())
    try:
        regiones = db.query(Region).order_by(Region.nombre).all()
        return render_template('agregar.html', regiones=regiones)
    finally:
        db.close()



@app.route('/comunas/<int:region_id>')
def obtener_comunas(region_id):
    session['ultima_region_consultada'] = region_id
    
    db = next(get_db())
    try:
        comunas = db.query(Comuna).filter_by(region_id=region_id).order_by(Comuna.nombre).all()
        return jsonify([{'id': comuna.id, 'nombre': comuna.nombre} for comuna in comunas])
    finally:
        db.close()




@app.route('/formulario', methods=['POST'])
def formulario():
    if request.method == 'POST':
        db_session = next(get_db())
        try:
            form_data = request.form
            files = request.files
            
            print("Datos recibidos del formulario:")
            for key, value in form_data.items():
                print(f"  {key}: {value}")

            errores = []

            campos_obligatorios = ['comuna_id', 'nombre', 'email', 'celular', 'tipo', 'edad', 'unidad_medida', 'fecha_entrega', 'descripcion','sector']
            for campo in campos_obligatorios:
                if not form_data.get(campo):
                    errores.append(f"El campo {campo} es requerido")



            if errores:
                for error in errores:
                    flash(error, 'error')
                

                regiones = db_session.query(Region).order_by(Region.nombre).all()
                return render_template('agregar.html', regiones=regiones)  
            

            if not errores:
                # Email
                email_valido, msg_email = validar_email(form_data.get('email'))
                if not email_valido:
                    errores.append(msg_email)

                # Teléfono
                telefono_valido, msg_telefono = validar_telefono(form_data.get('celular'))
                if not telefono_valido:
                    errores.append(msg_telefono)

                # Nombre
                nombre_valido, msg_nombre = validar_nombre(form_data.get('nombre'))
                if not nombre_valido:
                    errores.append(msg_nombre)

                # Edad
                edad_valida, msg_edad = validar_edad(form_data.get('edad'))
                if not edad_valida:
                    errores.append(msg_edad)

                # Fecha
                fecha_valida, msg_fecha = validar_fecha(form_data.get('fecha_entrega'))
                if not fecha_valida:
                    errores.append(msg_fecha)

                # Descripción
                descripcion_valida, msg_desc = validar_descripcion(form_data.get('descripcion'))
                if not descripcion_valida:
                    errores.append(msg_desc)

                # Sector
                sector_valido, msg_sector = validar_sector(form_data.get('sector'))
                if not sector_valido:
                    errores.append(msg_sector)

                # Comuna
                comuna_valida, msg_comuna = validar_comuna_id(form_data.get('comuna_id'), db_session)
                if not comuna_valida:
                    errores.append(msg_comuna)

                # Tipo
                tipo_valido, msg_tipo = validar_tipo_animal(form_data.get('tipo'))
                if not tipo_valido:
                    errores.append(msg_tipo)

                # Unidad
                unidad_valida, msg_unidad = validar_unidad_medida(form_data.get('unidad_medida'))
                if not unidad_valida:
                    errores.append(msg_unidad)


                  


            aviso = Aviso(
                comuna_id=int(form_data.get('comuna_id')),
                sector=form_data.get('sector', ''),
                nombre=form_data.get('nombre', ''),
                email=form_data.get('email', ''),
                celular=form_data.get('celular', ''),
                tipo=form_data.get('tipo', ''),
                cantidad=form_data.get('cantidad', ''),
                edad=int(form_data.get('edad', 0)),
                unidad_medida=form_data.get('unidad_medida', ''),
                fecha_entrega=datetime.strptime(form_data.get('fecha_entrega'), '%Y-%m-%dT%H:%M'),
                descripcion=form_data.get('descripcion', ''),
                fecha_ingreso=datetime.now()
            )

            db_session.add(aviso)
            db_session.flush()

            # Procesar contactos
            i = 0
            while f'contactos{i}plataforma' in form_data:
                plataforma = form_data.get(f'contactos{i}plataforma')
                identificador = form_data.get(f'contactos{i}identificador')

                if plataforma and identificador:
                    contacto = ContactarPor(
                        nombre=plataforma,
                        identificador=identificador,
                        aviso_id=aviso.id
                    )
                    db_session.add(contacto)
                i += 1


            fotos_files = files.getlist('fotos')
            if fotos_files and fotos_files[0].filename != '':
                # save_photos(fotos_files, aviso.id)
                pass

            db_session.commit()
            flash('Aviso creado', 'success')
            return redirect(url_for('index'))

        except Exception as e:
            db_session.rollback()
            print(f"Error en formulario {str(e)}")
            import traceback
            traceback.print_exc()
            
            flash(f'Error al crear el aviso {str(e)}', 'error')
            
            regiones = db_session.query(Region).order_by(Region.nombre).all()
            return render_template('agregar.html', regiones=regiones)
        
        finally:
            db_session.close()

    return redirect(url_for('agregar'))

            




if __name__ == '__main__':
    app.run(debug=True)
