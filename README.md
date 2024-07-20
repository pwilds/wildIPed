# wildIPed

wildIPed es una aplicación web sencilla desarrollada con Flask que permite buscar información sobre una dirección IP utilizando la API de `ipinfo.io`. Además, proporciona la funcionalidad para obtener la dirección IP pública del usuario.

## Requisitos

- Python 3.7 o superior
- Flask
- requests

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/wildIPed.git
cd wildIPed
```

2. Crea un entorno virtual y activa el entorno:

```bash
python -m venv venv
source venv/bin/activate   # En Windows usa `venv\Scripts\activate`
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Ejecuta la aplicación Flask:

```bash
python app.py
```

2. Abre tu navegador y ve a `http://127.0.0.1:5000`.

## Rutas

- `GET /`: Página de inicio donde se puede ingresar una dirección IP para buscar información.
- `POST /buscar`: Realiza la búsqueda de la información de la dirección IP ingresada.
- `GET /get_my_ip`: Devuelve la dirección IP pública del usuario.

## Archivos

- `app.py`: Archivo principal de la aplicación Flask.
- `templates/index.html`: Plantilla HTML para la página de inicio.
- `templates/resultado.html`: Plantilla HTML para mostrar los resultados de la búsqueda.

## Ejemplo de Uso

1. Ingresar una dirección IP en la página de inicio y hacer clic en el botón de búsqueda.
2. La aplicación mostrará información sobre la dirección IP ingresada (ubicación, proveedor de servicios de Internet, etc.).
3. También se puede hacer una solicitud a `/get_my_ip` para obtener la dirección IP pública del usuario.

## API

La aplicación utiliza la API de `ipinfo.io` para obtener información sobre direcciones IP. Necesitas un token de API que puedes obtener registrándote en [ipinfo.io](https://ipinfo.io/signup).

Reemplaza `api_token` en `app.py` con tu propio token de API.

```python
api_token = 'tu_api_token'
```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio.
--
