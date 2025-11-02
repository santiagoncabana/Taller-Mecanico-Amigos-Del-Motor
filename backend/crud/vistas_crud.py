from sqlalchemy.orm import Session
from database.models import Cliente
from ..crud.auth_cliente_crud import create_cliente as crear_cliente_vista

def obtener_clientes(db:Session):
    return db.query(Cliente).all()


def obtener_clientes_por_id(db:Session,cliente: int):
    return db.query(Cliente).filter(Cliente.id == cliente).first()



