from MecApp.backend.database.models import Turno
from ..database.database import get_db, Session
from schemas.turno_schema import TurnoCreate


def crear_turno(db: Session, turno_datos: TurnoCreate):

    turno_existente = db.query(Turno).filter(
        Turno.fecha == turno_datos.fecha,
        #Turno.empleado_id == turno_datos.empleado_id
    ).first()

    if turno_existente:
        
        return None
    else:
        turno_prueba = Turno(
            telefono= turno_datos.telefono, 
            cuit= turno_datos.cuit, 
            patente= turno_datos.patente, 
            modelo= turno_datos.modelo, 
            fecha= turno_datos.fecha, 
            hora_inicio= turno_datos.hora_inicio
        )
        db.add(turno_prueba)
        db.commit()
        db.refresh(turno_prueba)
        return turno_prueba



