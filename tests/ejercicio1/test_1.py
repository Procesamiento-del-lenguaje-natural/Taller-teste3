# Test 1 - Validación de la no modificación de las variables del ejercicio1

import sys
import os
import pytest

# Añadir la ruta al directorio 'data' para importar la función
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))
from funciones_ejercicio1 import obtener_variables_ejercicio1

# Importar las variables del notebook del estudiante
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks')))

def test_1():
    # Obtener las variables originales
    originales = obtener_variables_ejercicio1()
    
    # Ejecutar el notebook del estudiante para obtener sus variables
    import nbformat
    from nbconvert.preprocessors import ExecutePreprocessor
    
    notebook_path = os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio1.ipynb')
    
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
    
    # Extraer las variables del namespace del notebook ejecutado
    alumno_vars = {}
    for cell in nb.cells:
        if cell.cell_type == 'code' and hasattr(cell, 'outputs'):
            for output in cell.outputs:
                if output.output_type == 'execute_result' or output.output_type == 'display_data':
                    if 'text/plain' in output.data:
                        # Aquí necesitarías extraer las variables del output
                        pass
    
    # Alternativa más simple: importar directamente las variables si están en un módulo
    try:
        # Asumiendo que el estudiante guarda sus variables en un archivo
        from ejercicio1_variables import *
        alumno_vars = {
            "texto1": texto1 if 'texto1' in locals() else None,
            "texto2": texto2 if 'texto2' in locals() else None,
            "nombre": nombre if 'nombre' in locals() else None,
            "texto3": texto3 if 'texto3' in locals() else None,
            "apples": apples if 'apples' in locals() else None,
            "formateo": formateo if 'formateo' in locals() else None,
            "palabras": palabras if 'palabras' in locals() else None,
            "texto4": texto4 if 'texto4' in locals() else None,
            "texto5": texto5 if 'texto5' in locals() else None,
            "texto6": texto6 if 'texto6' in locals() else None,
            "texto7": texto7 if 'texto7' in locals() else None,
            "texto8": texto8 if 'texto8' in locals() else None,
        }
    except ImportError:
        pytest.fail("No se pudieron importar las variables del estudiante. Asegúrate de que el notebook se haya ejecutado correctamente.")

    # Verificar que las variables no fueron modificadas 
    for var, valor_original in originales.items():
        if var in alumno_vars:
            valor_alumno = alumno_vars[var]
            assert valor_alumno == valor_original, f"La variable '{var}' fue modificada. Valor esperado: {valor_original!r}, valor encontrado: {valor_alumno!r}"
        else:
            pytest.fail(f"La variable '{var}' no fue encontrada en el código del estudiante.")