// Variables globales
let avisoActual = null;
let notaSeleccionada = null;

// Función para abrir el modal de evaluación
function evaluarAviso(avisoId) {
    avisoActual = avisoId;
    notaSeleccionada = null;
    resetBotonesNota();
    const modal = new bootstrap.Modal(document.getElementById('modalEvaluar'));
    modal.show();
}

// Función para seleccionar una nota
function seleccionarNota(nota) {
    notaSeleccionada = nota;
    
    // Remover clase active de todos los botones
    resetBotonesNota();
    
    // Agregar clase active al botón seleccionado
    const botones = document.querySelectorAll('.nota-btn');
    botones[nota - 1].classList.add('active');
}

// Función para resetear los botones de nota
function resetBotonesNota() {
    document.querySelectorAll('.nota-btn').forEach(btn => {
        btn.classList.remove('active');
    });
}

// Función para confirmar la evaluación
function confirmarEvaluacion() {
    if (avisoActual === null || notaSeleccionada === null) {
        mostrarMensaje('Por favor seleccione una nota', 'warning');
        return;
    }
    
    // Mostrar loading
    const confirmBtn = document.querySelector('#modalEvaluar .btn-primary');
    const originalText = confirmBtn.innerHTML;
    confirmBtn.innerHTML = '<span class="spinner-border spinner-border-sm" role="status"></span> Procesando...';
    confirmBtn.disabled = true;
    
    fetch(`/api/avisos/${avisoActual}/nota`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nota: notaSeleccionada })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la respuesta del servidor');
        }
        return response.json();
    })
    .then(data => {
        if (data.success) {
            // Actualizar el promedio en la interfaz
            actualizarPromedioEnInterfaz(avisoActual, data.nuevoPromedio);
            
            // Cerrar modal
            const modal = bootstrap.Modal.getInstance(document.getElementById('modalEvaluar'));
            modal.hide();
            
            mostrarMensaje('Nota agregada exitosamente!', 'success');
        } else {
            mostrarMensaje('Error: ' + data.error, 'danger');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        mostrarMensaje('Error al conectar con el servidor', 'danger');
    })
    .finally(() => {
        // Restaurar botón
        confirmBtn.innerHTML = originalText;
        confirmBtn.disabled = false;
    });
}

// Función para actualizar el promedio en la interfaz
function actualizarPromedioEnInterfaz(avisoId, nuevoPromedio) {
    const promedioElement = document.getElementById(`promedio-${avisoId}`);
    if (promedioElement) {
        promedioElement.textContent = nuevoPromedio.toFixed(1);
        
        // Efecto visual de actualización
        promedioElement.classList.add('text-success');
        setTimeout(() => {
            promedioElement.classList.remove('text-success');
        }, 2000);
    }
}

// Función para mostrar mensajes temporales
function mostrarMensaje(mensaje, tipo) {
    // Crear contenedor de alertas si no existe
    let alertContainer = document.getElementById('alert-container');
    if (!alertContainer) {
        alertContainer = document.createElement('div');
        alertContainer.id = 'alert-container';
        alertContainer.style.cssText = 'position: fixed; top: 20px; right: 20px; z-index: 1050; min-width: 300px;';
        document.body.appendChild(alertContainer);
    }
    
    // Crear alerta
    const alertId = 'alert-' + Date.now();
    const alerta = document.createElement('div');
    alerta.id = alertId;
    alerta.className = `alert alert-${tipo} alert-dismissible fade show`;
    alerta.innerHTML = `
        ${mensaje}
        <button type="button" class="btn-close" onclick="document.getElementById('${alertId}').remove()"></button>
    `;
    
    alertContainer.appendChild(alerta);
    
    // Auto-eliminar después de 4 segundos
    setTimeout(() => {
        const alertToRemove = document.getElementById(alertId);
        if (alertToRemove) {
            alertToRemove.remove();
        }
    }, 4000);
}

// Event listeners cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', function() {
    // Agregar tooltips si es necesario
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    console.log('Aplicación de evaluación de avisos cargada correctamente');
});

// Manejar errores no capturados
window.addEventListener('error', function(e) {
    console.error('Error en la aplicación:', e.error);
    mostrarMensaje('Ocurrió un error inesperado', 'danger');
});