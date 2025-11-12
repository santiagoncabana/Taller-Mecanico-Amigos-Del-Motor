
from pydantic import BaseModel
from datetime import date, time
from database.models import Cliente, Turno

class TurnoCreate(BaseModel):
    # Datos del Cliente
    telefono: str
    DNI: int
    
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
    marca: str
    anio : int
    
class OrdenCreate(BaseModel):
    turno_id: int
    descripcion_trabajo: str
    precio_total: int
    patente: str
    modelo: str
    marca: str
    anio: int

class OrdenResponse(BaseModel):
    id: int
    turno_id: int
    descripcion_trabajo: str
    precio_total: int
    patente: str
    modelo: str
    marca: str
    anio: int
    nombre_cliente: str
    telefono_cliente: int
    dni_cliente: str
    fecha_turno: str
    empleado_id: int
    vehiculo_id: int
    
    class Config:
        from_attributes = True