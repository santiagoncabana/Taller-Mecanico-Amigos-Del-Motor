from pydantic import BaseModel

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

# class UserAuthResponse(BaseModel):
#     nombre: str

#     email: str