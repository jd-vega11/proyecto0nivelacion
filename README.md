# Proyecto 0 API
#### Aplicación de eventos

Aplicación para soportar el manejo de eventos requerido por la empresa ABC. Un evento está compuesto de un nombre, una categoría (las cuatro posibles categorías son: Conferencia, Seminario, Congreso o Curso), un lugar, una dirección, una fecha de inicio y una fecha de fin, y si el evento es presencial o virtual (tipo).

## Descripción

En este repositorio se encuentra el API rest que soporta las operaciones básicas (CRUD) sobre los eventos, junto con el manejo de usuarios y autenticación a través de Token. Este back-end se realizó utilizando el Framework Django con una base de datos PostgresSQL y el front se realizó con React.

## Tabla de contenido

- [Pre-requisitos](#pre-requisitos)
- [Procedimiento](#procedimiento-backend)
- [Autenticación](#autenticación)
- [Peticiones](#peticiones)
- [Despliegue](#despliegue)
- [License](#license)

---

## Pre-requisitos

Para poder ejecutar este proyecto de forma local es necesario contar con lo siguiente:

- Python 3 o superior (con versión de pip compatible)
- Postgres DB v.10 o superior
- Virtualenv (puede instalarlo con `pip install virtualenv`)

## Procedimiento-backend

- Clonar el repositorio
- Ingresar al folder del repositorio `cd proyecto0nivelacion`
- Crear un ambiente virutal con el comando `virtualenv <nombre de su ambiente>`
- Activar el ambiente virtual (ir al directorio /bin dentro de la carpeta del ambiente virtual y ejecutar `source activate`)
- Actualizar pip (`python -m pip install --upgrade pip`)
- Instalar Django (`python -m pip install Django`)
- Instalar 
- En Postgres, crear la base de datos para soportar la persistencia y agregar un usuario con permisos sobre esa base de datos para que la aplicación pueda acceder a ella.
- Ingresar al archivo /proyecto0src/settings.py y agregar la configuración de su base de datos (en este repositorio se dejan credenciales de ejemplo):
```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<nombre de su base de datos>',
        'USER': '<usuario>',
        'PASSWORD':'<contraseña>',
        'HOST': '<dirección ip de la máquina donde tiene la base de datos>',
        'PORT':'<puerto de conexión a la base de datos>'
    }
}
```
- Nuevamente dentro de su ambiente virtual, instalar psycopg2 para comunicación Django - Postgress (`pip install psycopg2`)
- Ejecutar migraciones (`python manage.py migrate`)
- Desplegar el proyecto en un servidor. Aqui se incluye solamente el comando para el servidor de pruebas: `python3 manage.py runserver 0.0.0.0:8080`

## Autenticación

La autenticación se realiza a través de tokens que se expiden a nombre de los usuarios según petición al end-point `api/api-auth` (según la validez de estas credenciales dentro del sistema). Para todos los servicios asociados a la manipulación de eventos es necesario enviar el token correspondiente o de lo contrario no es posible procesar las solicitudes. Este token debe incluirse en el header de autorización como se indica en el siguiente ejemplo para obtener la lista de eventos de un usuario:

```
curl --location --request GET 'http://127.0.0.1:8080/api/events' \
--header 'Authorization: Token 00f7ca5ff75531dab094626d5f43bde1a6fd9d3f'

```

### Particularidades Postman

Es necesario agregar el header directamente con `key = Authorization y value = Token <token generado>`, no funciona usando la opción BearerToken desde la pestaña de Authorization.


## Peticiones

Para las peticiones que incluyen envío de datos, es necesario que estén en formato JSON en el cuerpo de la petición (no se aceptan cuerpos con form-data). Por ejemplo, para crear un evento:

```
curl --location --request POST 'http://127.0.0.1:8080/api/events' \
--header 'Authorization: Token 1974bcb27a76270b4819b19455d3e4480ab82eef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "event_name": "Sesion asincrona de Cualquier cosa", 
    "event_category": "CONFERENCE", 
    "event_place": "Conferencia Virtual en Sicuaplus", 
    "event_address": "https://sicuaplus.uniandes.edu.co/", 
    "event_initial_date": "2020-08-20T20:39:14Z", 
    "event_final_date": "2020-08-20T20:39:17Z", 
    "event_type": "VIRTUAL", 
    "thumbnail": "Banner del evento, seleccione un archivo PNG o JPG"    
}'
```
## Despliegue

El despliegue de la solución se realizó en la máquina virtual correspondiente con ip 172.24.98.186. El back-end se encuentra en el puerto 8081 y el front-end se encuentra en el puerto 8080. Es necesario contar con la configuración de proxy tanto en el navegador como en Postman (o similares) para poder acceder.

## Desarrollador

- Juan David Vega
 
---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2018 © 
