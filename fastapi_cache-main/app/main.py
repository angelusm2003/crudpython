import os
from fastapi.security import OAuth2PasswordRequestForm
from api.router import router
from core.config import settings
from db.sessions import bulk_create_profiles, create_db_and_tables
from fastapi import FastAPI, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from schemas.user import UserOut, UserAuth, TokenSchema, SystemUser
from replit import db

from helpers.utils import (
    get_hashed_password,
    create_access_token,
    create_refresh_token,
    verify_password
)

from api.authori import get_current_user
from helpers import utils
from uuid import uuid4

app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    openapi_prefix=settings.openapi_prefix,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
)

app.include_router(router, prefix=settings.api_prefix)


@app.get("/")
async def root():
    return {"Say": "Bienvenido"}


@app.get("/create_tables")
async def create_tables():
    await create_db_and_tables()

    return {"Tablas creadas"}


@app.get("/create_profiles/{number}")
async def create_profiles(
        number: int,
):
    await bulk_create_profiles(number)

    return {"Perfiles Creados"}


@app.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # querying database to check if user already exist
    user = db.get(data.email, None)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )
    user = {
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
    }
    db[data.email] = user  # saving user to database
    return user


@app.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.get(form_data.username, None)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user['password']
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user['email']),
        "refresh_token": create_refresh_token(user['email']),
    }


@app.get('/who', summary='Get details of currently logged in user', response_model=UserOut)
async def get_me(user: SystemUser = Depends(get_current_user)):
    return user