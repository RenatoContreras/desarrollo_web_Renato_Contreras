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

const validateCantidad = (Cantidad) => {

    if (!Cantidad) return false;
    let lengthValid = Cantidad.length >=1;

    return lengthValid;

};



const validateForm = () => {
    let formulario = document.forms["formulario"];

    let Región = formulario["region_id"].value;
    let Comuna = formulario["comuna_id"].value;
    let Sector = formulario["sector"].value;

    let Nombre = formulario["nombre"].value;
    let Email = formulario["email"].value;
    let Teléfono = formulario["celular"].value;
    let Contacto = formulario["contactos0plataforma"].value;
    let Id = formulario["contactos0identificador"].value;

    let Tipo = formulario["tipo"].value;
    let Edad = formulario["edad"].value;
    let Cantidad = formulario["cantidad"].value;
    let Unidad = formulario["unidad_medida"].value;
    let Fecha = formulario["fecha_entrega"].value;
    let Descripción = formulario["descripcion"].value;
    let Foto = formulario["fotos"].files;


    //-------------------------------------------------------------------------//


    let invalidInputs = [];
    let isValid = true;

    const setInvalidInput = (inputName) => {
        invalidInputs.push(inputName);
        isValid = false;
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
    if (!validateCantidad(Cantidad)) {
        setInvalidInput("Cantidad");
    }




    let validationBox = document.getElementById ("val-box");
    let validationMessajeElem = document.getElementById ("val-msg");
    let validationListElem = document.getElementById ("val-list");
    // let formContainer = document.querySelector (".main-container");

    validationListElem.innerHTML = ""; // Limpiar lista


    if (!isValid) {
        // Mostrar errores
        validationMessajeElem.innerText = "Campos Inválidos:";
        invalidInputs.forEach(input => {
            let listElement = document.createElement("li");
            listElement.innerText = input;
            validationListElem.appendChild(listElement);
        });
        validationBox.hidden = false;
    } else {

        formulario.style.display = "none";
        validationMessajeElem.innerText = "¿Está seguro?";
        

        let yesButton = document.createElement("button");
        yesButton.innerText = "Si, enviar";
        yesButton.addEventListener("click", () => {

            validationMessajeElem.innerText = "Hemos recibido la información de adopción, muchas gracias y suerte!";
            validationListElem.innerHTML = "";
            
            let homeButton = document.createElement("button");
            homeButton.innerText = "Volver a la portada";
            homeButton.addEventListener("click", () => {
                window.location.href = "/"; 
            });
            validationListElem.appendChild(homeButton);
            

            formulario.submit();
        });
        

        let noButton = document.createElement("button");
        noButton.innerText = "No, volver al formulario";
        noButton.addEventListener("click", () => {
            formulario.style.display = "block";
            validationBox.hidden = true;
        });

        validationListElem.appendChild(yesButton);
        validationListElem.appendChild(noButton);
        validationBox.hidden = false;
    }
};

let sumbitBtn = document.getElementById("submit-btn");
sumbitBtn.addEventListener("click", validateForm);