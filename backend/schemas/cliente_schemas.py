from pydantic import BaseModel
from typing import Optional

        
class ClienteOut(BaseModel):  #ClienteOut se usa para la respuesta (response_model) y agrega id
    nombre: str         
    id: int
    email: str         #Agregue email, contrasena y telefono para ver esos datos en la vista del encargado cuando llame a todos los clientes
    contrasena: str
    telefono: Optional[str] = None #Esto hace que el cliente que todavia no registro su numero muestre null
    
    class config:
        orm_mode = True #orm_mode = True permite que Pydantic convierta instancias ORM (objetos SQLAlchemy) a dict/JSON sin problemas