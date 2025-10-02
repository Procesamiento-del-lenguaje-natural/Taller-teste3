## Cómo activar y desactivar el entorno virtual

**Activar el entorno virtual:**

- **Windows:**
  ```powershell
  .venv\Scripts\activate
  ```
- **MacOS / Linux:**
  ```bash
  source .venv/bin/activate
  ```

Verás el prefijo `(.venv)` en tu terminal si está activo.

**Desactivar el entorno virtual:**

En cualquier sistema, ejecuta:
```bash
deactivate
```

# Taller-1-teste2


## Instalación de dependencias

Asegúrate de tener Python 3.8 o superior instalado.

**Para correr localmente:**

1. Abre una terminal en la carpeta del proyecto.
2. Crea un entorno virtual:

   - **Windows:**
     ```powershell
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **MacOS / Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

Esto instalará todas las dependencias necesarias para ejecutar los tests y notebooks correctamente.

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

## ⚠️ Requisitos específicos para el Ejercicio 4

El **Ejercicio 4** (procesamiento de tweets) tiene validaciones especiales que requieren:

### 🔍 **Estructura obligatoria del código:**
- **DEBE usar un loop:** `for ... in tweets` (usando la variable `tweets` original)
- **DEBE incluir estas funciones específicas:**
  - `re.sub(` con asignación (`=`)
  - `.lower()` como método
  - `.append()` para agregar a la lista
  - `emoji_pattern.sub(` para remover emojis

### 📋 **Variable de salida requerida:**
- **DEBE crear:** `tweets_procesados` (lista con 10 tweets procesados)
- **DEBE procesar:** Saltos de línea, URLs, minúsculas, emojis

### ⚡ **Validaciones automáticas:**
- **Test 8:** Verifica estructura del código y uso de funciones (anti-trampa)
- **Test 9:** Verifica funcionalidad y salida correcta

### 💡 **Consejos:**
- NO modifiques los tweets originales en la primera celda
- USA exactamente `tweets_procesados` como nombre de variable final
- El loop DEBE iterar sobre `tweets` (no copies individuales)

