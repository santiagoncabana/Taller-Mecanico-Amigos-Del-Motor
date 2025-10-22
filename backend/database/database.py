# Importamos las librerias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@127.0.0.1/mecapp"

# Creamos el puente para la conexion con Python
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()

# Obtenemos la sesion de la 'Base de Datos'
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 