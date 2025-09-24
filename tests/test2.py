# ------------------------------
# TEST 2 (GIT): Verificar transformaciones correctas (sin importar nombres de variables)
# ------------------------------
import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data')))
from funciones_ejercicio1 import obtener_variables_ejercicio1

# Importar el archivo generado por el notebook con las variables transformadas
import importlib.util
resultados_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'resultados_ejercicio1.py'))
spec = importlib.util.spec_from_file_location('resultados_ejercicio1', resultados_path)
resultados = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resultados)

def find_in_namespace(expected, tipo, ns):
    """
    Busca en el namespace alguna variable con el valor esperado y tipo dado.
    """
    for var_name in dir(ns):
        if not var_name.startswith('__'):
            var_value = getattr(ns, var_name)
            if isinstance(var_value, tipo) and var_value == expected:
                return var_name
    return None

def test_transformaciones_correctas():
    originales = obtener_variables_ejercicio1()
    ns = resultados

    # 1. texto1 -> minusculas
    assert find_in_namespace(originales["texto1"].lower(), str, ns), "No se encontró ninguna variable con texto1.lower()"

    # 2. texto2 -> mayusculas
    assert find_in_namespace(originales["texto2"].upper(), str, ns), "No se encontró ninguna variable con texto2.upper()"

    # 3. nombre -> capitalize
    assert find_in_namespace(originales["nombre"].capitalize(), str, ns), "No se encontró ninguna variable con nombre.capitalize()"

    # 4. texto3 -> capitalize
    assert find_in_namespace(originales["texto3"].capitalize(), str, ns), "No se encontró ninguna variable con texto3.capitalize()"

    # 5. apples -> count("apples")
    assert find_in_namespace(originales["apples"].count("apples"), int, ns), "No se encontró ninguna variable con apples.count('apples')"

    # 6. apples -> find("aeppel")
    assert find_in_namespace(originales["apples"].find("aeppel"), int, ns), "No se encontró ninguna variable con apples.find('aeppel')"

    # 7. formateo -> format (solo revisamos que haya aplicado format, no valores fijos)
    found_format = False
    for var_name in dir(ns):
        if not var_name.startswith('__'):
            var_value = getattr(ns, var_name)
            if isinstance(var_value, str) and "My name is" in var_value and "I'm" in var_value:
                found_format = True
                break
    assert found_format, "No se encontró ninguna variable que corresponda a formateo.format(...)"
