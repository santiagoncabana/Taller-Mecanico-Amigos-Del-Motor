from pydantic import BaseModel
from .cliente_schemas import ClienteaBase


#Registro
class ClienteRegister(ClienteaBase):
    contrasena:str


#login
class ClienteLogin(ClienteaBase):
    correo:str
    contrasena:str