# Crud Python+Postgres+Redis+Replit+Jwt

The project consists of a CRUD for person profiles, with user creation and login.

## Requirements

You must have the latest version of Docker Desktop installed and internet access, as the project uses images from Docker Hub.

## Installation

Navigate to the `app` folder of the project

```
fastapi_cache-main\app
```

Build the Docker image with the following command:

```
docker build .
```

Once the project images, the PostgreSQL database, and the Redis database are built, run the following command:

```
docker-compose up
```

When the following message appears:

```
Application startup complete.
```

You can open the FastAPI page at the following link
Endpoints for database

These endpoints must be executed at startup:

```
GET create_tables/
```

To create the tables

```
GET create_profile/{number}
```

To create profiles, where number is an integer referring to the number of profiles you want to create
Endpoints for CRUD

```
GET /api/users/profiles
```

To get all profiles

```
POST /api/users/profiles
```

To create profiles

```
GET /api/users/profiles/{profile_id}
```

To get a specific profile, where profile_id is the profile's ID

```
PUT /api/users/profiles/{profile_id}
```

To update a specific profile, where profile_id is the profile's ID

```
DELETE /api/users/profiles/{profile_id}
```

To delete a specific profile, where profile_id is the profile's ID
Other Endpoints

```
POST /signup
```

To register a user (email and password)

```
POST /login
```

To log in the user (email and password)

```
GET /who
```

## License
[MIT](https://choosealicense.com/licenses/mit/)

