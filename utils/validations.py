import re
from datetime import datetime, timedelta


#---------------------- FORMULARIO ----------------------#

def validar_email(email):

    if not email:
        return False, "El email es requerido"
    
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(patron, email):
        return False, "El formato del email no es válido"
    
    return True, ""

def validar_telefono(celular):

    if not celular:
        return False, "El teléfono es requerido"
    
    celular_limpio = re.sub(r'[\s\-]', '', celular)
    
    if not re.match(r'^[0-9]{8,9}$', celular_limpio):
        return False, "El teléfono debe tener 8 o 9 dígitos"
    
    return True, ""

def validar_nombre(nombre):

    if not nombre:
        return False, "El nombre es requerido"
    
    if len(nombre.strip()) < 3:
        return False, "El nombre debe tener al menos 3 carácteres"
    
    if len(nombre) > 100:
        return False, "El nombre es demasiado largo"
    

    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\.\-]+$', nombre):
        return False, "El nombre contiene caracteres no válidos"
    
    return True, ""

def validar_edad(edad):

    try:
        edad_num = int(edad)
        if edad_num < 0 or edad_num > 60:
            return False, "La edad debe estar entre 0 y 60"
        return True, ""
    except (ValueError, TypeError):
        return False, "La edad debe ser un número válido"

def validar_fecha(fecha_entrega):

    try:
        fecha_obj = datetime.strptime(fecha_entrega, '%Y-%m-%dT%H:%M')
        if fecha_obj < datetime.now():
            return False, "La fecha no puede ser en el pasado"
        
        if fecha_obj > datetime.now() + timedelta(days=365):
            return False, "La fecha no puede ser más de 1 año en el futuro"
            
        return True, ""
    except ValueError:
        return False, "Formato de fecha inválido"

def validar_descripcion(descripcion):

    if not descripcion:
        return False, "descripción obligatoria"  
    
    if len(descripcion) > 500:
        return False, "La descripción no puede tener más de 500 caracteres"
    
    return True, ""

def validar_sector(sector):

    if not sector:
        return False, " sector obligatorio" 
    
    if len(sector) > 100:
        return False, "El sector es demasiado largo"
    
    return True, ""

def validar_comuna_id(comuna_id, db_session):

    from models import Comuna  # Import aquí para evitar circular imports
    
    try:
        comuna_id_num = int(comuna_id)
        comuna = db_session.query(Comuna).filter_by(id=comuna_id_num).first()
        
        if not comuna:
            return False, "La comuna seleccionada no existe"
        
        return True, ""
    except (ValueError, TypeError):
        return False, "ID de comuna inválido"

def validar_tipo_animal(tipo):

    tipos_permitidos = ['perro', 'gato']
    
    if tipo not in tipos_permitidos:
        return False, "Tipo de animal no válido"
    
    return True, ""

def validar_unidad_medida(unidad):

    unidades_permitidas = ['me', 'añ']
    
    if unidad not in unidades_permitidas:
        return False, "Unidad de medida no válida"
    
    return True, ""




def validar_cantidad(cantidad):

    try:
        cantidad_num = int(cantidad)
        if cantidad_num < 1 or cantidad_num > 60:
            return False, "La cantidad debe estar entre 1 y 60"
        return True, ""
    except (ValueError, TypeError):
        return False, "La cantidad debe ser un número válido"






def validar_todo(comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion, db_session=None):

    errores = []
    
    valido, mensaje = validar_email(email)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_telefono(celular)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_nombre(nombre)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_edad(edad)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_fecha(fecha_entrega)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_descripcion(descripcion)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_sector(sector)
    if not valido:
        errores.append(mensaje)
    
    if db_session:
        valido, mensaje = validar_comuna_id(comuna_id, db_session)
        if not valido:
            errores.append(mensaje)
    
    valido, mensaje = validar_tipo_animal(tipo)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_unidad_medida(unidad_medida)
    if not valido:
        errores.append(mensaje)
    
    valido, mensaje = validar_cantidad(cantidad)
    if not valido:
        errores.append(mensaje)
    
    return len(errores) == 0, errores







#---------------------- COMENTARIOS ----------------------#



def validar_nombre_comentario(nombre):

    if not nombre:
        return False, "El nombre es requerido"
    
    if len(nombre.strip()) < 3:
        return False, "El nombre debe tener al menos 3 carácteres"
    
    if len(nombre) > 80:
        return False, "El nombre es demasiado largo"
    

    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\.\-]+$', nombre):
        return False, "El nombre contiene caracteres no válidos"
    
    return True, ""




def validar_comentario_comentario(comentario):

    if not comentario:
        return False, "descripción obligatoria"  
    
    if len(comentario) < 5:
        return False, "La descripción no puede tener menos de 5 caracteres"
    
    if len(comentario) > 300:
        return False, "La descripción no puede tener más de 300 caracteres"
    
    patrones = [
            r'(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER|CREATE|EXEC)\b)',
            r'(<script|javascript:|onload=|onerror=)',
            r'(\b(OR|AND)\b\s+\b(1=1|2=2)\b)',
        ]
        
    texto_upper = comentario.upper()
    for patron in patrones:
        if re.search(patron, texto_upper, re.IGNORECASE):
            return False, "El comentario contiene contenido no permitido"

        
    return True, ""



def validar_comentarios (data):

    nombre = data.get('nombre', '').strip()
    comentario = data.get('texto', '').strip()

    errores = []

    valido, mensaje = validar_nombre(nombre)
    if not valido:
        errores.append(mensaje)


    valido, mensaje = validar_comentario_comentario(comentario)
    if not valido:
        errores.append(mensaje)

    return len(errores) == 0, errores