from pydantic import BaseModel


class ClienteaBase(BaseModel):
    nombre:str

    # Configuración esencial para que Pydantic pueda leer objetos del ORM
    class Config:
        orm_mode = True
        
class ClienteOut(ClienteaBase): #ClienteOut se usa para la respuesta (response_model) y agrega id.
    id: int
    class config:
        orm_mode = True #orm_mode = True permite que Pydantic convierta instancias ORM (objetos SQLAlchemy) a dict/JSON sin problemas.