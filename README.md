# Proyecto ETL: Carga de Datos de Airbnb

Este proyecto es un proceso ETL (Extract, Transform, Load) que tiene como objetivo cargar y transformar datos de Airbnb para su posterior análisis. En esta primera etapa, nos enfocamos en la carga de datos desde un archivo CSV a una base de datos PostgreSQL.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

Proyecto_ETL:           .gitignore, credentials.json, README.md

Proyecto_ETL/data:      Airbnb_Open_Data.csv

Proyecto_ETL/Notebooks: 001_DataLoad.ipynb, 002_EDA.ipynb, 003_CleanData.ipynb


### Descripción de Archivos y Carpetas

- **.gitignore**: Archivo que especifica los archivos y carpetas que deben ser ignorados por Git. En este caso, se ignora el archivo `credentials.json` por razones de seguridad.
- **credentials.json**: Archivo que contiene las credenciales de acceso a la base de datos PostgreSQL.
- **README.md**: Este archivo, que proporciona una descripción general del proyecto.
- **data/**: Carpeta que contiene el archivo CSV con los datos de Airbnb.
- **Notebooks/**: Carpeta que contiene los notebooks de Jupyter utilizados en el proyecto.

## Notebook 001_DataLoad.ipynb

Este notebook se encarga de la carga inicial de los datos desde el archivo CSV `Airbnb_Open_Data.csv` a una base de datos PostgreSQL.

### Pasos Realizados en el Notebook

1. **Carga de Credenciales**: Se cargan las credenciales de la base de datos desde el archivo `credentials.json`.

2. **Carga del Dataset**: Se carga el archivo CSV `Airbnb_Open_Data.csv` en un DataFrame de Pandas.

3. **Creación de la Base de Datos**: Se verifica si la base de datos `airbnb` existe en PostgreSQL. Si no existe, se crea.

4. **Carga de Datos a la Base de Datos**: Se crea una tabla llamada `airbnb_data` en la base de datos y se cargan los datos del DataFrame en esta tabla.

5. **Verificación de Datos**: Se realizan consultas simples para verificar que los datos se han cargado correctamente en la base de datos.

### Requisitos

- **Python**
- **Pandas**
- **SQLAlchemy**
- **Psycopg2**
- **PostgreSQL**

### Instrucciones de Uso

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/Proyecto_ETL.git
   cd Proyecto_ETL

2. **Instalar Dependencias**:
   ```bash
   pip install pandas sqlalchemy psycopg2

Configurar Credenciales:
se debe crear un archivo `credentials.json` con el siguiente contenido:
3. **Instalar Dependencias**:
   ```javascript
   {
    "user": "user",
    "password": "password",
    "host": "host",
    "port": "port", 
    "database": "database"
  }
  ```

luego de haberlo creado, Asegúrate de que el archivo credentials.json esté correctamente configurado con tus credenciales de PostgreSQL.

## Ejecutar el Notebook:
Abre el notebook 001_DataLoad.ipynb en Jupyter y ejecuta las celdas en orden.
