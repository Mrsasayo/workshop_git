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

### Instalar Dependencias:
   ```bash
   pip install pandas sqlalchemy psycopg2 matplotlib seaborn 
   ```

## Notebook 001_DataLoad.ipynb

Este notebook se encarga de la carga inicial de los datos desde el archivo CSV `Airbnb_Open_Data.csv` a una base de datos PostgreSQL.

### Pasos Realizados en el Notebook

1. **Carga de Credenciales**: Se cargan las credenciales de la base de datos desde el archivo `credentials.json`.

2. **Carga del Dataset**: Se carga el archivo CSV `Airbnb_Open_Data.csv` en un DataFrame de Pandas.

3. **Creación de la Base de Datos**: Se verifica si la base de datos `airbnb` existe en PostgreSQL. Si no existe, se crea.

4. **Carga de Datos a la Base de Datos**: Se crea una tabla llamada `airbnb_data` en la base de datos y se cargan los datos del DataFrame en esta tabla.

5. **Verificación de Datos**: Se realizan consultas simples para verificar que los datos se han cargado correctamente en la base de datos.

### Instrucciones de Uso

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/Proyecto_ETL.git
   cd Proyecto_ETL

Configurar Credenciales:
se debe crear un archivo `credentials.json` con el siguiente contenido:

2. **Instalar Dependencias**:
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

### Ejecutar el Notebook:
Abre el notebook 001_DataLoad.ipynb en Jupyter y ejecuta las celdas en orden.

# Proyecto ETL: Análisis Exploratorio de Datos (EDA)

En esta etapa del proyecto, nos enfocamos en el análisis exploratorio de datos (EDA) utilizando el notebook `002_EDA.ipynb`. Este notebook tiene como objetivo explorar y visualizar los datos de Airbnb cargados en la base de datos PostgreSQL para identificar patrones, tendencias y posibles problemas en los datos.

## Notebook 002_EDA.ipynb

Este notebook realiza un análisis exploratorio de los datos de Airbnb, incluyendo la identificación de valores nulos, duplicados, y la visualización de distribuciones y relaciones entre variables.

### Pasos Realizados en el Notebook

1. **Carga de Datos**: Se conecta a la base de datos PostgreSQL y se cargan los datos desde la tabla `airbnb_data`.

2. **Exploración Inicial**:
   - Se verifica el tamaño del dataset (número de filas y columnas).
   - Se identifican filas duplicadas.
   - Se calculan los valores nulos y su porcentaje por columna.


3. **Análisis de Tipos de Datos**: Se revisan los tipos de datos de cada columna para asegurar que sean correctos.

4. **Visualización de Datos**:
   - Distribución de precios.
   - Relación entre precios y noches mínimas.
   - Distribución de tarifas de servicio.
   - Detección de valores atípicos en precios y tarifas de servicio.
   - Distribución de tipos de habitación.
   - Distribución de publicaciones por año de construcción.
   - Porcentaje de hosts verificados vs. no verificados.
   - Cantidad de publicaciones por grupo de vecindario.
   - Porcentaje de cada tipo de política de cancelación.
   - Distribución de propiedades con reserva instantánea.

### Ejecutar el Notebook:
Abre el notebook 002_EDA.ipynb en Jupyter y ejecuta las celdas en orden.

# Proyecto ETL: Limpieza de Datos

En esta etapa del proyecto, nos enfocamos en la limpieza y transformación de los datos utilizando el notebook `003_CleanData.ipynb`. Este notebook tiene como objetivo preparar los datos para su posterior análisis, eliminando valores nulos, corrigiendo errores y transformando columnas para que sean más útiles.

## Notebook 003_CleanData.ipynb

Este notebook realiza la limpieza y transformación de los datos de Airbnb almacenados en la base de datos PostgreSQL. Se enfoca en la creación de una nueva tabla (`airbnb_EDA`), la renombración de columnas, la eliminación de columnas innecesarias, el manejo de valores nulos y la corrección de errores en los datos.

### Pasos Realizados en el Notebook

1. **Carga de Datos**:
   - Se conecta a la base de datos PostgreSQL y se cargan los datos desde la tabla `airbnb_data`.

2. **Creación de una Nueva Tabla (`airbnb_EDA`)**:
   - Se crea una nueva tabla llamada `airbnb_EDA` con la misma información que la tabla original (`airbnb_data`).
   - Se verifica que la nueva tabla se haya creado correctamente y que contenga el mismo número de registros que la tabla original.

3. **Renombración de Columnas**:
   - Se renombran las columnas que contienen espacios en sus nombres para facilitar su manejo en consultas SQL.
   - Ejemplo: `host id` se convierte en `host_id`, `minimum nights` se convierte en `minimum_nights`, etc.

4. **Eliminación de Columnas Innecesarias**:
   - Se eliminan columnas que no son relevantes para el análisis, como `host_name`, `lat`, `long`, `country_code`, `country`, `neighbourhood`, y `house_rules`.

5. **Manejo de Valores Nulos**:
   - Se reemplazan los valores nulos en columnas de texto con `'not fill'`.
   - Se reemplazan los valores nulos en columnas numéricas con `-1`.
   - Se transforma la columna `last_review` para convertir las fechas en un formato numérico (`AAAAMMDD`). Las fechas nulas se reemplazan con `99999999`.

6. **Corrección de Errores en los Datos**:
   - Se corrigen errores en la columna `neighbourhood_group`, como `'brookln'` y `'manhatan'`, que se cambian a `'Brooklyn'` y `'Manhattan'`, respectivamente.


Ejecutar el Notebook:
Abre el notebook 003_CleanData.ipynb en Jupyter y ejecuta las celdas en orden.
