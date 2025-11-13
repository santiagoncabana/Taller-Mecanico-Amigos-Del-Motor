from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from ..crud.vistas_crud import obtener_clientes, obtener_clientes_por_dni
from ..schemas.cliente_schemas import ClienteOut
from ..database.database import get_db
from fastapi import HTTPException


router = APIRouter(prefix="/api/clientes", tags=["clientes"])

@router.get("/", response_model=list[ClienteOut])
def obtener_todos_los_clientes(db: Session = Depends(get_db)):
    return obtener_clientes(db)

@router.get("/dni/{dni}")
def obtener_cliente_por_dni(dni: str, db: Session = Depends(get_db)):
    cliente = obtener_clientes_por_dni(db, dni)
    
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    
    #Ingresar respuesta manualmente si no pediria todo lo del ClientOut y que no queremos que el empleado ingrese el numero de telefono cuando lo busca por el DNI
    response = {
        "id": cliente.id,
        "nombre": cliente.nombre,
        "email": cliente.email,
        "contrasena": cliente.contrasena,
        "DNI": cliente.DNI,
        "telefono": cliente.telefono
    }
    
    #Agregar mensaje si no tiene teléfono
    if not cliente.telefono:
        response["advertencia"] = "Este cliente aún no registró su número de teléfono"
    return response

