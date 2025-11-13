from fastapi import APIRouter, Depends, HTTPException
from ..database.database import get_db, Session
from ..crud.auth_cliente_crud import create_cliente,autenticacion_cliente  ,autenticacion_encargado ,create_empleado
from ..schemas.auth_schema import ClienteRegister, ClienteLogin
from ..database.models import Cliente
from ..schemas.auth_schema import EncargadoLogin, EmpleadoRegister
from fastapi import Form
from MecApp.backend.security.security import pwd_context


SECRET_KEY = "cabana"
ALGORITHM = "HS256"

router = APIRouter()

"""# Registro de cliente
@router.post("/register",tags=["register cliente"])
def registerCliente(cliente: ClienteRegister, db: Session = Depends(get_db)):
    return create_cliente(db, cliente)"""

@router.post("/register")
def register(
    DNI: int = Form(...),
    nombre: str = Form(...),
    email: str = Form(...),
    contrasena: str = Form(...),
    db: Session = Depends(get_db)
):
    if db.query(Cliente).filter(Cliente.DNI == DNI).first():
        raise HTTPException(400, "DNI ya registrado")

    #hashed = pwd_context.hash(contrasena)
    cliente = Cliente(DNI=DNI, nombre=nombre, email=email, contrasena=contrasena)
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return {"mensaje": "Cliente creado", "id": cliente.id}
    

#Registro Encargado
@router.post("/register/encargado", tags=["register encargado"])
def registerEncargado(empleado: EmpleadoRegister, db: Session = Depends(get_db)):
    return create_empleado(db, empleado)


# Login Cliente
@router.post("/login", tags=["login cliente"])
def loginCliente(cliente: ClienteLogin, db: Session = Depends(get_db)):
    user = autenticacion_cliente(db, cliente.email, cliente.contrasena)
    if user:
        return {"message": "Autenticación exitosa", "email": user.email}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

# Login Encargado
@router.post("/encargado/login", tags=["login encargado"])
def loginEncargado(cliente: EncargadoLogin, db: Session = Depends(get_db)):
    user = autenticacion_encargado(db, cliente.email, cliente.contrasena)
    if user:
        return {
            "message": "Autenticación exitosa",
            "email": user.email,
            "nombre": user.nombre,
            "rol": user.rol
        }
    raise HTTPException(status_code=401, detail="Credenciales incorrectas para el encargado")