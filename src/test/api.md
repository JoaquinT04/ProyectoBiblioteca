# Test Modulo API
Fecha 4/06/23
## Funcionalidad de endpoints del módulo de libros

url: /api/libros/id

devolvera un json con la siguiente informaión de libro si el id es valido :
> - id: primary key del libro
> - titulo 
> - descripcion 
> - autor

```
{
  "id": 1,
  "titulo": "titulo del libro",
  "descripcion": "descripcion del libro",
  "autor": "autor del libro"
}

```

de lo contrario enviara un json vacio
```
{
	
}

```