# Crud Python+Postgres+Redis+Replit+Jwt

The project consists of a CRUD for person profiles, with user creation and login.

## Requirements

You must have the latest version of Docker Desktop installed and internet access, as the project uses images from Docker Hub.

## Installation

Navigate to the `app` folder of the project

```bash
fastapi_cache-main\app

Build the Docker image with the following command:

```bash
docker build .

Once the project images, the PostgreSQL database, and the Redis database are built, run the following command:

```bash
docker-compose up

When the following message appears:

```bash
Application startup complete.

You can open the FastAPI page at the following link
Endpoints for database

These endpoints must be executed at startup:

```bash
GET create_tables/

To create the tables

```bash
GET create_profile/{number}

To create profiles, where number is an integer referring to the number of profiles you want to create
Endpoints for CRUD

```bash
GET /api/users/profiles

To get all profiles

```bash
POST /api/users/profiles

To create profiles

```bash
GET /api/users/profiles/{profile_id}

To get a specific profile, where profile_id is the profile's ID

```bash
PUT /api/users/profiles/{profile_id}

To update a specific profile, where profile_id is the profile's ID

```bash
DELETE /api/users/profiles/{profile_id}

To delete a specific profile, where profile_id is the profile's ID
Other Endpoints

```bash
POST /signup

To register a user (email and password)

```bash
POST /login

To log in the user (email and password)

```bash
GET /who

## License
[MIT](https://choosealicense.com/licenses/mit/)

