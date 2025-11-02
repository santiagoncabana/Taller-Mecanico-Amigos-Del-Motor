from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..crud.vistas_crud import obtener_clientes
from ..schemas.cliente_schemas import ClienteOut
from ..database.database import get_db


router = APIRouter(prefix="/api/clientes", tags=["clientes"])

@router.get("/", response_model=list[ClienteOut])
def obtener_todos_los_clientes(db: Session = Depends(get_db)):
    return obtener_clientes(db)