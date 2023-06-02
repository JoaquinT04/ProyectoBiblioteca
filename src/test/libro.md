# Test Modulo Libro
Fecha 02/06/23

## Funcionalidad para agregar nuevos registros
 
Formulario de carga con Campos: titulo, descripcion, isbn y autor (estado activo por defecto)
<details><summary>Primera Carga</summary>

![Imagen](assets/images/libro/carga_exitosa.png)

Carga Exitosa.

</details>

<details><summary>Segunda Carga</summary>

![Imagen](assets/images/libro/carga02.png)
Carga Fallida. Se muestra error en Titulo.

Se corrige.  
  
Carga exitosa.

</details>

<details><summary>Tercer Carga</summary>

![Imagen](assets/images/empleado/carga03.png)
Carga Fallida. Se muestra mensaje, en ISBN solo se permiten 13 digitos.

Se corrige.

Carga exitosa.

</details>

<details><summary>Cuarta Carga</summary>

![Imagen](assets/images/empleado/carga04.png)
Carga Fallida. Se muestra mensaje de que debe elegirse un autor.

Se corrige.

Carga exitosa

</details>

<details><summary>Quinta Carga</summary>

![Imagen](assets/images/libro/carga05.png)

Se cargan ISBN repetidos.

![Imagen](assets/images/libro/carga05b.png)

Se soluciona en el modelo de libro agregando unique=True en isbn.

![Imagen](assets/images/libro/carga06.png)

Tambien se probó la carga de un ISBN negativo, lo cual probocaba la caida del servidor.
Se corrigió en el validators.py de libro agregando un mensaje de error si se ingresa
un numero negativo.
</details>

## Funcionalidad para visualizar el listado
Utilizacion del template listar.html usando una tabla. Se vizualizan los campos:
![Imagen](assets/images/libro/listar01.png)
Los botones Editar, Desactivar/Activar y Agregar Libro se encuentran presentes

## Funcionalidad para actualizar registros
Funcion del boton editar correcta despliega los datos correctos del campo elegido.
![Imagen](assets/images/libro/editar01.png)

Cambio de titulo de Caperucita a Caperucita Roja
![Imagen](assets/images/libro/editar02.png)
Cambios guardados exitosamente.

## Funcionalidad para desactivar registros
Listado sin desactivar.
![Imagen](assets/images/libro/listar01.png)

Desactivados: Caperucita Roja, Los 3 chanchitos y Pinocho.
![Imagen](assets/images/libro/inactivo01.png)
Funcionan correctamente los cambios de estado. 

## Registros en el Admin

![Imagen](assets/images/libro/admin01.png)
La base de datos se ve reflejada correctamente en el Admin.