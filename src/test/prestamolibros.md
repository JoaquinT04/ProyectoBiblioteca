# Test Modulo Prestamo de Libros
Fecha 25/05/23
## Funcionalidad para agregar prestamo
 
Formulario de carga con Campos (Libro, Socio, Empleado):
<details><summary>Primera Carga</summary>

![Imagen](assets/images/prestamoLibros/primeracarga.png)

Carga Exitosa   

</details>

<details><summary>Segunda Carga</summary>

![Imagen](assets/images/prestamoLibros/segundacarga.png)

Segunda carga, intento realizar prestamo de un libro el cual ya estaba en prestamo...
  
 reintentando...  

 ![Imagen](assets/images/prestamoLibros/segundacarga2.png)  
  
 Carga exitosa: Se corrigio agregando un validar en el campo del libro, con solo cambiar a un libro disponible se puede realizar la carga exitosa


</details>

<details><summary>Tercer Carga</summary>

![Imagen](assets/images/prestamoLibros/tercercarga.png)

Carga exitosa: Se realizo carga con un socio que ya tenia un prestamo de otro libro

</details>

<details><summary>Cuarta Carga</summary>

![Imagen](assets/images/prestamoLibros/cuartacarga.png)

Carga exitosa: Se cambio de socio y de empleado, carga exitosa.

</details>

## Funcionalidad para visualizar el listado de Libros prestados
Utilizacion de Template listar.html usando una tabla se vizualizan los campos:
![Imagen](assets/images/prestamoLibros/listado.png)
Botones Borrar, Editar y Agregar Prestamo

## Funcionalidad para actualizar registros
Funcion del boton editar correcta despliega los datos correctos del campo elegido
![Imagen](assets/images/prestamoLibros/editar.png)
cambio de nombre de Antonio a Pedro
![Imagen](assets/images/prestamoLibros/modificado.png)
Guardado Exitoso

## Funcionalidad Borrar registros
Para la funcion de Borrar, se agrego un campo "activo" al modelo, para no borrar el registro y quede constancia en la base de datos, por lo tanto al borrar se desactiva el prestamo.

Listado sin borrar 
![Imagen](assets/images/prestamoLibros/listado2.png)

Borrando el prestamo del libro "El gato negro"
    Se consulta previamente si esta seguro de la accion de borrar
![Imagen](assets/images/prestamoLibros/borrandoc.png)

Funcionalidad Exitosa se muestra el listado del prestamo actualizado 
![Imagen](assets/images/prestamoLibros/listado3.png)

* Como bonus se vuelve a agregar el prestamo del libro que se habia borrado:
![Imagen](assets/images/prestamoLibros/agregandoprestamo.png)

Se muestro la carga exitosa:
![Imagen](assets/images/prestamoLibros/listadofinal.png)



## Registros en el Admin 
**Admin**
La base de datos se ve reflejada correctamente en el Admin.
![Imagen](assets/images/prestamoLibros/admin.jpg)

