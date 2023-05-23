# ProyectoBiblioteca

Python - Django
Comisión 1. Squad 2. Bootcamp Alkemy

## Descripcion

La aplicación web esta diseñada usando Python y Django para dar
funcionalidades a una biblioteca, la cual permitirá a sus usuarios consultar el
catálogo de libros, y un listado de los préstamos de libros realizados a sus
socios. Cuenta con endpoint con devoluciones de datos en JSON

### Modulos

*autor
    *models.py ( Ubicacion Principal del modelo autor )
        *nombre ( Nombre del Autor )
        *apellido ( Apellido del Autor)
        *nacionalidad ( Nacionalidad del Autor)
        *activo ( Por default se crea en True)
    *views,py ( Funcionalidades CRUD, activar o desactivar autor )
        *CrearAutor ( Utiliza su formulario ***forms.py*** para crear un Autor / uso Generic Views)
        *ListarAutores ( Funcion que utiliza un template para mostrar la lista / uso Generic Views )
        *EditarAutor ( Utiliza su formulario ***forms.py*** para editar un Autor / uso Generic Views )
        *activar_autor ( funcion que cambia Activo a True)
        *desactivar_autor ( funcion que cambia Activo a False)

*biblioteca
    *models.py ( Ubicacion Principal del modelo PrestamoLibro )
        *fecha_prestamos ( La fecha en la que se realizo el prestamo del libro )
        *fecha_devolucion ( Fechaen la que se devuelve el Libro)
        *socio ( La persona a la que se le presta el Libro / ForeignKey de modelo socio )
        *empleado ( La persona encargada del prestamo del libro / ForeignKey de modelo empleado)
        *libro ( Datos del libro Prestado / ForeignKey de modelo libro )
    *views,py ( )
        *
        *