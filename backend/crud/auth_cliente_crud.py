from sqlalchemy.orm import Session
from ..database.models import Cliente,Empleado
from ..schemas.auth_schema import ClienteRegister, EmpleadoRegister
from MecApp.backend.security.security import pwd_context

def create_cliente(db: Session, cliente: ClienteRegister):
    db_cliente = Cliente(
        nombre=cliente.nombre,
        email=cliente.email,
        contrasena=cliente.contrasena,
        DNI=cliente.DNI
    )
    db.add(db_cliente)
    db.commit()
    db.refresh(db_cliente)
    return db_cliente

def create_empleado(db: Session, empleado: EmpleadoRegister):
    db_empleado = Empleado(
        nombre=empleado.nombre,
        email=empleado.email,
        contrasena=empleado.contrasena,
        rol=empleado.rol,
        disponible=empleado.disponible
    )
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado



def autenticacion_cliente(db: Session, correo: str, contrasena_user: str):
    cliente = db.query(Cliente).filter(Cliente.email == correo).first()
    
    if not cliente:
        return None
    if cliente.contrasena == contrasena_user:
        return cliente
    return None




def autenticacion_encargado(db: Session, correo: str, contrasena_user: str):
    empleado = db.query(Empleado).filter(Empleado.email == correo).first()
    
    if not empleado:
        return None
    if empleado.contrasena == contrasena_user:
        return empleado
    return None