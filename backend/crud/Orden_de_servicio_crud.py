from database.models import OrdenDeServicio
from sqlalchemy.orm import Session
from schemas.turno_schema import orden_de_servicio_create
from database.models import Cliente, Turno

"""def create_orden_de_servicio(db: Session, orden: orden_de_servicio_create):
    nueva_orden = OrdenDeServicio(
        descripcion_trabajo=orden.descripcion_trabajo,
        precio_total=orden.precio_total,
        turno_id=orden.turno_id,
        patente=orden.patente,
        modelo=orden.modelo,
    )
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden"""
    
    
def create_orden(db: Session, orden: OrdenDeServicio):
    # 1. Buscar el turno
    turno = db.query(Turno).filter(Turno.id == orden.turno_id).first()
    if not turno:
        raise ValueError("Turno no encontrado")
    
    # 2. Buscar el cliente relacionado al turno
    cliente = db.query(Cliente).filter(Cliente.id == turno.cliente_id).first()
    if not cliente:
        raise ValueError("Cliente no encontrado")
    
    # 3. Crear la orden con los datos autocompletados
    nueva_orden = OrdenDeServicio(
        turno_id=orden.turno_id,
        descripcion_trabajo=orden.descripcion_trabajo,
        precio_total=orden.precio_total,
        patente=orden.patente,
        modelo=orden.modelo,
        
        # ← AUTOCOMPLETAR DESDE CLIENTE Y TURNO
        nombre_cliente=cliente.nombre,
        telefono_cliente=turno.telefono,  # Del turno
        dni_cliente=turno.DNI             # Del turno
    )
    
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden