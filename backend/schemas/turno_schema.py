
from pydantic import BaseModel
from datetime import date, time

class TurnoCreate(BaseModel):
    # Datos del Cliente
    cliente_id: str
    telefono: str
    cuit: str
    
    # Datos del Vehículo
    patente: str
    modelo: str
    
    # Datos del Turno
    fecha: date        
    hora_inicio: time  
    empleado_id: int
    