import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from .routers import clienteAuth_router 
from .routers import turno_router
from .database.database import create_db_tables
from .database.database import engine, Base #para probar la vista encargado
from MecApp.backend.routers import vistaEncargado_router #para probar la vista encargado

create_db_tables()

app = FastAPI()


#origins = [
   #"http://127.0.0.1:5500", 
    #"http://localhost:5500",
#]
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://127.0.0.1:8000",  # ← AGREGAR
    "http://localhost:8000",   # ← AGREGAR
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,             # Lista de URLs permitidas
    allow_credentials=True,            # Permite cookies y encabezados de autorización
    allow_methods=["*"],               # Permite todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],               # Permite todos los encabezados
)

app.include_router(clienteAuth_router.router)
app.include_router(turno_router.router)

app.include_router(vistaEncargado_router.router)
Base.metadata.create_all(bind=engine)