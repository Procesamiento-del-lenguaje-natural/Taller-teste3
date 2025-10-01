# Taller-1-teste2

## Instalación de dependencias

Asegúrate de tener Python 3.8 o superior instalado.

### Windows

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### MacOS / Linux 

Abre la terminal en la carpeta del proyecto y ejecuta:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Si agregas paquetes a `requirements.txt` (por ejemplo, `pyspellchecker`), solo debes listarlos uno por línea.

## Dependencias adicionales para pruebas

Para ejecutar los tests, necesitas instalar las siguientes dependencias:

### pytest (Framework de testing)
```bash
pip install pytest
```

### nbformat (Para análisis de notebooks)
```bash
pip install nbformat
```

**Importante**: El paquete `nbformat` es esencial para que los tests funcionen correctamente, ya que permite:
- Leer y analizar archivos `.ipynb` (Jupyter notebooks)
- Validar el código directamente desde los notebooks
- Mantener la estructura de carpetas sin modificaciones

### Instalación completa desde requirements.txt

Todas las dependencias están listadas en `requirements.txt`. Para instalar todo de una vez:

```bash
pip install -r requirements.txt
```

### Para GitHub Actions

Si usas GitHub Actions, asegúrate de incluir este paso en tu workflow:

```yaml
- name: Install dependencies
  run: |
    pip install pytest nbformat
    pip install -r requirements.txt
```

## Ejemplo de ejecución de tests

Para ejecutar un test específico, por ejemplo `test_1.py`, usa:

```bash
pytest tests/ejercicio1/test_1.py
```

Para ejecutar todos los tests del ejercicio 1:

```bash
pytest tests/ejercicio1/
```

Para ejecutar todos los tests de la carpeta:

```bash
pytest tests/
```

