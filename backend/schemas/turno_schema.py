
from pydantic import BaseModel
from datetime import date, time

class TurnoCreate(BaseModel):
    # Datos del Cliente
    telefono: str
    DNI: int
    
    # Datos del Vehículo
    patente: str
    modelo: str
    
    # Datos del Turno
    fecha: str  
    hora: str   
    #cliente_id: int


class TurnoResponse(BaseModel):
    id: int
    cliente_id: int
    empleado_id: int
    fecha: str
    hora: str
    #estado: str

    class Config:
        from_attributes = True