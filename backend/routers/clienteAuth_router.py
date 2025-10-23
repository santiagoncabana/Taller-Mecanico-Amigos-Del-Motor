from fastapi import APIRouter, Depends, HTTPException
from ..database.database import get_db, Session
from ..crud.auth_cliente_crud import create_cliente,autenticacion_cliente    
from ..schemas.auth_schema import ClienteRegister
from ..schemas.auth_schema import ClienteLogin


router = APIRouter()

# Registro de cliente
@router.post("/register",tags=["register cliente"])
def registerCliente(cliente: ClienteRegister, db: Session = Depends(get_db)):
    return create_cliente(db, cliente)

#login cliente
@router.post("/login", tags=["login cliente"])
def loginCliente(cliente: ClienteLogin, db: Session = Depends(get_db)):
    user = autenticacion_cliente(db, cliente.email, cliente.contrasena)
    if user:
        return {"message": "Autenticación exitosa", "nombre": user.nombre, "email": user.email}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

