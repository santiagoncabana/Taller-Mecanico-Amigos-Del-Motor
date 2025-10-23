from fastapi import FastAPI
from .routers import clienteAuth_router
from .database.database import create_db_tables

create_db_tables()

app = FastAPI()

app.include_router(clienteAuth_router.router)
