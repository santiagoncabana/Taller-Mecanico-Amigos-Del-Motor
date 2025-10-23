from pydantic import BaseModel


class ClienteaBase(BaseModel):
    nombre:str

    # Configuración esencial para que Pydantic pueda leer objetos del ORM
    class Config:
        orm_mode = True