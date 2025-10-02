# Test para validar que se usen las funciones/metodos correctos en el notebook ejercicio1.ipynb

import os
import re
import pytest
try:
    import nbformat
except ImportError:
    nbformat = None

def test_funciones_usadas():

    if nbformat is None:
        pytest.skip("El paquete nbformat no está instalado. Instálalo con 'pip install nbformat' para ejecutar este test.")

    notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio1.ipynb'))
    try:
        with open(notebook_path, encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
    except Exception as e:
        pytest.skip(f"No se pudo leer el notebook: {e}")

    codigo = "\n".join(cell.source for cell in nb.cells if cell.cell_type == 'code')

    # Lista de validaciones: cada dict contiene el método, el texto clave para el print, el patrón de método, y el mensaje
    validaciones = [
        {
            'metodo': r'texto1\.lower\(\)',
            'print_kw': 'minusculas',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto1."
        },
        {
            'metodo': r'texto2\.upper\(\)',
            'print_kw': 'mayusculas',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto2."
        },
        {
            'metodo': r'nombre\.capitalize\(\)',
            'print_kw': 'nombre modificado',
            'mensaje': "No se encontró el uso de función requerida para la variable nombre"
        },
        {
            'metodo': r'texto3\.capitalize\(\)',
            'print_kw': 'texto3 modificado',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto3."
        },
        {
            'metodo': r'apples\.count\(["\']apples["\']\)',
            'print_kw': 'apples',
            'mensaje': "No se encontro el uso de la función requerida para la variable apples."
        },
        {
            'metodo': r'apples\.find\(["\']aeppel["\']\)',
            'print_kw': 'aeppel',
            'mensaje': "No se encontro el uso de la función requerida para la variable aeppel."
        },
        {
            'metodo': r'formateo\.format\(',
            'print_kw': 'mi nombre y edad',
            'mensaje': "No se encontro el uso de la función requerida para la variable formateo."
        },
        {
            'metodo': r'["\'] ["\']\.join\(palabras\)',
            'print_kw': 'union de palabras',
            'mensaje': "No se encontro el uso de la función requerida para la variable palabras."
        },
        {
            'metodo': r'texto4\.strip\(\)',
            'print_kw': 'texto4 modificado',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto4."
        },
        {
            'metodo': r'texto5\.replace\(["\']Jhon["\'],\s*["\']',
            'print_kw': 'texto5 modificado',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto5."
        },
        {
            'metodo': r'texto6\.split\(["\']_["\']\)',
            'print_kw': 'texto6 modificado',
            'mensaje': "No se encontro el uso de la función requerida para la variable texto6."
        }
    ]

    for v in validaciones:
        # Permitir cualquier nombre de variable de salida, pero debe ser asignación con el método correcto
        patron = re.compile(r'\w+\s*=\s*' + v['metodo'])
        tiene_metodo = patron.search(codigo)
        tiene_print = re.search(r'print\(["\'][^\)]*' + v['print_kw'] + r'[^\)]*["\']\)', codigo, re.IGNORECASE)
        assert tiene_metodo, v['mensaje']
