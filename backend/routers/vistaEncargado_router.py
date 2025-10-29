from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..crud.vistas_crud import todos_los_clientes
from ..schemas.cliente_schemas import ClienteOut
from ..database.database import get_db

router = APIRouter(tags=["Encargado"])

@router.get ("/Clientes", response_model=List[ClienteOut])
def ver_clientes(db:Session = Depends(get_db)):
    vista = todos_los_clientes(db)
    return vista