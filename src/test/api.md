# Test Modulo API
Fecha 4/06/23
# Funcionalidad de endpoints de los módulos:
### Libro
<details><summary>Enpoint detalle libro</summary>

## url: api/libro/id/

Este endpoint devolvera un json con la siguiente información de libro si el id es valido :
> - id: primary key del libro
> - titulo 
> - descripcion 
> - autor
> - activo: valor booleano para ver si el libro esta activo o no

```
{
    "id": 1,
    "titulo": "Holaa",
    "descripcion": "asdasdqweqwe qweqwe   qwe wq e q wew q",
    "isbn": 1234567891245,
    "autor": {
        "id": 5,
        "nombre": "Juan Alberto",
        "apellido": "Gomez",
        "nacionalidad": "Venezolano"
    },
    "activo": True
}

```

Si el id no es valido se enviara un json de la siguiente forma:
```

{
    "detail": "No encontrado."
}

```
</details>


<details><summary>Enpoint listar libros</summary>

## url: /api/libro/
Este endpoint devolvera una lista de libros en formato json:
```
[
    {
        "id": 1,
        "titulo": "Holaa",
        "descripcion": "asdasdqweqwe qweqwe   qwe wq e q wew q",
        "isbn": 1234567891245,
        "autor": {
            "id": 5,
            "nombre": "Juan Alberto",
            "apellido": "Gomez",
            "nacionalidad": "Venezolano",
            "activo": true
        },
        "activo": true
    },
    {
        "id": 3,
        "titulo": "Holaaa la venganza",
        "descripcion": "askndoqwmeomq",
        "isbn": 1234512345234,
        "autor": {
            "id": 2,
            "nombre": "Juan",
            "apellido": "Hernandez",
            "nacionalidad": "Mexicano",
            "activo": true
        },
        "activo": true
    },
    {
        "id": 2,
        "titulo": "Nuevo libro",
        "descripcion": "asoidnoqiwneoqn",
        "isbn": 1283940239483,
        "autor": {
            "id": 2,
            "nombre": "Juan",
            "apellido": "Hernandez",
            "nacionalidad": "Mexicano",
            "activo": true
        },
        "activo": true
    }
]
```

Si la lista esta vacia se devolvera lo siguiente:
```

[]

```
</details>

### Empleado
<details><summary>Endpoint detalle empleado</summary>

## url: /api/empleado/id

Este endpoint devolvera un json con la siguiente información de empleados si el id es valido :
> - id: primary key del empleado
> - nombre 
> - apellido 
> - numero de legajo
> - activo: valor booleano para ver si el empleado esta activo o no

```
{
    "id": 3,
    "nombre": "Pablo",
    "apellido": "Alvarez",
    "numero_legajo": 123123,
    "activo": True
}
```
Si el id no es valido se enviara un json de la siguiente forma:
```

{
    "detail": "No encontrado."
}

```
</details>

<details><summary>Enpoint listar empleados</summary>

## url: /api/empleado/

Este endpoint devolvera una lista de empleados en formato jsno

```
[
    {
        "id": 3,
        "nombre": "Pablo",
        "apellido": "Alvarez",
        "numero_legajo": 123123,
        "activo": True
    },
    {
        "id": 2,
        "nombre": "Jose",
        "apellido": "Hernandez",
        "numero_legajo": 513412983,
        "activo": True
    },
    {
        "id": 1,
        "nombre": "Pepe",
        "apellido": "Tejerina",
        "numero_legajo": 1231412,
        "activo": True
    }
]
```

Si la lista esta vacia se devolvera lo siguiente:
```

[]

```
</details>

### Autor
<details><summary>Endpoint detalle autor</summary>

## url: /api/autor/id

Este endpoint devolvera un json con la siguiente información del autor si el id es valido :
> - id: primary key del autor
> - nombre 
> - apellido 
> - nacionalidad
> - activo: valor booleano para ver si el autor esta activo o no

```
{
        "id": 5,
        "nombre": "Juan Alberto",
        "apellido": "Gomez",
        "nacionalidad": "Venezolano",
        "activo": true
}
```

Si el id no es valido se enviara un json de la siguiente forma:
```

{
    "detail": "No encontrado."
}

```
</details>

<details><summary>Enpoint listar autores</summary>

## url: /api/autor/

Este endpoint devolvera una lista de autores en formato jsno

```
[
    {
        "id": 1,
        "nombre": "Gonzalo",
        "apellido": "Hernandez",
        "nacionalidad": "Argentino",
        "activo": true
    },
    {
        "id": 2,
        "nombre": "Juan",
        "apellido": "Hernandez",
        "nacionalidad": "Mexicano",
        "activo": true
    },
    {
        "id": 4,
        "nombre": "Jose Martin asda",
        "apellido": "Mendez",
        "nacionalidad": "Paraguayo",
        "activo": true
    },
    {
        "id": 3,
        "nombre": "Joaquin",
        "apellido": "Tejerina",
        "nacionalidad": "Argentino",
        "activo": true
    }
]

```
Si la lista esta vacia se :
```
[]

```
</details>

### socio
<details><summary>Endpoint detalle socio</summary>

## url: /api/socio/id

Este endpoint devolvera un json con la siguiente información de empleados si el id es valido :
> - id: primary key del socio
> - nombre 
> - apellido 
> - fecha nacimiento
> - activo: valor booleano para ver si el socio esta activo o no

```
{
    "id": 2,
    "apellido": "Gomez",
    "nombre": "Joaquin",
    "fecha_nacimiento": "1999-10-04",
    "activo": true
}
```

Si el id no es valido se enviara un json de la siguiente forma:
```

{
    "detail": "No encontrado."
}

```
</details>

<details><summary>Enpoint listar socios</summary>

## url: /api/socio/

Este endpoint devolvera una lista de socios en formato jsno

```
[
    {
        "id": 2,
        "apellido": "Gomez",
        "nombre": "Joaquin",
        "fecha_nacimiento": "1999-10-04",
        "activo": true
    },
    {
        "id": 3,
        "apellido": "Perez",
        "nombre": "Julio",
        "fecha_nacimiento": "1834-02-28",
        "activo": true
    },
    {
        "id": 1,
        "apellido": "Tejerina",
        "nombre": "Jorge",
        "fecha_nacimiento": "2010-05-10",
        "activo": true
    }
]
```

Si la lista esta vacia se devolvera lo siguiente:
```

[]

```
</details>
