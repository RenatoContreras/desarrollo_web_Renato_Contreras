#--------------------- index ---------------------

Tiene una breve bienvenida y muestra opsiones para ir a:

Agregar Aviso Adopción Listado Adopciones Estadísticas

Además de una tabla con 5 avisos de adopción, la cual mustra los últimos 5 avisos que se suben a la base de datos.

#--------------------- agregar ---------------------

Formulario que solicita información para agregar un aviso de adopción. Accede a la base de datos para recoger las regiones y comunas, con ayuda de la función cargar comunas. 


#--------------------- estadísticas ---------------------

Muestra 3 gráficos que ahora recogen datos desde la base de datos. Para estos se usa la biblioteca Highcharts de (https://www.highcharts.com/blog/products/highcharts/) y la ruta de get-estadisticas en app.py la cual recoge los datos de la db. Se usan llamadas con fetch para implementar los gráficos del lado del cliente. 

#--------------------- listado ---------------------

Muestra una lista con avisos de adopción, e información sobre estos, tal que si se hace click en alguna fila, lleva a esta misma información sobre la mascota, con máyor detalle y más ordenada. Se cambia a un listado que muestra los últimos 5 avisos, com mayor detalle que los del indice, y que además para acceder a aun más detalle, si se hace click sobre las filas, conduce al template información. Utiliza jinja para actualizar las tablas
Se cambia el paginado y la cantidad de fotos se corrige

#--------------------- información ---------------------

Se le agrega la funcionalidad de ingresar comentarios, así como de visualizarlos sin recargar la página. Se cuenta con inputs de nombre y comentario, los cuales se validan en el frontend y backend, y de cumplir con las restricciones se insertan los datos en la base de datos. Por otro lado se muestra el listado de comentarios usando llamadas asincronas desde el lado del cliente, utilizando la función de fetch















