# Backend de Bidcraft

## Cómo Empezar

### Prerrequisitos

- Docker

### Instalación

1. Clonar el repositorio:
    ```bash
    https://github.com/psychofizz/app.git
    ```

1b. Actualizar el docker-compose en la linea sobre volumes, use el directorio donde esta ubicado el proyecto.

2. Crear y activar un entorno virtual:
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```
    Si no funciona por problemas entre sistemas operativos se puede reconstruir el venv
     Para esto borrar los .venv y venv
     luego
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Lanzar docker en consola y ejecutar en /app
   ```bash
   docker-compose up -d --build
   ```

## Licencia

Este proyecto está bajo alguna licencia.
