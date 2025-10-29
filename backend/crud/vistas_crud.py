from sqlalchemy.orm import Session
from database.models import Cliente
from ..crud.auth_cliente_crud import create_cliente as crear_cliente_vista

def todos_los_clientes(db:Session):
    return db.query(Cliente).all()

nuevo_cliente = crear_cliente_vista

