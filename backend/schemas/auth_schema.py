from pydantic import BaseModel
from .cliente_schemas import ClienteaBase




#Registro
class ClienteRegister(ClienteaBase):
    nombre:str
    email:str
    contrasena:str
    dni:int
    nro_telefono:int


#login
class ClienteLogin(BaseModel):
    email:str
    contrasena:str