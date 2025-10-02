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

    # Diccionario de variables transformadas esperadas: nombre_variable: valor_esperado
    variables_esperadas = {
        'texto1_teste': originales["texto1"].lower(),
        'texto2_test': originales["texto2"].upper(),
        'nombre': originales["nombre"].capitalize(),
        'texto3_t': originales["texto3"].capitalize(),
        'apples_t': originales["apples"].count("apples"),
        'aeppel_t': originales["apples"].find("aeppel"),
        'formateo_t': None,  # Se valida aparte
        'palabras_t': " ".join(originales["palabras"]),
        'texto4_t': originales["texto4"].strip(),
        # texto5_t y texto6_t se validan aparte
    }

    # Validar que cada variable transformada existe y tiene el valor esperado
    for var, valor_esperado in variables_esperadas.items():
        if var == 'formateo_t':
            # Validar que existe y contiene el formato esperado
            assert hasattr(ns, var), f"No se encontró la variable '{var}' en el archivo de resultados."
            valor = getattr(ns, var)
            assert isinstance(valor, str) and "My name is" in valor and "I'm" in valor, f"La variable '{var}' no tiene el formato esperado. Valor encontrado: {valor!r}"
        else:
            assert hasattr(ns, var), f"No se encontró la variable '{var}' en el archivo de resultados."
            valor = getattr(ns, var)
            assert valor == valor_esperado, f"La variable '{var}' tiene un valor incorrecto. Esperado: {valor_esperado!r}, encontrado: {valor!r}"

    # texto5_t: reemplazar la palabra Jhon a tu nombre
    orig = originales["texto5"]
    needle = "Jhon"
    pos = orig.find(needle)
    assert hasattr(ns, 'texto5_t'), "No se encontró la variable 'texto5_t' en el archivo de resultados."
    valor = getattr(ns, 'texto5_t')
    if pos != -1:
        left, right = orig[:pos], orig[pos+len(needle):]
        assert valor != orig and valor.startswith(left) and valor.endswith(right) and ("Jhon" not in valor), \
            f"La variable 'texto5_t' no es un reemplazo válido de 'Jhon'. Valor encontrado: {valor!r}"

    # texto6_t: separar el texto por el caracter '_'
    assert hasattr(ns, 'texto6_t'), "No se encontró la variable 'texto6_t' en el archivo de resultados."
    valor = getattr(ns, 'texto6_t')
    assert valor == originales["texto6"].split("_"), f"La variable 'texto6_t' tiene un valor incorrecto. Esperado: {originales['texto6'].split('_')!r}, encontrado: {valor!r}"

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
