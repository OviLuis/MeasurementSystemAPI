# MeasurementSystemAPI

Micro servicio que expone una API creada con Django Rest Framework para gestionar las lecturas de dispositivos.


Estructura del api: 
- GET: `api/measures/` Permite obtener el listado de todas las lecturas registradas
- POST: `api/measures/` permite registrar una lectura, se deben enviar los datos: `{'device_id': id del dispositivo,
'measure_value': valor de la lectura,
'measure_unit': unidad de medida,
'measure_date': estampa de tiempo}`
- DELETE: `api/measures/<pk>/` eliminar una lectura
- GET: `api/measures/<pk>/` obtener una lectura
- PUT: `api/measures/<pk>/` modificar datos de una lectura


Para ejecutar el microservicio localmente, se debe crear un ambiente virtual.  
1. En el instalar los requerimientos `pip install -r requirements.txt`
2. Ejectar las migraciones `python manage.py makemigrations` desde la carpeta `apps`
3. Ejecutar `python manage.py migrate` desde la carpeta `apps`
4. ejecutar `python manage.py runserver` desde la carpeta `apps`

Para ejecutar el microservicio desde docker:
1. construir la imagen `apimicroservice`. ejecutar `docker build -t apimicroservice .` desde la raiz del projecto donde esta ubicado el archio `Dockerfile`
2. ejecutar `docker-compose up -d` desde la raiz del projecto o donde este ubicado el archivo `docker-compose.yml`

Adicionalmente el microservicio permite realizar la descarga de un archivo en formato csv con las lecturas registradas visitando directamente `http://localhost:8000/down_load_csv_file/` o `http://localhost:8000`

