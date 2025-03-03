import psycopg2
import json

# Cargar credenciales desde el archivo JSON
with open("../credenciales.json", "r") as file:
    credenciales = json.load(file)

# Establecer la conexión
try:
    conn = psycopg2.connect(
        user=credenciales["user"],
        password=credenciales["password"],
        host=credenciales["host"],
        port=credenciales["port"],
        database=credenciales["database"]
    )
    print("¡Conexión exitosa!")
except Exception as e:
    print(f"Error al conectar a la base de datos: {e}")
finally:
    if conn:
        conn.close()