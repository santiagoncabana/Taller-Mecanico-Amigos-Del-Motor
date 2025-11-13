from sqlalchemy.orm import Session
from database.models import Cliente, Vehiculo
from ..crud.auth_cliente_crud import create_cliente

#Obtener todos los clientes registrados
def obtener_clientes(db:Session):
    return db.query(Cliente).all()

#Obtener cliente por DNI
def obtener_clientes_por_dni(db:Session,dni: str):
    return db.query(Cliente).filter(Cliente.DNI == dni).first()    #Cambie para que lo busque por DNI y no por id


#Funciones de Vehiculos

def obtener_todos_los_vehiculos(db:Session):
    return db.query(Vehiculo).all()