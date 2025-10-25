import os, hashlib, filetype
from flask import Flask, request, render_template, redirect, url_for, flash, session, jsonify #, current_app
from flask_cors import cross_origin
from datetime import datetime, timedelta
from database.db import get_db
from models import Region, Comuna, Aviso, ContactarPor, Foto, Comentario
from sqlalchemy.exc import SQLAlchemyError
#from utils.validations import validar_email, validar_telefono, validar_nombre, validar_edad, validar_fecha, validar_descripcion, validar_sector, validar_comuna_id, validar_tipo_animal, validar_unidad_medida
from utils.validations import validar_todo, validar_comentarios
from werkzeug.utils import secure_filename
import time
from sqlalchemy import func

UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'programacionweb'







#----------------------- funciones -----------------------

def save_photos(fotos_files, aviso_id, db_session, upload_folder):

    try:

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        for file in fotos_files:
            if file and file.filename != '':
                try:

                    _filename = hashlib.sha256(
                        secure_filename(file.filename).encode("utf-8")
                    ).hexdigest()
                    

                    _extension = filetype.guess(file).extension
                    img_filename = f"{_filename}.{_extension}"
                    
                    file.save(os.path.join(upload_folder, img_filename))

                    foto = Foto(
                        ruta_archivo=img_filename, 
                        nombre_archivo=secure_filename(file.filename),  
                        aviso_id=aviso_id
                    )
                    db_session.add(foto)
                    print(f"Foto guardada: {img_filename} (original: {file.filename})")
                    
                except Exception as e:
                    print(f"Error al guardar foto {file.filename}: {str(e)}")
                    continue
        
        return True
        
    except SQLAlchemyError as e:
        print(f"Error de base de datos: {str(e)}")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

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
        


        return render_template('informacion.html', ultimos_avisos=ultimos_avisos, aviso_id=aviso_id)


    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        return redirect(url_for('listado'))

    finally:
        db.close()







@app.route('/api/comentarios', methods=['POST'])
def api_comentario():

    if request.method == 'POST':

        db_session = next(get_db())
        try:
            data = request.get_json()
            
            print("Datos recibidos:")
            for key, value in data.items():
                print(f"  {key}: {value}")

                
            # validaciones:

            valido, errores = validar_comentarios(data)

            if not valido:
                return jsonify({
                    'success': False, 
                    'error': ', '.join(errores)
                }), 400
            

            comentario = Comentario(

                nombre=data.get('nombre').strip(),  # .strip()
                texto=data.get('texto').strip(),   # .strip()
                fecha=datetime.now(),
                aviso_id = int(data.get('aviso_id'))
            )

            db_session.add(comentario)
            db_session.commit()

            return jsonify({
                'success' : True,
                'message' : 'Comentario Agregado',
                'comentario' : {
                    'id' : comentario.id,
                    'nombre' : comentario.nombre,
                    'texto' : comentario.texto,
                    'fecha' : comentario.fecha.strftime('%d-%m-%Y %H:%M')
                }
            })


        except Exception as e:
            db_session.rollback()

            return jsonify({
                'success' : False,
                'error' : str(e)
            }), 500
        
        finally:
            db_session.close()

@app.route ('/api/comentarios/<int:aviso_id>', methods=['GET'])
def get_comentario(aviso_id):
    db = next(get_db())
    try:
        comentarios = db.query(Comentario)\
        .filter_by(aviso_id=aviso_id)\
        .order_by(Comentario.fecha.desc()).all()

        comentarios_data =[]
        for comentario in comentarios:
            comentarios_data.append({
                    'id' : comentario.id,
                    'nombre' : comentario.nombre,
                    'texto' : comentario.texto,
                    'fecha' : comentario.fecha.strftime('%d-%m-%Y %H:%M')

                })
        return jsonify({
            'success' : True,
            'comentarios' : comentarios_data
        })
    except Exception as e:
        return jsonify({
            'success' : False,
            'error' : str(e)
        }), 500
    finally:
        db.close()






@app.route("/estadísticas", methods=["GET"])
def estadisticas():
    return render_template("estadisticas.html")

@app.route("/get-estadisticas-data", methods=["GET"])
@cross_origin(origin="127.0.0.1", supports_credentials=True)
def get_estadisticas_data():

    db_session = next(get_db())
    try:

        # Gráfico Lineas


        fecha_inicio = datetime.now() - timedelta(days=30)
    
        estadisticas = db_session.query(
            func.date(Aviso.fecha_ingreso).label('fecha'),
            func.count(Aviso.id).label('cantidad')
        ).filter(Aviso.fecha_ingreso >= fecha_inicio).group_by(func.date(Aviso.fecha_ingreso)).order_by(func.date(Aviso.fecha_ingreso)).all()



        fecha_actual = fecha_inicio.date()
        hoy = datetime.now().date()
        datos_completos = {}

        while fecha_actual <= hoy:
            datos_completos[fecha_actual.strftime("%Y-%m-%d")] = 0
            fecha_actual += timedelta(days=1)


        for fecha, cantidad in estadisticas:
            datos_completos[fecha.strftime("%Y-%m-%d")] = cantidad



        # Gráfico Torta

        data2 = db_session.query(
            Aviso.tipo,
            func.count(Aviso.id).label('cantidad')
        ).group_by(Aviso.tipo).all()

        # Gráfico Barras


        data_3 = db_session.query(
            func.date(Aviso.fecha_ingreso).label('fecha'),
            Aviso.tipo,
            func.count(Aviso.id).label('cantidad')
        ).group_by(func.date(Aviso.fecha_ingreso), Aviso.tipo).order_by(func.date(Aviso.fecha_ingreso)).all()

        datos_por_mes_tipo = {}
        
        for fecha, tipo, cantidad in data_3:
            if fecha:
                mes = fecha.strftime('%Y-%m')  #%Y-%m-%d
                clave = (mes, tipo)
                if clave not in datos_por_mes_tipo:
                    datos_por_mes_tipo[clave] = 0
                datos_por_mes_tipo[clave] += cantidad



        data3 = []
        for (mes, tipo), cantidad in datos_por_mes_tipo.items():
            data3.append({
                "mes": mes,
                "tipo": tipo,
                "cantidad": cantidad
            })


        # Todo


        Dota = {
            'data1': [
                {
                    'fecha': fecha,
                    'cantidad': cantidad
                    } for fecha, cantidad in datos_completos.items()],

            'data2': [
                {
                    'tipo': t,
                    'cantidad': c
                    } for t, c in data2],


            'data3' : data3

        }


        time.sleep(2)
        return jsonify(Dota)
    

    except Exception as e:
        print(f"Error obteniendo estadísticas: {str(e)}")
        return jsonify({"error": str(e)}), 500
    finally:
        db_session.close()






@app.route('/listado')
def listado():
    db = next(get_db())
    try:

        page = request.args.get('page', 1, type=int)

        Total = db.query(Aviso).count() 

        ultimos_avisos = db.query(Aviso)\
            .join(Comuna)\
            .join(Region)\
            .order_by(Aviso.fecha_ingreso.desc())\
            .offset((page - 1)*5)\
            .limit(5)\
            .all()
        
        Paginas = (Total + 4) // 5
        
        return render_template('listado.html', ultimos_avisos=ultimos_avisos, page = page, Paginas= Paginas)
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





            valido, errores = validar_todo(
                comuna_id=form_data.get('comuna_id'),
                sector=form_data.get('sector'),
                nombre=form_data.get('nombre'),
                email=form_data.get('email'),
                celular=form_data.get('celular'),
                tipo=form_data.get('tipo'),
                cantidad=form_data.get('cantidad'),
                edad=form_data.get('edad'),
                unidad_medida=form_data.get('unidad_medida'),
                fecha_entrega=form_data.get('fecha_entrega'),
                descripcion=form_data.get('descripcion'),
                db_session=db_session
            )


            if not valido:
                print('hay errores D:')
                for error in errores:
                    print(f'{error}')
                    flash(f'No se envio el formulario: {error}', 'error')
                regiones = db_session.query(Region).order_by(Region.nombre).all()                
                return render_template('agregar.html', regiones = regiones, sector=form_data.get('sector', ''),)



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

            #files = request.files
            fotos_files = files.getlist('fotos')
            if fotos_files and fotos_files[0].filename != '':
                save_photos(fotos_files, aviso.id, db_session, app.config['UPLOAD_FOLDER'])
                

            db_session.commit()
            flash('', 'success')
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


