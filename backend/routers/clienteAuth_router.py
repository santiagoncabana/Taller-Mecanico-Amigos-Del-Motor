from fastapi import APIRouter, Depends, HTTPException
from ..database.database import get_db, Session
from ..crud.auth_cliente_crud import create_cliente,autenticacion_cliente  ,autenticacion_encargado ,create_empleado
from ..schemas.auth_schema import ClienteRegister
from ..schemas.auth_schema import ClienteLogin
from ..schemas.auth_schema import EncargadoLogin
from ..schemas.auth_schema import EmpleadoRegister


router = APIRouter()

# Registro de cliente
@router.post("/register",tags=["register cliente"])
def registerCliente(cliente: ClienteRegister, db: Session = Depends(get_db)):
    return create_cliente(db, cliente)
    


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