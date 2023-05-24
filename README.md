# ProyectoBiblioteca

Python - Django
Comisión 1. Squad 2. Bootcamp Alkemy

## Descripcion

La aplicación web esta diseñada usando Python y Django para dar
funcionalidades a una biblioteca, la cual permitirá a sus usuarios consultar el
catálogo de libros, y un listado de los préstamos de libros realizados a sus
socios. Cuenta con endpoint con devoluciones de datos en JSON

### Modulos

- autor
    - admin.py ( Administrador)
        - Agregado modelo al administrador utilizando list_display ( campos: nombre, apellido, nacionalidad y activo )
        - list_filter ( campos: activo y nacionalidad )
        - search_field ( campos: nombre y apellido )
    - models.py ( Ubicacion Principal del modelo autor )
        - nombre ( Nombre del Autor )
        - apellido ( Apellido del Autor)
        - nacionalidad ( Nacionalidad del Autor)
        - activo ( Por default se crea en True)
    - views.py ( Funcionalidades CRUD, activar o desactivar autor )
        - CrearAutor ( Utiliza su  - formulario ***forms.py*** para crear un Autor / uso Generic Views)
        - ListarAutores ( Funcion que utiliza un template para mostrar la lista / uso Generic Views )
        - EditarAutor ( Utiliza su formulario ***forms.py*** para editar un Autor / uso Generic Views )
        - activar_autor ( funcion que cambia Activo a True)
        - desactivar_autor ( funcion que cambia Activo a False)

- biblioteca
    - admin.py ( Administrador)
        - Agregado modelo al administrador utilizando list_display ( campos: fecha_prestamos, fecha_devolucion, socio, empleado y libro )
        - ordering ( fecha_devolucion )
        - search_field ( campos: socio, empleado y libro )
    - models.py ( Ubicacion Principal del modelo PrestamoLibro )
        - fecha_prestamos ( La fecha en la que se realizo el prestamo del libro )
        - fecha_devolucion ( Fechaen la que se devuelve el Libro)
        - socio ( La persona a la que se le presta el Libro / ForeignKey de modelo socio )
        - empleado ( La persona encargada del prestamo del libro / ForeignKey de modelo empleado)
        - libro ( Datos del libro Prestado / ForeignKey de modelo libro )
    - views.py ( )

- empleado
    - admin.py ( Administrador)
        - Agregado modelo al administrador utilizando list_display ( campos: apellido, nombre, numero_legajo y activo )
        - list_filter ( campos: activo )
        - search_field ( campos: nombre y apellido )
    - models.py ( Ubicacion Principal del modelo empleado )
        - nombre ( Nombre del Empleado )
        - apellido ( Apellido del Empleado )
        - numero_legajo ( Numero de legajo del empleado )
        - activo ( Por default se crea en True)
    - views.py ( Funcionalidades CRUD, activar o desactivar empleado )
        - CrearEmpleado ( Utiliza su  - formulario ***forms.py*** para crear un Empleado / uso Generic Views)
        - ListarEmpleados ( Funcion que utiliza un template para mostrar la lista / uso Generic Views )
        - EditarEmpleado ( Utiliza su formulario ***forms.py*** para editar un Empleado / uso Generic Views )
        - activar_empleado ( funcion que cambia Activo a True )
        - desactivar_empleado ( funcion que cambia Activo a False )
- libro
    - admin.py ( Administrador)
        - Agregado modelo al administrador utilizando list_display ( campos: titulo, descripcion, isbn, autor y activo )
        - list_filter ( campos: activo )
        - search_field ( campos: titulo )
    - models.py ( Ubicacion Principal del modelo libro )
        - titulo ( Titulo del Libro )
        - descripcion ( Descripcion del Libro, puede tener o No )
        - isbn ( El isbn es un estandard número de 13 cifras que identifica a cada libro )
        - autor ( La persona que escribio el libro / ForeignKey de modelo autor)
        - activo ( El libro esta disponible o no. Por default se crea en True)
    - views.py ()
- socio
    - admin.py ( Administrador)
        - Agregado modelo al administrador utilizando list_display ( campos: nombre, apellido, fecha_nacimiento y activo )
        - list_filter ( campos: activo )
        - search_field ( campos: nombre y apellido )
    - models.py ( Ubicacion Principal del modelo socio )
        - nombre ( Nombre del Socio )
        - apellido ( Apellido del Socio )
        - fecha_nacimiento ( Fecha de Nacimiento del Socio )
        - activo ( Si es un socio dado de alta o no. Por default se crea en True)
    - views.py ( Funcionalidades desactivar socio )
        - desactivar_socio ( funcion que cambia el campo Activo a False )
        
### Visual       
    Algunas Screenshots de nuestros templates Aqui
    - HOME
    - SOCIOS
    - PRESTAMO LIBRO
    - LISTADOS
    - ETC

### Instalacion

    REQUERIMIENTOS:
        - asgiref 3.6.0
        - Django 4.2.1
        - Jinja2 3.1.2
        - MarkupSafe 2.1.2
        - Pillow 9.5.0
        - sqlparse 0.4.4
        - tzdata 2023.3

### Autores y Colaboradores

    Joaquin Tejerina :+1:       [GitHub](https://github.com/JoaquinT04/).
    Ramiro Lopez                [GitHub](https://github.com/razier31/).
    Dante Alberto Martinez      [GitHub](https://github.com/errorcode106/).