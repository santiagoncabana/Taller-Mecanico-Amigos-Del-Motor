from sqlalchemy.orm import Session

from ..database.models import Cliente

from ..schemas.auth_schema import ClienteRegister

def create_cliente(db: Session, cliente: ClienteRegister):
    db_cliente = Cliente(
        nombre=cliente.nombre,
        email=cliente.email,
        contrasena=cliente.contrasena
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente



def autenticacion_cliente(db: Session, correo: str, contrasena_user: str):
    cliente = db.query(Cliente).filter(Cliente.email == correo).first()
    
    if not cliente:
        return None
    if cliente.contrasena == contrasena_user:
        return cliente
    return None