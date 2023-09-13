# Crud Python+Postgres+Redis+Replit+Jwt

El proyecto consiste en un crud de perfiles de personas, con creacion y logueo de usuario

## Requisitos

Se debe tener instalada la ultima version de docker desktop y acceso a internet, ya que el proyecto ocupa imagenes del docker hub

## Instalacion

Posicionarse en la carpeta app del proyecto 

```bash
fastapi_cache-main\app
```

Generar la imagen de docker con el siguiente comando

```bash
docker build .
```
Una vez generada las imagenes del proyecto, la base de datos postgres, la base de datos redis, se ejecuta el siguiente comando:

```bash
docker-compose up
```
Cuando el aparezca el siguiente mensaje: 

```bash
Application startup complete.
```

Se puede cargar la pagina de Fastapi en el siguiente [link](http://localhost:8000/docs) 

## Endpoints para base de datos

Se debe ejecutar estos endpoints al iniciar:

```bash
GET create_tables/
```
Para la creacion de las tablas

```bash
GET create_profile/{number}
```
Para la creacion de perfiles , donde number es un entero y hace referencia al numero de perfiles que se desea crear

## Endpoints para crud

```bash
GET /api/users/profiles
```
Para obtener todos los perfiles

```bash
POST /api/users/profiles
```
Para la creacion de perfiles

```bash
GET /api/users/profiles/{profile_id}
```
Para obtener un perfil especifico, donde profile_id es el id del perfil

```bash
PUT /api/users/profiles/{profile_id}
```
Para la actualizacion de un perfil especifico, donde profile_id es el id del perfil

```bash
DELETE /api/users/profiles/{profile_id}
```
Para el borrado de un perfil especifico, donde profile_id es el id del perfil
## Otros Endpoints 
```bash
POST /signup
```
Para registrar usuario (correo y password)

```bash
POST /login
```
Para el logueo del usuario (correo y password)

```bash
GET /who
```
Para obtener informacion del usuario actual, este endpoint cuenta con autenticacion


## License

[MIT](https://choosealicense.com/licenses/mit/)
