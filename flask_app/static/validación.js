//validaciones para Agregar Aviso Adopción
const validateSelect = (select) => {
    if(!select) return false;
    return true
};

const validateSector = (Sector) => {
    if (!Sector) return false; 
    let lengthValid = Sector.trim().length >=5;
    return lengthValid;
};

const validateNombre = (Nombre) => {
    if (!Nombre) return false;
    let lengthValid = Nombre.trim().length >=3;
    return lengthValid;
};

const validateTeléfono = (Teléfono) => {
    if (!Teléfono) return false;
    let lengthValid = Teléfono.length >=8;

    let re = /^[0-9]+$/;
    let formatValid = re.test(Teléfono);

    return lengthValid && formatValid;
};

const validateEmail = (Email) => {
    if (!Email) return false;
    let lengthValid = Email.length >=8;

    let re = /^[\w.]+@[a-zA-Z]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = re.test(Email);

    return lengthValid && formatValid;

};

const validateId = (Id) => {
    if (!Id) return false;
    let lengthValid = Id.length >=8;

    return lengthValid;
};

const validateEdad = (Edad) => {
    if (!Edad) return false;
    let lengthValid = Edad.length >=1;

    return lengthValid;
};

const validateFecha = (Fecha) => {
    if (!Fecha) return false;
    else return true
};

const validateDescripción = (Descripción) => {
    if (!Descripción) return false;
    let lengthValid = Descripción.length <= 200;

    return lengthValid
};

const validateFoto = (Foto) => {
    if (!Foto || Foto.length === 0) return false;
    

    if (Foto.length < 1 || Foto.length > 5) return false;
    

    for (const file of Foto) {
        const esImagen = file.type.startsWith("image/");
        const esPDF = file.type === "application/pdf";
        
        if (!esImagen && !esPDF) {
            return false; 
        }
    }
    
    return true; 
};






const validateForm = () => {


    let formulario = document.forms["formulario"];
    let Región = formulario["Región"].value;
    let Comuna = formulario["Comuna"].value;
    let Sector = formulario["Sector"].value;

    let Nombre = formulario["Nombre"].value;
    let Email = formulario["Email"].value;
    let Teléfono = formulario["Teléfono"].value;
    let Contacto = formulario["Contacto"].value;
    let Id = formulario["Id"].value;

    let Tipo = formulario["Tipo"].value;
    let Edad = formulario["Edad"].value;
    let Unidad = formulario["Unidad"].value;
    let Fecha = formulario["Fecha"].value;
    let Descripción = formulario["Descripción"].value;
    let Foto = formulario["Foto"].files;


    //----------------------------------------------------------------------------------------------------//


    let invalidInputs = [];
    let isValid = true;
    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid &&= false;
    };


    if (!validateSelect(Región)) {
        setInvalidInput("Región");
    }
    if (!validateSelect(Comuna)) {
        setInvalidInput("Comuna");
    }
    if (!validateSector(Sector)) {
        setInvalidInput("Sector");
    }

    if (!validateNombre(Nombre)) {
        setInvalidInput("Nombre");
    }
    if (!validateEmail(Email)) {
        setInvalidInput("Email");
    }
    if (!validateTeléfono(Teléfono)) {
        setInvalidInput("Teléfono");
    }
    if (!validateSelect(Contacto)) {
        setInvalidInput("Contacto");
    }
    if (!validateId(Id)) {
        setInvalidInput("Id");
    }

    if (!validateSelect(Tipo)) {
        setInvalidInput("Tipo");
    }
    if (!validateEdad(Edad)) {
        setInvalidInput("Edad");
    }
    if (!validateSelect(Unidad)) {
        setInvalidInput("Unidad");
    }
    if (!validateFecha(Fecha)) {
        setInvalidInput("Fecha");
    }
    if (!validateDescripción(Descripción)) {
        setInvalidInput("Descripción");
    }
    if (!validateFoto(Foto)) {
        setInvalidInput("Foto");
    }


    let validationBox = document.getElementById ("val-box");
    let validationMessajeElem = document.getElementById ("val-msg");
    let validationListElem = document.getElementById ("val-list");
    let formContainer = document.querySelector (".main-container");

    if (!isValid) {
        validationListElem.C0 = ";"
        for (input of invalidInputs) {
            let listElement = document.createElement("li");
            listElement.innerText = input;
            validationListElem.append(listElement);
        }


        validationMessajeElem.innerText = "Campos Inválidos:";
        validationBox.hidden = false;

    } else {
        formulario.style.display = "none";

        validationMessajeElem.innerText = "Respuesta Válida, ¿Desea Enviar sus Respuestas o Volver?";
        validationListElem.textContent = "";

        // estilos para validation box



        // botones:
        // Botones de confirmación
        let submitButton = document.createElement("button");
        submitButton.innerText = "✅ Sí, Enviar";
        submitButton.style.margin = "10px";
        submitButton.style.padding = "10px 20px";
        submitButton.style.backgroundColor = "#28a745";
        submitButton.style.color = "white";
        submitButton.style.border = "none";
        submitButton.style.borderRadius = "5px";
        submitButton.style.cursor = "pointer";

        submitButton.addEventListener("click", () => {
            // 👇 ENVIAR EL FORMULARIO
            formulario.submit();
        });

        let backButton = document.createElement("button");
        backButton.innerText = "↩️ Volver y Corregir";
        backButton.style.margin = "10px";
        backButton.style.padding = "10px 20px";
        backButton.style.backgroundColor = "#6c757d";
        backButton.style.color = "white";
        backButton.style.border = "none";
        backButton.style.borderRadius = "5px";
        backButton.style.cursor = "pointer";

        backButton.addEventListener("click", () => {
            formulario.style.display = "block";
            validationBox.hidden = true;
        });

        validationListElem.appendChild(submitButton);
        validationListElem.appendChild(backButton);
        validationBox.hidden = false;
    }
};

// Agregar el event listener al botón
let sumbitBtn = document.getElementById("sumbit-btn");
if (sumbitBtn) {
    sumbitBtn.addEventListener("click", validateForm);
}

