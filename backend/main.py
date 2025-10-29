import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI
from .routers import clienteAuth_router 
from .routers import turno_router
from .database.database import create_db_tables
from .database.database import engine, Base #para probar la vista encargado
from MecApp.backend.routers import vistaEncargado_router #para probar la vista encargado

create_db_tables()

app = FastAPI()

app.include_router(clienteAuth_router.router)
app.include_router(turno_router.router)

app.include_router(vistaEncargado_router.router)
Base.metadata.create_all(bind=engine)