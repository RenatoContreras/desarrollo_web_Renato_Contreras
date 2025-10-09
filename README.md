#--------------------- index.html ---------------------

Tiene una breve bienvenida y muestra opsiones para ir a:

Agregar Aviso Adopción Listado Adopciones Estadísticas

Además de una tabla con 5 avisos de adopción, la cual mustra los últimos 5 avisos que se suben a la base de datos.


#--------------------- agregar.html ---------------------

Formulario que solicita información para agregar un aviso de adopción. Se modifica para que acceda a la base de datos para recoger las regiones y comunas, con ayuda de la función cargar comunas. 


#--------------------- estadísticas.html ---------------------

Muestra 3 imagenes estáticas que simulan Gráficos de Estadísticas. Se mantiene igual.

#--------------------- listado.html ---------------------

Muestra una lista con avisos de adopción, e información sobre estos, tal que si se hace click en alguna fila, lleva a esta misma información sobre la mascota, con máyor detalle y más ordenada. Se cambia a un listado que muestra los últimos 5 avisos, com mayor detalle que los del indice, y que además para acceder a aun más detalle, si se hace click sobre las filas, conduce al template información. Utiliza jinja para actualizar las tablas

#--------------------- información.html ---------------------

Segun el id de la fila de listado.html en que se hace click, se muestra la información más especifica del id de la mascota seleccionada, obtenida ahora desde la base de datos.






















