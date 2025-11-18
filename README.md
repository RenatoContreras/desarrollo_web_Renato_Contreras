#--------------------- index.html ---------------------

Muestra una lista con ayuda de thymeleaf, con algunos datos de todos los avisos de adopción, en la columna de nota, se muestra el promedio, y junto a esta hay otra columna que permite abrir un modal para evaluar con notas del 1 al 7, con un boton para cada nota entera y con la posibilidad de cerrar el modal o enviar la nota.

#--------------------- app.js --------------------- 

Maneja la interaccion con el indice, mostrando mensajes y/o errores al momento de evaluar avisos, así como las llamadas asincronas 

#--------------------- services ---------------------

ApiService gestiona las evaluaciones y notas con las funciones obtenerPromedioNotas y agregarNota
AppService gestiona los avisos con la función obtenerTodosLosAvisos()

#--------------------- models ---------------------

Se definen entidades Aviso, Nota, Comuna y sus relaciones, y sus repositorios

#--------------------- controllers ---------------------

AppController renderiza la vista principal, carga lista de avisos. Por otro lado ApiController maneja las api's

