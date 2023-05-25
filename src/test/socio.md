# Test Modulo Socio
Fecha 25/05/23
## Funcionalidad para agregar nuevos registros
 
Formulario de carga con Campos (nombre, apellido fecha de nacimiento):
<details><summary>Primera Carga</summary>

![Imagen](assets/images/socio/primeracarga.png)

Carga Exitosa   

</details>

<details><summary>Segunda Carga</summary>

![Imagen](assets/images/socio/segundacargaerr.png)

Carga Fallida se muestra el error

 reintentando...  

 ![Imagen](assets/images/socio/segundacarga.png)  
 carga exitosa funcionalidad de Validador solo texto comprobada!

</details>

<details><summary>Tercer Carga</summary>

![Imagen](assets/images/socio/tercercargaerr.png)

Carga Fallida se muestra el error

 reintentando...  

 ![Imagen](assets/images/socio/tercercarga.png)  
 carga exitosa funcionalidad de Validador min length comprobada!

</details>

<details><summary>Cuarta Carga</summary>

![Imagen](assets/images/socio/cuartacargaerr.png)

Carga Fallida se muestra el error

![Imagen](assets/images/socio/cuartacarga.png)

Carga exitosa probado el campo fecha   

</details>

## Funcionalidad para visualizar el listado
Utilizacion de Template listar.html usando una tabla se vizualizan los campos:
![Imagen](assets/images/socio/listado.png)
Botones Editar, Desactivar y Agregar Socio Presentes

## Funcionalidad para actualizar registros
Funcion del boton editar correcta despliega los datos correctos del campo elegido
![Imagen](assets/images/socio/actualizar.png)
cambio de nombre de Antonio a Pedro
![Imagen](assets/images/socio/modificado.png)
Guardado Exitoso
## Funcionalidad para desactivar registros
Listado sin desactivar
![Imagen](assets/images/socio/listadod.png)
desactivando Banderas y Ortega...
![Imagen](assets/images/socio/listadod2.png)
Funcionalidad Exitosa se muestra correctamente los cambios de estado 

## Registros en el Admin y/o en el DB Browser
**Admin**
![Imagen](assets/images/socio/admin.png)
base de datos reflejada correctamente en el Admin
**DB Browser**
![Imagen](assets/images/socio/dbbrow.png)
Confirmacion de base de Datos usando el Db Browser

