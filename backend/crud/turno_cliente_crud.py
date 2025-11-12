from sqlalchemy.orm import Session
from sqlalchemy import and_
from ..database.models import Turno, Empleado
from ..schemas.turno_schema import TurnoCreate
from sqlalchemy import func


def hay_espacio_disponible(db: Session, fecha: str, hora: str):
    existing_turno = db.query(Turno).filter(and_(Turno.fecha == fecha, Turno.hora == hora)).first()
    return existing_turno is None

from sqlalchemy import func
from sqlalchemy.orm import Session
from MecApp.backend.database.models import Turno, Empleado, Cliente
from MecApp.backend.schemas.turno_schema import TurnoCreate

def conseguir_empleado_disponible(db: Session, fecha: str, hora: str) -> Empleado | None:
    # Subconsulta: IDs de empleados que ya tienen turno en esa fecha y hora
    empleados_ocupados = (
        db.query(Turno.empleado_id)
        .filter(Turno.fecha == fecha, Turno.hora == hora)
        .subquery()
    )

    # Consulta directa: empleados disponibles y no ocupados, orden aleatorio
    empleado = (
        db.query(Empleado)
        .filter(
            Empleado.disponible == True,
            ~Empleado.id.in_(empleados_ocupados)
        )
        .order_by(func.random())
        .first()
    )

    return empleado

def create_turno(db: Session, turno: TurnoCreate):
    #Buscar cliente por DNI
    cliente = db.query(Cliente).filter(Cliente.DNI == turno.DNI).first()
    if not cliente:
        raise ValueError("Cliente no encontrado con ese DNI")
    
    if turno.telefono:
        cliente.telefono = turno.telefono #Actualiza la tabla de cliente cuando se crea el turno, ya que en solo ahi pedimos numero y en la tabla de clientes queda null siempre.
    
    #Buscar empleado disponible
    emp = conseguir_empleado_disponible(db, turno.fecha, turno.hora)
    if not emp:
        raise ValueError("No hay empleados disponibles")
    
    #Crear turno con cliente_id y empleado_id
    new_turno = Turno(
        cliente_id=cliente.id,      #RELACIONADO CON CLIENTE
        empleado_id=emp.id,          #RELACIONADO CON EMPLEADO
        telefono=turno.telefono,
        DNI=turno.DNI,
        fecha=turno.fecha,
        hora=turno.hora,
        estado="pendiente"
    )
    db.add(new_turno)
    db.commit()
    db.refresh(new_turno)
    return new_turno

def update_turno_estado(db: Session, turno_id: int, nuevo_estado: str):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    
    if turno:
        turno.estado = nuevo_estado
        db.commit()
        db.refresh(turno)
        return turno
    return None


#Otras CRUD funciones
def get_turnos(db: Session):
    return db.query(Turno).all()

def get_turno_by_id(db: Session, turno_id: int):
    return db.query(Turno).filter(Turno.id == turno_id).first()

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