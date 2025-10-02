# Test para validar que se usen las funciones/metodos correctos en el notebook ejercicio1.ipynb

import os
import nbformat
import re
import pytest

def test_funciones_usadas():
    notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio1.ipynb'))
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    codigo = "\n".join(cell.source for cell in nb.cells if cell.cell_type == 'code')

    # Validar que se use texto1.lower() y no solo un print
    tiene_print = re.search(r'print\(["\"][^\)]*minusculas[^\)]*["\"]\)', codigo, re.IGNORECASE)
    tiene_lower = re.search(r"texto1_teste\s*=\s*texto1\.lower\(\)", codigo)
    assert tiene_lower, (
        "No se encontró el uso de 'texto1.lower()' para definir 'texto1_teste'. "
        + ("Solo se encontró un print con la respuesta, no la transformación requerida." if tiene_print else "")
    )
    # Validar que se use texto2.upper()
    assert re.search(r"texto2_test\s*=\s*texto2\.upper\(\)", codigo), (
        "No se encontró el uso de 'texto2.upper()' para definir 'texto2_test'."
    )
    # Validar que se use nombre.capitalize()
    assert re.search(r"nombre\s*=\s*nombre\.capitalize\(\)", codigo), (
        "No se encontró el uso de 'nombre.capitalize()' para definir 'nombre'."
    )
    # Validar que se use texto3.capitalize()
    assert re.search(r"texto3_t\s*=\s*texto3\.capitalize\(\)", codigo), (
        "No se encontró el uso de 'texto3.capitalize()' para definir 'texto3_t'."
    )
    # Validar que se use apples.count("apples")
    assert re.search(r"apples_t\s*=\s*apples\.count\(['\"]apples['\"]\)", codigo), (
        'No se encontró el uso de "apples.count(\"apples\")" para definir "apples_t".'
    )
    # Validar que se use apples.find("aeppel")
    assert re.search(r"aeppel_t\s*=\s*apples\.find\(['\"]aeppel['\"]\)", codigo), (
        'No se encontró el uso de "apples.find(\"aeppel\")" para definir "aeppel_t".'
    )
    # Validar que se use formateo.format(
    assert re.search(r"formateo_t\s*=\s*formateo\.format\(", codigo), (
        'No se encontró el uso de "formateo.format()" para definir "formateo_t".'
    )
    # Validar que se use " ".join(palabras)
    assert re.search(r"palabras_t\s*=\s*['\"] ['\"]\.join\(palabras\)", codigo), (
        'No se encontró el uso de " \".join(palabras)" para definir "palabras_t".'
    )
    # Validar que se use texto4.strip()
    assert re.search(r"texto4_t\s*=\s*texto4\.strip\(\)", codigo), (
        'No se encontró el uso de "texto4.strip()" para definir "texto4_t".'
    )
    # Validar que se use texto5.replace("Jhon", ...)
    assert re.search(r'texto5_t\s*=\s*texto5\.replace\(["\\\']Jhon["\\\'],\s*["\\\']', codigo), (
        'No se encontró el uso de "texto5.replace(\"Jhon\", ...)" para definir "texto5_t".'
    )
    # Validar que se use texto6.split("_")
    assert re.search(r"texto6_t\s*=\s*texto6\.split\(['\"]_['\"]\)", codigo), (
        'No se encontró el uso de "texto6.split(\"_\")" para definir "texto6_t".'
    )
