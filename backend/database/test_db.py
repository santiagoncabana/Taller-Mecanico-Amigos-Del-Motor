from MecApp.backend.database.database import engine, Base
from MecApp.backend.database import models

try:
    with engine.connect() as connection:
        print("Conexión exitosa a la base de datos.")
except Exception as e:
    print("Error al conectar a la base de datos.")
    print(e)
