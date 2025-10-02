# Test 1 - Validación de la no modificación de las variables del ejercicio1 

import sys
import os
import pytest

# Añadir la ruta al directorio 'data' para importar la función 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))

def test_1():
    try:
        from funciones_ejercicio1 import obtener_variables_ejercicio1
        obtener_variables_ejercicio1()
    except Exception as e:
        pytest.fail(f"El archivo funciones_ejercicio1.py. Recuerde no modificar el archivo funciones_ejercicio1.py. Error: {str(e)}")
        