

# Instalación y Configuración Inicial

## Preparación Inicial
1. Instalar docker -> https://docs.docker.com/get-docker/
2. Instalar docker-compose -> https://docs.docker.com/compose/install/

## Instalación de Odoo con docker
1. Descargar el repositorio
~~~
git clone https://github.com/Killdemons/TBT.git
~~~
2. Ingresar a la carpeta 
~~~
cd tbt
~~~
3. Opcional: Editar docker-compose.yaml, esto siempre y cuando se requiera añadir nuevos servicios o modificar parámetros.
4. Ejecutar docker-compose
~~~
docker-compose up -d
~~~
