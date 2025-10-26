# Importamos las Librerias
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    id = Column(Integer, primary_key=True, index=True) # Pk
    nombre = Column(String(100))
    email = Column(String(100), unique=True)
    contrasena = Column(String(100))

    vehiculos = relationship("Vehiculo", back_populates="cliente")
    turnos = relationship("Turno", back_populates="cliente")


class Vehiculo(Base):
    __tablename__ = "vehiculo"

    id = Column(Integer, primary_key=True, index=True) # Pk
    marca = Column(String(50))
    modelo = Column(String(50))
    año = Column(Integer)
    cliente_id = Column(Integer, ForeignKey("cliente.id"))

    cliente = relationship("Cliente", back_populates="vehiculos")


class Empleado(Base):
    __tablename__ = "empleado"

    id = Column(Integer, primary_key=True, index=True) # Pk
    nombre = Column(String(100))
    rol = Column(String(50))  

    turnos = relationship("Turno", back_populates="empleado")


class Turno(Base):
    __tablename__ = "turno"

    id = Column(Integer, primary_key=True, index=True) # Pk
    fecha = Column(Date)
    estado = Column(String(50))
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    empleado_id = Column(Integer, ForeignKey("empleado.id"))

    cliente = relationship("Cliente", back_populates="turnos")
    empleado = relationship("Empleado", back_populates="turnos")
    orden_servicio = relationship("OrdenDeServicio", back_populates="turno", uselist=False)


class OrdenDeServicio(Base):
    __tablename__ = "orden_de_servicio"

    id = Column(Integer, primary_key=True, index=True) # Pk
    descripcion_trabajo = Column(String(255))
    precio_total = Column(Float)
    estado = Column(String(50))
    turno_id = Column(Integer, ForeignKey("turno.id"))

    turno = relationship("Turno", back_populates="orden_servicio")
    trabajos = relationship("Trabajo", back_populates="orden_servicio")


class Trabajo(Base):
    __tablename__ = "trabajo"

    id = Column(Integer, primary_key=True, index=True) # Pk
    descripcion_trabajo = Column(String(255))
    repuesto_usado = Column(String(255))
    precio_total = Column(Float)
    orden_servicio_id = Column(Integer, ForeignKey("orden_de_servicio.id"))

    orden_servicio = relationship("OrdenDeServicio", back_populates="trabajos")
