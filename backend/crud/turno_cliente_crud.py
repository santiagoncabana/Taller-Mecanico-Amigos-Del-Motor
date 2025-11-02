from sqlalchemy.orm import Session
from sqlalchemy import and_
from ..database.models import Turno, Empleado
from ..schemas.turno_schema import TurnoCreate

def hay_espacio_disponible(db: Session, fecha: str, hora: str) -> bool:
    existing_turno = db.query(Turno).filter(and_(Turno.fecha == fecha, Turno.hora == hora)).first()
    return existing_turno is None

def conseguir_empleado_disponible(db: Session, fecha: str, hora: str) -> Empleado | None:
    empleados = db.query(Empleado).all()
    for emp in empleados:
        turno_asignado = db.query(Turno).filter(and_(
            Turno.empleado_id == emp.id,
            Turno.fecha == fecha,
            Turno.hora == hora
        )).first()
        if not turno_asignado:
            return emp
    return None

def create_turno(db: Session, turno: TurnoCreate) -> Turno:
    if not hay_espacio_disponible(db, turno.fecha, turno.hora):
        raise ValueError("Slot no disponible")
    
    emp = conseguir_empleado_disponible(db, turno.fecha, turno.hora)
    if not emp:
        raise ValueError("No hay empleados disponibles")
    
    new_turno = Turno(
        cliente_id=turno.cliente_id,
        empleado_id=emp.id,
        fecha=turno.fecha,
        hora=turno.hora,
        estado="pendiente"
    )
    db.add(new_turno)
    db.commit()
    db.refresh(new_turno)
    return new_turno

# Otras CRUD funciones
def get_turnos(db: Session):
    return db.query(Turno).all()

def get_turno_by_id(db: Session, turno_id: int):
    return db.query(Turno).filter(Turno.turno_id == turno_id).first()

def update_turno(db: Session, turno_id: int, updated_data: dict):
    db_turno = get_turno_by_id(db, turno_id)
    if not db_turno:
        return None
    for key, value in updated_data.items():
        setattr(db_turno, key, value)
    db.commit()
    db.refresh(db_turno)
    return db_turno

def delete_turno(db: Session, turno_id: int):
    db_turno = get_turno_by_id(db, turno_id)
    if not db_turno:
        return None
    db.delete(db_turno)
    db.commit()
    return db_turno