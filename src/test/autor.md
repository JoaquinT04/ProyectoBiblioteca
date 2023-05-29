# Test Modulo Autor
Fecha 28/05/23
## Funcionalidad para agregar nuevos registros
 

Por ahora se puede cargar nombres,apellidos y nacionalidad que no tengan ni numeros, caracteres especiales o tildes con un minimo de caracteres de 5 y un maximo de 50, por defecto cada autor
va a tener el atributo activado en **True**

## Funcionalidad para visualizar el listado
El listado muestra 6 columnas que son:
> - nombre: muestra el nombre del autor
> - apellido: muestra el apellido del autor
> - nacionalidad: muestra la nacionalidad del autor
> - estado: muestra el estado de actividad del autor
> - modificar estado: muestra un boton para desactivar/activar el estado del autor
> - modificar el autor: muestra un boton que te lleva a la funcionalidad de editar el autor
## Funcionalidad para actualizar registros
A la hora de actualizar solo se puede modificar el nombre, el apellido y la nacionalidad, pero el
atributo activo no se puede modificar en esta funcinalidad ya que se puede modificar en el listado

## Funcionalidad para desactivar registros
Es un boton que me permite cambiar el atributo activo del autor a True si es False y viceversa

## Registros en el Admin y/o en el DB Browser
### Listado
En el admin tanto como en el db Browser los registros se muestran en una tabla con las siguientes 
columnas:

> - nombre: muestra el nombre del autor
> - apellido: muestra el apellido del autor
> - nacionalidad: muestra la nacionalidad del autor
> - activo: muestra el estado de actividad del autor

este ultimo aparece con un check por defecto ya que es True, pero desde
el admin se puede modificar esta opción a la hora de crear un nuevo autor
### Crear
Ene el admin se puede crear un autor agregando valores al nombre, apellido, nacionalidad y activo(check)

### Modificar
En el admin podemos modificar los atributod de nombre, apellido, nacionalidad y activo
En el DB Browser se puede modificar pero no tiene ningun tipo de control

