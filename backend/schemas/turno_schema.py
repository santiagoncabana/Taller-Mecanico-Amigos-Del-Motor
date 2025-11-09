
from pydantic import BaseModel
from datetime import date, time
from database.models import Cliente, Turno

class TurnoCreate(BaseModel):
    # Datos del Cliente
    telefono: str
    DNI: int
    
    # Datos del Vehículo
    #patente: str
    #modelo: str
    
    # Datos del Turno
    fecha: str  
    hora: str   
    estado: str = "Pendiente"


class TurnoResponse(BaseModel):
    id: int
    cliente_id: int
    empleado_id: int
    fecha: str
    hora: str

    class Config:
        from_attributes = True
        

class TurnoUpdate(BaseModel):
    estado: str = "Finalizado"
    
class orden_de_servicio_create(BaseModel):
    descripcion_trabajo: str
    precio_total: int
    turno_id: int
    patente: str
    modelo: str
    
class OrdenCreate(BaseModel):
    turno_id: int
    descripcion_trabajo: str
    precio_total: int
    patente: str
    modelo: str

class OrdenResponse(BaseModel):
    id: int
    turno_id: int
    descripcion_trabajo: str
    precio_total: int
    patente: str
    modelo: str
    nombre_cliente: str
    telefono_cliente: str
    dni_cliente: str
    
    class Config:
        from_attributes = True