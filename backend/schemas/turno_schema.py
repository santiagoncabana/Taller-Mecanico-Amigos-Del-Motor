
from pydantic import BaseModel
from datetime import date, time

class TurnoCreate(BaseModel):
    # Datos del Cliente
    nombre_cliente: str
    telefono: str
    cuit: str
    
    # Datos del Vehículo
    patente: str
    modelo: str
    
    # Datos del Turno
    fecha: date        
    hora_inicio: time  
    