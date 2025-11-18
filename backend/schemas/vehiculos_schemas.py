from database.models import Vehiculo
from pydantic import BaseModel


class vehiculos(BaseModel):
    id: int
    marca:str
    modelo:str
    anio:int
    patente:str
    cliente_id:int