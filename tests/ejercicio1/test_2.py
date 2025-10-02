# Test 2 - Validación de las salidas del ejercicio1

import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))
from funciones_ejercicio1 import obtener_variables_ejercicio1

# Importar el archivo generado al final del notebook ejercicio1.ipynb
import importlib.util
resultados_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'resultados_ejercicio1.py'))
spec = importlib.util.spec_from_file_location('resultados_ejercicio1', resultados_path)
resultados = importlib.util.module_from_spec(spec)
spec.loader.exec_module(resultados)

def find_in_namespace(expected, tipo, ns):
    for var_name in dir(ns):
        if not var_name.startswith('__'):
            var_value = getattr(ns, var_name)
            if isinstance(var_value, tipo) and var_value == expected:
                return var_name
    return None

def test_2():
    originales = obtener_variables_ejercicio1()
    ns = resultados

    # variable: texto1 a minusculas
    assert find_in_namespace(originales["texto1"].lower(), str, ns), "No se encontró ninguna función adecuada para texto1"
    
    # variable: texto2 a mayusculas
    assert find_in_namespace(originales["texto2"].upper(), str, ns), "No se encontró ninguna función adecuada para texto2"

    # variable: nombre cada primer letra de cada palabra en mayuscula
    assert find_in_namespace(originales["nombre"].capitalize(), str, ns), "No se encontró ninguna función adecuada para nombre"

    #variable: texto3 capitalizado
    assert find_in_namespace(originales["texto3"].capitalize(), str, ns), "No se encontró ninguna función adecuada para texto3"

    # variable: apples contar las ocurrencias de la palabra 'apples'
    assert find_in_namespace(originales["apples"].count("apples"), int, ns), "No se encontró ninguna función adecuada para apples"

    # variable: apples encontrar en que lugar del texto esta palabra 'aeppel'
    assert find_in_namespace(originales["apples"].find("aeppel"), int, ns), "No se encontró ninguna función adecuada para aeppel"

    # variable: formateo darle tu nombre y tu edad al texto
    found_format = False
    for var_name in dir(ns):
        if not var_name.startswith('__'):
            var_value = getattr(ns, var_name)
            if isinstance(var_value, str) and "My name is" in var_value and "I'm" in var_value:
                found_format = True
                break
    assert found_format, "No se encontró ninguna función adecuada para formateo"

    # variable: palabras unir las palabras con un ' ' (espacio en blanco)
    assert find_in_namespace(" ".join(originales["palabras"]), str, ns), "No se encontró ninguna función adecuada para palabras"

    # variable: texto4 quitar los espacios en blanco
    assert find_in_namespace(originales["texto4"].strip(), str, ns), "No se encontró ninguna función adecuada para texto4"

    # variable: texto5 reemplazar la palabra Jhon a tu nombre
    orig = originales["texto5"]
    needle = "Jhon"
    pos = orig.find(needle)
    found_replace = False
    if pos != -1:
        left, right = orig[:pos], orig[pos+len(needle):]
        for var_name in dir(ns):
            if not var_name.startswith('__'):
                var_value = getattr(ns, var_name)
                if isinstance(var_value, str) and var_value != orig and var_value.startswith(left) and var_value.endswith(right) and ("Jhon" not in var_value):
                    middle = var_value[len(left): len(var_value) - len(right)] if len(right) > 0 else var_value[len(left):]
                    if middle.strip():
                        found_replace = True
                        break
    assert found_replace, "No se encontró un reemplazo válido de 'Jhon' en texto5"

    # variable: texto6 separar el texto por el caracter '_'
    assert find_in_namespace(originales["texto6"].split("_"), list, ns), "No se encontró ninguna función adecuada para texto6"

    # variable: texto7 encontrar el indice de la palabra colonias
    assert find_in_namespace(originales["texto7"].find("colonias"), int, ns), "No se encontró ninguna función adecuada para texto7"

    # variable: texto8 quitar tildes (verificamos que ya no existan vocales con tilde)
    found_no_tildes = False
    original_texto8 = originales["texto8"]
    for var_name in dir(ns):
        if not var_name.startswith('__'):
            var_value = getattr(ns, var_name)
            # Verificar que sea string, sin tildes, diferente al original y con longitud similar
            if (isinstance(var_value, str) and 
                all(vocal not in var_value for vocal in "áéíóúÁÉÍÓÚ") and
                var_value != original_texto8 and
                abs(len(var_value) - len(original_texto8)) <= 2):
                found_no_tildes = True
                break
    assert found_no_tildes, "No se encontró ninguna variable que reemplace las tildes en texto8"
