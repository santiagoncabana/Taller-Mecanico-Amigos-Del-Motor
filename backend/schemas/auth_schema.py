from pydantic import BaseModel
from backend.schemas.cliente_schemas import ClienteaBase




#Registro
class ClienteRegister(ClienteaBase):
    nombre:str
    email:str
    contrasena:str
    dni:str
    nro_telefono:str


#login
class ClienteLogin(BaseModel):
    email:str
    contrasena:str