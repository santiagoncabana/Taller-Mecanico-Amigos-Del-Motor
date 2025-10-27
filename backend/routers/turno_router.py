from fastapi import APIRouter, Depends, HTTPException

from MecApp.backend.crud.turno_cliente_crud import crear_turno as crear_turno_db #cambie el nombre de la funcion porque se pisaba con la funcion del crud a la ahora de llamarlo
from MecApp.backend.schemas.turno_schema import TurnoCreate
from ..database.database import get_db, Session

router = APIRouter()
# turnos endpoints

@router.post("/turnos", tags=["turnos"])
def crear_turno_prueba(turno_datos: TurnoCreate, db: Session = Depends(get_db)): #cambie el nombre de la funcion porque se pisaba con la funcion del crud a la ahora de llamarlo
    nuevo_turno = crear_turno_db(db, turno_datos)
    
    if nuevo_turno is None:
        raise HTTPException(status_code=400, detail="Ya existe un turno para esa fecha y empleados.")
    return {"message": "Turno creado exitosamente", "turno_id": nuevo_turno.id}

@router.get("/ObtenerTurnos", tags=["Turnos1"])
def ListaTurnos():
    return[{"nombre": "Pedro"}, {"nombre": "Maxi"}]