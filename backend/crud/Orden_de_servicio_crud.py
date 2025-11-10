from database.models import OrdenDeServicio
from sqlalchemy.orm import Session
from schemas.turno_schema import orden_de_servicio_create
from database.models import Cliente, Turno


    
def create_orden(db: Session, orden: OrdenDeServicio):
    #Buscar el turno
    turno = db.query(Turno).filter(Turno.id == orden.turno_id).first()
    if not turno:
        raise ValueError("Turno no encontrado")
    
    #Buscar el cliente relacionado al turno
    cliente = db.query(Cliente).filter(Cliente.id == turno.cliente_id).first()
    if not cliente:
        raise ValueError("Cliente no encontrado")
    
    #Crear la orden con los datos autocompletados
    nueva_orden = OrdenDeServicio(
        turno_id=orden.turno_id,
        descripcion_trabajo=orden.descripcion_trabajo,
        precio_total=orden.precio_total,
        patente=orden.patente,
        modelo=orden.modelo,
        
        #AUTOCOMPLETAR DESDE CLIENTE Y TURNO
        nombre_cliente=cliente.nombre,
        telefono_cliente=turno.telefono,  
        dni_cliente=turno.DNI             
    )
    
    db.add(nueva_orden)
    db.commit()
    db.refresh(nueva_orden)
    return nueva_orden

def actualizar_turno_estado(db: Session, turno_id: int, nuevo_estado: str):
    turno = db.query(Turno).filter(Turno.id == turno_id).first()
    
    if not turno:
        raise ValueError("Turno no encontrado")
    
    #Validaciones de negocio
    estados_validos = ["Pendiente", "Finalizado"]
    if nuevo_estado not in estados_validos:
        raise ValueError(f"Estado inválido. Use: {estados_validos}")
    
    #No permitir cambiar si ya está completado
    if turno.estado == "Finalizado":
        raise ValueError("No se puede modificar un turno Finalizado")
    
    #Actualizar
    turno.estado = nuevo_estado
    db.commit()
    db.refresh(turno)
    return turno