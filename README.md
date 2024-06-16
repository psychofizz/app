# Plataforma de Subastas de Honduras

## Descripción

Nuestra plataforma de subastas se centra en el desarrollo de un mercado que actualmente no existe en Honduras. Aunque hay muchas plataformas de e-commerce en el país, pocas se enfocan en el modelo de venta de subastas. Esto nos proporciona un nicho de mercado que puede desarrollarse de una manera que otras plataformas no han previsto. 

La plataforma está diseñada para manejar transacciones y objetos de alto valor, implementando verificaciones de identidad para reducir la cantidad de fraude y actividades de mala fe. Nuestro objetivo es ofrecer una experiencia segura y confiable tanto para compradores como para vendedores.

Además, la plataforma será accesible para todo el público hondureño, ya sea desde computadoras o dispositivos móviles, gracias a un diseño responsive y el uso de tecnologías web probadas en el mercado que pueden manejar nuestras necesidades.

## Tecnologías Utilizadas

### Backend

- **Django**: Django es un framework web de alto nivel basado en Python que facilita el desarrollo rápido y seguro de aplicaciones web complejas. Proporciona una arquitectura bien estructurada y numerosas características integradas, como autenticación de usuarios, administración de bases de datos y seguridad.

### Base de Datos

- **PostgreSQL**: PostgreSQL es un sistema de gestión de bases de datos relacional de código abierto y altamente confiable. Ofrece capacidades avanzadas de almacenamiento y consulta, soporte para transacciones ACID, y es compatible con una amplia variedad de tipos de datos, lo que lo convierte en una opción ideal para el almacenamiento de datos de la plataforma de subastas.

## Características

- **Verificación de Identidad**: Implementamos un sistema de verificación de identidad para garantizar la autenticidad de los usuarios y reducir el fraude.
- **Diseño Responsive**: La plataforma está diseñada para ser accesible desde cualquier dispositivo, ya sea una computadora de escritorio o un dispositivo móvil.
- **Transacciones Seguras**: Nos enfocamos en ofrecer una plataforma segura para manejar transacciones y objetos de alto valor.
- **Experiencia de Usuario**: Priorizamos una experiencia de usuario de alta calidad, asegurando que la plataforma sea intuitiva y fácil de usar.

## Cómo Empezar

### Prerrequisitos

- Docker

### Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/tuusuario/nombre-del-repositorio.git
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
