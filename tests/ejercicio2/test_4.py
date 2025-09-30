# Test 4
import re

def test_uso_maketrans_y_translate():

    import os
    import nbformat
    test_dir = os.path.dirname(__file__)
    notebook_path = os.path.join(test_dir, '..', '..', '..', 'notebooks', 'ejercicio2.ipynb')
    notebook_path = os.path.abspath(notebook_path)
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    codigo_alumno = "\n".join(
        line for cell in nb.cells if cell.cell_type == "code" for line in cell.source
    )
    # Verificar uso correcto de str.maketrans con dos argumentos
    coincidencias = re.findall(r"str\.maketrans\(([^)]*)\)", codigo_alumno)
    maketrans_valido = any(len([a.strip() for a in args.split(",") if a.strip()]) == 2 for args in coincidencias)
    assert maketrans_valido, "No se encontró una implementación válida de 'str.maketrans()'"
    # Verificar que se imprime una traducción con .translate
    print_con_translate = "print(" in codigo_alumno and ".translate(" in codigo_alumno
    assert print_con_translate, "No se encontró ningún 'print()' que imprima una traducción con .translate()."


