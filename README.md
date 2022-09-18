# Tarea N°1 Sistemas Distribuidos - Implementación de Redis y gRPC entre Cliente, Servidor y Base de datos 
Integrantes:
  - Nicolás Ríos
  - Rómulo Otárola
## Inicializar contenedores
Se debe ejecutar el archivo **docker-compose.yml** con el comando:
``sh
docker-compose up --build``
## Importante!
Luego de inicializar los contendores se deben descomprimir el archivo **user-ct-test-collection-09.txt.gz** contenido en **Crawler**
## Importante 2
Se deben instalar las dependencias referenciadas en **requirements.txt** para el correcto funcionamiento de los códigos
## Scrap de páginas e inserción de datos
Dentro de la carpeta **Crawler** se debe ejecutar el siguiente comando:
``sh
python3 scrap-db.py``
Este se encarga de insertar la información del dataset limpiado y luego lo inserta en la base de datos
