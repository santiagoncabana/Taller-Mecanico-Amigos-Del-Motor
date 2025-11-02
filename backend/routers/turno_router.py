from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database.database import get_db
from ..crud.turno_cliente_crud import create_turno, get_turnos, get_turno_by_id, update_turno, delete_turno
from ..schemas.turno_schema import TurnoCreate, TurnoResponse

router = APIRouter(prefix="/api/turnos", tags=["turnos"])

@router.post("/", response_model=TurnoResponse)
def crear_nuevo_turno(turno: TurnoCreate, db: Session = Depends(get_db)):
    try:
        return create_turno(db, turno)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[TurnoResponse])
def obtenerTodosLosTurnos(db: Session = Depends(get_db)):
    return get_turnos(db)

@router.get("/{turno_id}", response_model=TurnoResponse)
def obtener_turno(turno_id: int, db: Session = Depends(get_db)):
    turno = get_turno_by_id(db, turno_id)
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno

@router.put("/{turno_id}", response_model=TurnoResponse)
def actualizar_turno_existente(turno_id: int, turno: TurnoCreate, db: Session = Depends(get_db)):
    updated = update_turno(db, turno_id, turno.dict(exclude={"cliente_id"}))  # No cambiar cliente_id
    if not updated:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return updated

@router.delete("/{turno_id}")
def eliminar_turno_existente(turno_id: int, db: Session = Depends(get_db)):
    deleted = delete_turno(db, turno_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return {"message": "Turno eliminado"}