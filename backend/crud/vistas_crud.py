from sqlalchemy.orm import Session, joinedload
from database.models import Cliente, Vehiculo
from ..crud.auth_cliente_crud import create_cliente

"""#Obtener todos los clientes registrados
def obtener_clientes(db:Session):
    return db.query(Cliente).all()

#Obtener cliente por DNI
def obtener_clientes_por_dni(db:Session,dni: str):
    return db.query(Cliente).filter(Cliente.DNI == dni).first()    #Cambie para que lo busque por DNI y no por id"""
    
def obtener_cliente_por_dni(db: Session, dni: str):
    cliente = (
        db.query(Cliente)
        .options(joinedload(Cliente.vehiculos))  # ← Cargar todos los vehículos
        .filter(Cliente.DNI == dni)
        .first()
    )
    
    if not cliente:
        raise ValueError(f"No se encontró cliente con DNI {dni}")
    
    return cliente


def obtener_todos_clientes(db: Session):
    clientes = (
        db.query(Cliente)
        .options(joinedload(Cliente.vehiculos))  #Cargar vehículos de todos
        .all()
    )
    
    return clientes


#Funciones de Vehiculos
def obtener_todos_los_vehiculos(db:Session):
    return db.query(Vehiculo).all()