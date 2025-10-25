const validateNombre = (Nombre) => {
    if (!Nombre) return false;
    let lengthValid = Nombre.trim().length >=3;
    return lengthValid;
};



const validateComentario = (Comentario) => {
    if (!Comentario) return false;
    let lengthValid = Comentario.length <= 300;

    return lengthValid
};



const validateForm = () => {

    let Nombre = document.getElementById("nombre").value;
    let Comentario = document.getElementById("coment").value;


    if (!validateNombre(Nombre)) {
        mensaje('Nombre inválido');
        return false;
    }
    if (!validateComentario(Comentario)) {
        mensaje('Comentario inválido');
        return false;
    }


    return true
}



document.addEventListener('DOMContentLoaded', function() {

    cargar();
    

    document.getElementById('submit-btn').addEventListener('click', function() {
        const nombre = document.getElementById('nombre').value.trim();
        const texto = document.getElementById('coment').value.trim();
        
        if (validateForm()) {

            const btn = this;
            const originalText = btn.textContent;
            btn.textContent = 'Enviando';
            btn.disabled = true;
            
            enviar(nombre, texto)
                .finally(() => {
                    btn.textContent = originalText;
                    btn.disabled = false;
                });
        }
    });
});


// FUNCIIONES


async function cargar () {
    try {
        const response = await fetch(`/api/comentarios/${AVISO_ID}`);
        const data = await response.json();

        if (data.success) {
            mostrar(data.comentarios);
        }
        else {
            console.error('Error al cargar comentarios:', data.error);
        }
    }catch (error){
        console.error('Error', error);
    }
}

function mostrar(comentarios) {
    const container = document.getElementById('comentarios-container'); 

    if (!container) {
        container.innerHTML = '<p>No hay Comentarios</p>'
        return;
    }
    const comentariosHTML = comentarios.map(comentario => 
`
        <div style ="border: 1px solid #000000ff;">
            <strong>${comentario.nombre}</strong>
            <small>${comentario.fecha}</small>
            <p>${comentario.texto}</p>
        </div>
    `).join('');
    
    container.innerHTML = comentariosHTML;
    
}



async function enviar(nombre, texto) {
    try{
        const response = await fetch('/api/comentarios', {
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json',
            },
            body : JSON.stringify({
                aviso_id : AVISO_ID,
                nombre: nombre,
                texto : texto
            })
        });
        const data = await response.json();

        if (data.success) {
            mensaje ('Comentario Agregado', 'success');

            document.getElementById('nombre').value = '';
            document.getElementById('coment').value = '';
            
            cargar();
        } else {
            mensaje('Error: ' + data.error, 'error');
        }
        
    } catch (error) {
        console.error('Error:', error);
        mensaje('Error de conexión', 'error');
    }
}





function mensaje (mensaje, tipo) {

    const messageDiv = document.getElementById('mensaje');
    messageDiv.textContent = mensaje;
    messageDiv.style.display = 'block';
    messageDiv.style.color = tipo === 'success' ? 'green' : 'red';
    
    setTimeout(() => {
        messageDiv.style.display = 'none';
    }, 5000);
}


