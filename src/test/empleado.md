# Test Modulo Empleado
Fecha 28/05/23

## Funcionalidad para agregar nuevos registros
 
Formulario de carga con Campos (nombre, apellido y numero de legajo):
<details><summary>Primera Carga</summary>

![Imagen](assets/images/empleado/carga_exitosa.jpg)

Carga Exitosa. 
Luego se realizaron 3 cargas mas con exito.

Carlos Alberto Belgrano   Legajo: 874
Juan Pablo Campos Villa   Legajo: 1174
Federico Saravia Mir   Legajo: 124

</details>

<details><summary>Segunda Carga</summary>

![Imagen](assets/images/empleado/carga02.jpg)
Carga Fallida. Se muestra error en Nombre.

![Imagen](assets/images/empleado/carga03.jpg)
En el campo Apellido solo se permiten hasta 30 caracteres. Idem para Nombre.

 Se corrige.  
  
 Carga exitosa.

</details>

<details><summary>Tercer Carga</summary>

![Imagen](assets/images/empleado/carga04.jpg)
Carga Fallida. Se guardan numeros o caracteres especiales en Nombre y Apellido


 ![Imagen](assets/images/empleado/carga05.jpg)  
 Se soluciona con el Validador RegexValidator!

 ![Imagen](assets/images/empleado/carga06.jpg)

</details>

<details><summary>Cuarta Carga</summary>

![Imagen](assets/images/empleado/carga07.jpg)
Carga Fallida. Se muestra el error en numero de legajo.

Carga exitosa cargando numeros positivos.

ACLARACION: En este campo se podria colocar un validador para acortar rango de legajo.

</details>

<details><summary>Quinta Carga</summary>

![Imagen](assets/images/empleado/carga08.jpg)
Se cargan legajos repetidos.

![Imagen](assets/images/empleado/carga09.jpg)

Se soluciona en el modelo de empleado agregando unique=True.

![Imagen](assets/images/empleado/carga10.jpg)

ACLARACION: Se puede cargar el legajo 0 pero se puede corregir desactivandolo.

</details>

## Funcionalidad para visualizar el listado
Utilizacion del template listar.html usando una tabla. Se vizualizan los campos:
![Imagen](assets/images/empleado/listar01.jpg)
Los botones Editar, Desactivar y Agregar Empleado se encuentran presentes

MODIFICACIONES: Se modifica template para una mejor vizualizacion. La 1ra columna muestra ahora apellido.  
![Imagen](assets/images/empleado/listar02.jpg)

Tambien se modifica la views y ordena por apellido y el campo activo. 
![Imagen](assets/images/empleado/listar03.jpg)

## Funcionalidad para actualizar registros
Funcion del boton editar correcta despliega los datos correctos del campo elegido.
![Imagen](assets/images/empleado/editar01.jpg)

Cambio de nombre de Sergio a Sebastian
![Imagen](assets/images/empleado/editar02.jpg)
Cambios guardados exitosamente.

## Funcionalidad para desactivar registros
Listado sin desactivar.
![Imagen](assets/images/empleado/activo01.jpg)

Desactivados: Romero y Belgrano.
![Imagen](assets/images/empleado/activo02.jpg)
Funcionan correctamente los cambios de estado. 

## Registros en el Admin y/o en el DB Browser
**Admin**
![Imagen](assets/images/empleado/admin01.jpg)
La base de datos se ve reflejada correctamente en el Admin.

**DB Browser**
![Imagen](assets/images/empleado/bdatos01.jpg)
Confirmacion de base de Datos usando el Db Browser