import re
from datetime import datetime, timedelta




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

    unidades_permitidas = ['meses', 'años']
    
    if unidad not in unidades_permitidas:
        return False, "Unidad de medida no válida"
    
    return True, ""