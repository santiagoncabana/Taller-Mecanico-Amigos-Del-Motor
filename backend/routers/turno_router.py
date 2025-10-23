from fastapi import APIRouter, Depends, HTTPException

from MecApp.backend.crud.turno_cliente_crud import crear_turno
from MecApp.backend.schemas.turno_schema import TurnoCreate
from ..database.database import get_db, Session

router = APIRouter()
# turnos endpoints

@router.post("/turnos", tags=["turnos"])
def crear_turno(turno_datos: TurnoCreate, db: Session = Depends(get_db)):
    nuevo_turno = crear_turno(db, turno_datos)
    
    if nuevo_turno is None:
        raise HTTPException(status_code=400, detail="Ya existe un turno para esa fecha y empleados.")
    return {"message": "Turno creado exitosamente", "turno_id": nuevo_turno.id}