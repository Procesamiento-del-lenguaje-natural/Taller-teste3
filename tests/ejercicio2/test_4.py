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

    # Verificar uso correcto de str.maketrans con dos argumentos
    coincidencias = re.findall(r"str\.maketrans\(([^)]*)\)", codigo_alumno)
    maketrans_valido = any(len([a.strip() for a in args.split(",") if a.strip()]) == 2 for args in coincidencias)
    assert maketrans_valido, f"No se encontró una implementación válida de 'str.maketrans()'. Código encontrado: {codigo_alumno[:500]}"

    # Verificar que se imprime una traducción con .translate
    print_con_translate = "print(" in codigo_alumno and ".translate(" in codigo_alumno
    assert print_con_translate, "No se encontró ningún 'print()' que imprima una traducción con .translate()."


