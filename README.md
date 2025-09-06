#--------------------- index.html ---------------------

Tiene una breve bienvenida y muestra opsiones para ir a:

Agregar Aviso Adopción
Listado Adopciones
Estadísticas

Además de una tabla con 5 avisos de adopción.


#--------------------- validación.js ---------------------
Para validar se crea una funcion para cada input

Para validar Select simplemente se pide que se haya seleccionado alguna opción

Para cada otro input del formulario se valida que exista información, además de validaciones especificas, como largo de inputs mínimo o máximo, o en caso de inputs numericos como teléfono o edad se valida que existan solo números, en caso del email, se valida que haya texto antes y después del @ y entre 2 y 3 letras despues del punto (opción .com, .cl, etc). Y para Fotos se valida que sea además que sea del tipo esperado de input. 

Aquí también se configuran los botones, para enviar, y con opción de volver a la página de inicio o volver al formulario.


#--------------------- agregar.html  --------------------- 


Formulario que solicita información para agregar un aviso de adopción.



#--------------------- select.js --------------------- 


Sirve en este caso para que al seleccionar una Región especifica, en la opción de Comuna aparezcan las relacionadas con esta Región.


#--------------------- estadísticas.html  --------------------- 

Muestra 3 imagenes estáticas que simulan Gráficos de Estadísticas.

#--------------------- listado.html  --------------------- 

Muestra una lista con avisos de adopción, e información sobre estos, tal que si se hace click en alguna fila, lleva a esta misma información sobre la mascota, con máyor detalle y más ordenada.

#--------------------- información.html  --------------------- 

Segun el id de la fila de listado.html en que se hace click, se muestra la información más especifica del id de la mascota seleccionada