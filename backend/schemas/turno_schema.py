
from pydantic import BaseModel
from datetime import date, time

class TurnoCreate(BaseModel):
    # Datos del Cliente
    telefono: str
    cuit: str
    
    # Datos del Vehículo
    patente: str
    modelo: str
    
    # Datos del Turno
    fecha: str  
    hora_inicio: str
    