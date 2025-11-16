from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from ..database.database import get_db
from ..crud.turno_cliente_crud import create_turno, get_turnos, get_turno_y_orden_por_DNI_cliente, update_turno, delete_turno, update_turno_estado, confirmar_llegada_turno
from ..schemas.turno_schema import TurnoCreate, TurnoResponse, TurnoUpdate, OrdenResponse
from database.models import Cliente, Turno
from typing import List

router = APIRouter(prefix="/api/turnos", tags=["turnos"])

        
@router.post("/")
def crear_nuevo_turno(turno: TurnoCreate, db: Session = Depends(get_db)):
    try:
        nuevo_turno = create_turno(db, turno)
        return {
            "mensaje": "Turno creado exitosamente",
            "turno_id": nuevo_turno.id,
            "cliente_id": nuevo_turno.cliente_id,
            "empleado_id": nuevo_turno.empleado_id,
            "fecha": nuevo_turno.fecha,
            "hora": nuevo_turno.hora,
            "Estado:": "Pendiente"
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/turnos/{turno_id}/confirmar-llegada")
def confirmar_llegada_cliente(turno_id: int, db: Session = Depends(get_db)):
    try:
        turno = confirmar_llegada_turno(db, turno_id)
        return {
            "mensaje": "Cliente confirmado en taller",
            "turno_id": turno.id,
            "estado": turno.estado
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
        

@router.get("/", response_model=list[TurnoResponse])
def obtenerTodosLosTurnos(db: Session = Depends(get_db)):
    return get_turnos(db)

"""@router.get("/{turno_DNI}", response_model=list[TurnoResponse, OrdenResponse])
def obtener_turno(turno_DNI: str, turno_id: int, db: Session = Depends(get_db)):
    turno = get_turno_y_orden_por_DNI_cliente(db, turno_DNI, turno_id)
    if not turno:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return turno"""
    
@router.get("/turnos/buscar/{dni}/todos", response_model=List[TurnoResponse])
def buscar_todos_turnos_por_dni(dni: str, db: Session = Depends(get_db)):
    turnos = (
        db.query(Turno)
        .options(joinedload(Turno.orden_servicio))
        .filter(Turno.DNI == dni)
        .all()
    )
    
    if not turnos:
        raise HTTPException(404, f"No se encontraron turnos para el DNI {dni}")
    
    return turnos

@router.put("/{turno_DNI}", response_model=TurnoResponse)
def actualizar_turno_existente(turno_DNI: str, turno: TurnoCreate, db: Session = Depends(get_db)):
    updated = update_turno(db, turno_DNI, turno.dict(exclude={"cliente_id"}))  # No cambiar cliente_id
    if not updated:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return updated

@router.delete("/{turno_id}")
def eliminar_turno_existente(turno_DNI: str, db: Session = Depends(get_db)):
    deleted = delete_turno(db, turno_DNI)
    if not deleted:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return {"message": "Turno eliminado"}
