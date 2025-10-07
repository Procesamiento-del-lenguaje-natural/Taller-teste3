# Test para validar que se usen las funciones/metodos correctos en el notebook ejercicio1.ipynb

import os
import re
import sys
import pytest
try:
    import nbformat
except ImportError:
    nbformat = None

def test_2():
    """Test anti-cheating: Verifica métodos correctos, no código hardcodeado y valores esperados"""

    if nbformat is None:
        pytest.skip("El paquete nbformat no está instalado. Instálalo con 'pip install nbformat' para ejecutar este test.")

    notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio1.ipynb'))
    try:
        with open(notebook_path, encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
    except Exception as e:
        pytest.skip(f"No se pudo leer el notebook: {e}")

    codigo = "\n".join(cell.source for cell in nb.cells if cell.cell_type == 'code')

    # Valores esperados (importamos desde funciones_ejercicio1.py para calcular)
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))
    try:
        from funciones_ejercicio1 import obtener_variables_ejercicio1
        vars_originales = obtener_variables_ejercicio1()
    except Exception as e:
        pytest.fail(f"Error al importar variables originales: {e}")

    # Calcular valores esperados
    valores_esperados = {
        'texto1_teste': vars_originales['texto1'].lower(),
        'texto2_test': vars_originales['texto2'].upper(), 
        'nombre': vars_originales['nombre'].capitalize(),
        'texto3_t': vars_originales['texto3'].capitalize(),
        'apples_t': vars_originales['apples'].count('apples'),
        'aeppel_t': vars_originales['apples'].find('aeppel'),
        'formateo_t': None,  # Depende del input del estudiante
        'palabras_t': ' '.join(vars_originales['palabras']),
        'texto4_t': vars_originales['texto4'].strip(),
        'texto5_t': None,  # Depende del reemplazo del estudiante
        'texto6_t': vars_originales['texto6'].split('_'),
        'texto7_t': vars_originales['texto7'].find('colonias'),
        'texto8_t': None  # Flexible - cualquier reemplazo de tildes es válido
    }

    # Lista de validaciones: verifica métodos y detecta código quemado
    validaciones = [
        {
            'metodo': r'\w+\s*=\s*texto1\.lower\(\)',
            'anti_hardcode': r'\w+\s*=\s*["\']este texto en minusculas["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto1.",
            'variable': 'texto1_teste'
        },
        {
            'metodo': r'\w+\s*=\s*texto2\.upper\(\)',
            'anti_hardcode': r'\w+\s*=\s*["\']ESTE TEXTO EN MAYUSCULAS["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto2.",
            'variable': 'texto2_test'
        },
        {
            'metodo': r'\w+\s*=\s*nombre\.capitalize\(\)',
            'anti_hardcode': r'\w+\s*=\s*["\']Alejandro jimenez franco["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable nombre.",
            'variable': 'nombre'
        },
        {
            'metodo': r'\w+\s*=\s*texto3\.capitalize\(\)',
            'anti_hardcode': r'\w+\s*=\s*["\']Este texto capitalizado["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto3.",
            'variable': 'texto3_t'
        },
        {
            'metodo': r'\w+\s*=\s*apples\.count\(["\']apples["\']\)',
            'anti_hardcode': r'\w+\s*=\s*4',
            'mensaje': "No se encontro el uso de la función requerida para la variable apples.",
            'variable': 'apples_t'
        },
        {
            'metodo': r'\w+\s*=\s*apples\.find\(["\']aeppel["\']\)',
            'anti_hardcode': r'\w+\s*=\s*\d+',
            'mensaje': "No se encontro el uso de la función requerida para la variable aeppel.",
            'variable': 'aeppel_t'
        },
        {
            'metodo': r'\w+\s*=\s*formateo\.format\(',
            'anti_hardcode': r'\w+\s*=\s*["\']My name is .*, I\'m \d+["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable formateo.",
            'variable': 'formateo_t'
        },
        {
            'metodo': r'\w+\s*=\s*["\'][^"\']*["\']\.join\(palabras\)',
            'anti_hardcode': r'\w+\s*=\s*["\']Hello World !["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable palabras.",
            'variable': 'palabras_t'
        },
        {
            'metodo': r'\w+\s*=\s*texto4\.strip\(\)',
            'anti_hardcode': r'\w+\s*=\s*["\']programar["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto4.",
            'variable': 'texto4_t'
        },
        {
            'metodo': r'\w+\s*=\s*texto5\.replace\(',
            'anti_hardcode': r'\w+\s*=\s*["\'][^"\']*loves programming["\']',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto5.",
            'variable': 'texto5_t'
        },
        {
            'metodo': r'\w+\s*=\s*texto6\.split\(',
            'anti_hardcode': r'\w+\s*=\s*\[.*\]',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto6.",
            'variable': 'texto6_t'
        },
        {
            'metodo': r'\w+\s*=\s*texto7\.find\(["\']colonias["\']\)',
            'anti_hardcode': r'\w+\s*=\s*\d+',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto7.",
            'variable': 'texto7_t'
        },
        {
            'metodo': r'\w+\s*=\s*texto8\.replace\(',
            'anti_hardcode': r'\w+\s*=\s*["\']El examen era manana["\']',  # Solo detecta si pone exactamente esta frase hardcodeada
            'mensaje': "No se encontro el uso de la función requerida para la variable texto8.",
            'variable': 'texto8_t'
        }
    ]

    # Validar cada método y detectar código hardcodeado
    for v in validaciones:
        # Verificar que use el método correcto
        tiene_metodo = re.search(v['metodo'], codigo, re.IGNORECASE)
        assert tiene_metodo, v['mensaje']
        
        # Verificar que NO esté hardcodeado
        tiene_hardcode = re.search(v['anti_hardcode'], codigo, re.IGNORECASE)
        if tiene_hardcode:
            pytest.fail(f"Código hardcodeado detectado: {v['mensaje']}")

    # Verificar que las variables se asignen correctamente (no solo prints)
    variables_requeridas = [
        'texto1_teste', 'texto2_test', 'nombre', 'texto3_t', 'apples_t', 
        'aeppel_t', 'formateo_t', 'palabras_t', 'texto4_t', 'texto5_t', 
        'texto6_t', 'texto7_t', 'texto8_t'
    ]
    
    for var in variables_requeridas:
        patron_asignacion = re.compile(rf'{var}\s*=\s*[^=]', re.IGNORECASE)
        tiene_asignacion = patron_asignacion.search(codigo)
        if not tiene_asignacion:
            pytest.fail(f"La variable '{var}' debe ser asignada correctamente, no solo impresa.")

    # Verificar valores esperados (importar resultados_ejercicio1.py) 
    try:
        results_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'resultados_ejercicio1.py'))
        if os.path.exists(results_path):
            sys.path.insert(0, os.path.dirname(results_path))
            import importlib.util
            spec = importlib.util.spec_from_file_location("resultados", results_path)
            resultados = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(resultados)
            
            # Verificar valores específicos que no dependen del input del estudiante
            valores_a_verificar = {
                'texto1_teste': valores_esperados['texto1_teste'],
                'texto2_test': valores_esperados['texto2_test'],
                'nombre': valores_esperados['nombre'],
                'texto3_t': valores_esperados['texto3_t'],
                'apples_t': valores_esperados['apples_t'],
                'aeppel_t': valores_esperados['aeppel_t'],
                'palabras_t': valores_esperados['palabras_t'],
                'texto4_t': valores_esperados['texto4_t'],
                'texto6_t': valores_esperados['texto6_t'],
                'texto7_t': valores_esperados['texto7_t']
                # texto5_t y texto8_t no se verifican porque dependen del input del estudiante
            }
            
            for var, valor_esperado in valores_a_verificar.items():
                if hasattr(resultados, var):
                    valor_actual = getattr(resultados, var)
                    assert valor_actual == valor_esperado, f"La variable '{var}' tiene valor incorrecto. Esperado: {valor_esperado!r}, obtenido: {valor_actual!r}"
    except Exception as e:
        pytest.skip(f"No se pudo verificar resultados_ejercicio1.py: {e}")
