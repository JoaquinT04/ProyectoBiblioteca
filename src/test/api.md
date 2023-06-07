# Test Modulo API
Fecha 4/06/23
## Funcionalidad de endpoints del módulo de libros

url: api/libro/id/

Este endpoint devolvera un json con la siguiente información de libro si el id es valido :
> - id: primary key del libro
> - titulo 
> - descripcion 
> - autor

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
    }
}

```

de lo contrario enviara un json vacio
```
{
    "detail": "No encontrado."
}

```

url: /api/libro/
Este endpoint devolvera una lista de json's y cada json tendra la siguiente información de libro si el id es valido :
> - id: primary key del libro
> - titulo 
> - descripcion 
> - autor
