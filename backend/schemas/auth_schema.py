from pydantic import BaseModel
from typing import Optional

#Registro
class ClienteRegister(BaseModel):
    nombre:str
    email:str
    contrasena:str
    DNI:int


#login
class ClienteLogin(BaseModel):
    email:str
    contrasena:str


#login encargado
class EncargadoLogin(BaseModel):
    email: str
    contrasena: str # Asegúrate que coincida con el campo JS (sin 'ñ')

class EmpleadoRegister(BaseModel):
    nombre: str
    email: str
    contrasena: str
    rol: str  # Puedes establecer el rol fijo aquí, por ejemplo: "encargado"
    disponible: bool

class ClienteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    contrasena: Optional[str] = None