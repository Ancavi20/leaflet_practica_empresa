# Prueba técnica Solardrone
Este proyecto consiste en una prueba técnica para la empresa Solardrone como desarrollador. 



## Requisitos

- Python 3.10
- Django 4.2.6
- rasterio 1.3.8
- Pillow 8.2.0
- requests 2.31.0
- matplotlib 3.8.0
- folium 0.14.0
## Configuración del entorno

1. Crea un entorno virtual:

```bash
  python3 -m venv 'ruta/del/entorno'
  cd 'entorno'
  source venv/bin/activate
```
2. Activar el entorno virtual
  - En Windows:
```
  .\Scripts\activate
```
  - En Linux/macOS
   ```
  source ./bin/activate
``` 
3. Instala las dependencias:
```
 pip install -r requirements.txt
```
4. Instalar paquetes necesarios para trabajar con Leaflet:
```
pip install leaflet
npm install plotty --save
```
5. Realiza las migraciones:
``` 
python manage.py migrate
``` 
6. Ejecuta el servidor:
``` 
python manage.py runserver
``` 
7. Abre tu navegador y ve a http://127.0.0.1:8000/ para ver la aplicación.
## Características

- Mapa Interactivo: Utiliza Leaflet para mostrar un mapa interactivo.
- Agregar Ubicaciones: Puedes agregar nuevas ubicaciones haciendo clic derecho en el mapa.
- Editar y Eliminar: Edita y elimina ubicaciones existentes desde la lista de marcadores.
- Subir Archivos: Permite subir archivos .tif y visualizarlos en el mapa, con opción para seleccionar el modo RGB.

## Estructura del Proyecto
- **map**: Contiene la configuración del proyecto Django y las vistas.
- **static**: Archivos estáticos como hojas de estilo y scripts de JavaScript.
- **templates**: Plantillas HTML.