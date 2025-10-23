from MecApp.backend.database.models import Turno
from ..database.database import get_db, Session
from schemas.turno_schema import TurnoCreate


def crear_turno(db: Session, turno_datos: TurnoCreate):

    turno_existente = db.query(Turno).filter(
        Turno.fecha == turno_datos.fecha and
        Turno.empleado_id == turno_datos.empleado_id
    ).first()

    if turno_existente:
        return None 



