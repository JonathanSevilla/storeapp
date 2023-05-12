# storeapp

## Creado por: Jonathan Sevilla
## Email: jonathansevilla.7@gmail.com
## Infraestructura del proyecto:
### El proyecto está hecho con el framework de Python, Django 3.2 y para la consturccion de las APIs se uso DRF


## Crear entorno virtual con el siguiente comando:
```
python -m venv env
```

## Como ejecutar este proyecto?
### Abre la terminal y ejecuta el siguiente comando:
```
pip install -r requirements.txt
```
### Ejecuta el siguiente comando, para acceder al entorno virtual:
```
env\scripts\activate
```
### Muevete a la carpeta de el projecto. Y ejecuta los siguientes comando:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Para usarlo desde Docker, ejecute los siguientes comandos:
```
docker build -t storeapp_django .
docker-compose up
```

### De esta manera puede ejecutar sin problemas la app.