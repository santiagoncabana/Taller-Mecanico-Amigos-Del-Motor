from backend.database.database import engine

try:
    with engine.connect() as connection:
        print("Conexion exitosa a la Base de Datos.")
except Exception as e:
    print("Error al conectar a la Base de Datos.")
    print(e)
