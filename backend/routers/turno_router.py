from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload
from ..database.database import get_db
from ..crud.turno_cliente_crud import create_turno, get_turnos, get_turno_y_orden_por_DNI_cliente, update_turno, delete_turno, update_turno_estado, confirmar_llegada_turno, get_turnos_pendientes,get_dashboard_stats
from ..schemas.turno_schema import TurnoCreate, TurnoResponse, TurnoUpdate, OrdenResponse,DashboardStats
from database.models import Cliente, Turno
from typing import List

router = APIRouter(prefix="/api/turnos", tags=["turnos"])

        
@router.post("/CrearTurno")
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
        

@router.get("/obtenerTodoLosTurnos", response_model=list[TurnoResponse])
def obtenerTodosLosTurnos(db: Session = Depends(get_db)):
    return get_turnos(db)



@router.get("/pendientes", response_model=List[TurnoResponse])
def listar_turnos_pendientes(db: Session = Depends(get_db)):
    """
    Obtiene todos los turnos cuyo estado es "Pendiente".
    """
    turnos = get_turnos_pendientes(db)
    
    # Aquí es donde se debería convertir el DNI, etc. a str si es necesario
    
    return turnos



# ------------------------------------------------------------------------------



@router.get("/dashboard/stats", response_model=DashboardStats)
def obtener_estadisticas_dashboard(db: Session = Depends(get_db)):
    """
    Obtiene métricas clave para las tarjetas del dashboard (Citas Hoy, Vehículos en Taller, etc.).
    """
    # Llama a la función CRUD que realiza las consultas de conteo
    return get_dashboard_stats(db)







# ----------------------------------------------------------------------------------

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
def eliminar_turno_existente(turno_id: int, db: Session = Depends(get_db)):
    deleted = delete_turno(db, turno_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Turno no encontrado")
    return {"message": "Turno eliminado"}