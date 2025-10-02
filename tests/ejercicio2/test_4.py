# Test 4 - Validación de uso correcto de str.maketrans y .translate en ejercicio2

import re
import os

def test_4():
    import nbformat

    # Importación y lectura del notebook
    notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio2.ipynb'))
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    codigo_alumno = "\n".join(
        cell.source for cell in nb.cells if cell.cell_type == "code"
    )


    # Validaciones tipo test_2.py pero para ejercicio2
    # 1. str.maketrans debe usarse en una asignación con dos argumentos
    patron_maketrans = re.compile(r'\w+\s*=\s*str\.maketrans\(([^)]*)\)')
    maketrans_valido = False
    for match in patron_maketrans.finditer(codigo_alumno):
        args = match.group(1)
        if len([a.strip() for a in args.split(",") if a.strip()]) == 2:
            maketrans_valido = True
            break
    assert maketrans_valido, "No se encontró una asignación válida usando 'str.maketrans' con dos argumentos."

    # 2. .translate debe usarse en una asignación (cualquier variable)
    patron_translate = re.compile(r'\w+\s*=\s*\w+\.translate\(')
    tiene_translate = patron_translate.search(codigo_alumno)
    assert tiene_translate, "No se encontró ninguna asignación usando '.translate()' sobre una variable."

    # 3. Si solo hay print con .translate pero no asignación, advertir trampa
    tiene_print_translate = re.search(r'print\([^\)]*\.translate\(', codigo_alumno)
    if tiene_print_translate and not tiene_translate:
        assert False, "Solo se encontró un print con .translate(), no una asignación de variable usando .translate()."


