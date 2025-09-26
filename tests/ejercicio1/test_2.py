import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))
from funciones_ejercicio1 import obtener_variables_ejercicio1

# Importar el archivo generado por el notebook con las variables transformadas
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

    # 8. palabras -> " ".join(palabras)
    assert find_in_namespace(" ".join(originales["palabras"]), str, ns), "No se encontró ninguna variable con ' '.join(palabras)"

    # 9. texto4 -> strip()
    assert find_in_namespace(originales["texto4"].strip(), str, ns), "No se encontró ninguna variable con texto4.strip()"

    # 10. texto5 -> replace("Jhon", algo)
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

    # 11. texto6 -> split("_")
    assert find_in_namespace(originales["texto6"].split("_"), list, ns), "No se encontró ninguna variable con texto6.split('_')"

    # 12. texto7 -> find("colonias")
    assert find_in_namespace(originales["texto7"].find("colonias"), int, ns), "No se encontró ninguna variable con texto7.find('colonias')"

    # 13. texto8 -> quitar tildes (verificamos que ya no existan vocales con tilde)
    found_no_tildes = False
    for var_name in dir(ns):
        if not var_name.startswith('__'):
            var_value = getattr(ns, var_name)
            if isinstance(var_value, str) and all(vocal not in var_value for vocal in "áéíóúÁÉÍÓÚ"):
                if "�" in var_value:  # reemplazo usado
                    found_no_tildes = True
                    break
    assert found_no_tildes, "No se encontró ninguna variable que reemplace las tildes en texto8"
