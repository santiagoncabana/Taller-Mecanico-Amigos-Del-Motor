from fastapi import APIRouter,Depends
from database.database import get_db
from schemas.auth_schema import ClienteRegister
from database.database import Session
from crud.user import 

app = APIRouter()


@app.post("/register")
def registerCliente(cliente:ClienteRegister,db:Session=Depends(get_db)):
    pass

