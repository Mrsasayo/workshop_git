import psycopg2
import json

def get_connection():
    """Establece y retorna una conexión a la base de datos."""
    with open("credenciales.json", "r") as file:
        credenciales = json.load(file)
    return psycopg2.connect(
        user=credenciales["user"],
        password=credenciales["password"],
        host=credenciales["host"],
        port=credenciales["port"],
        database=credenciales["database"]
    )

def create_table():
    """Crea la tabla de candidatos en la base de datos."""
    create_table_query = """
    CREATE TABLE IF NOT EXISTS candidates (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        email VARCHAR(100),
        country VARCHAR(100),
        application_date DATE,
        yoe INTEGER,
        seniority VARCHAR(50),
        technology VARCHAR(100),
        code_challenge_score FLOAT,
        technical_interview_score FLOAT
    );
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()
        print("Tabla creada exitosamente.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()

from sqlalchemy import create_engine, text
import pandas as pd

def create_database():
    # Código para crear la base de datos
    pass

def load_data_to_db(df):
    # Código para crear la tabla y cargar los datos
    pass

if __name__ == "__main__":
    # Ejecutar las funciones
    create_database()
    df = pd.read_csv("../data/raw/candidates.csv")
    load_data_to_db(df)