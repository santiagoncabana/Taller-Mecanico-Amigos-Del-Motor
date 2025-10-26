import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from .routers import clienteAuth_router 
from .routers import turno_router
from .database.database import create_db_tables

create_db_tables()

app = FastAPI()

app.include_router(clienteAuth_router.router)
app.include_router(turno_router.router)