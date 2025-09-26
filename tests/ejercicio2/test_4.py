#Versión jupyter

# Importación de librerias
from IPython import get_ipython
import re

def validar_maketrans_y_translate():
    shell = get_ipython()
    history = shell.history_manager.get_range()

# Verificar uso correcto de str.maketrans
    maketrans_valido = False
    for _, _, code in history:
        coincidencias = re.findall(r"str\.maketrans\(([^)]*)\)", code)
        for args in coincidencias:
            partes = [a.strip() for a in args.split(",") if a.strip()]
            if len(partes) == 2:
                maketrans_valido = True
                break
        if maketrans_valido:
            break

    if maketrans_valido:
        print("✅ Se implementó correctamente 'str.maketrans()'")
    else:
        print("❌ No se encontró una implementación válida de 'str.maketrans()' con dos argumentos.")

# Verificar que se imprime una traducción con .translate
    print_con_translate = any(
        "print(" in code and ".translate(" in code
        for _, _, code in history
    )

    if print_con_translate:
        print("✅ Se detectó un 'print()' que imprime el resultado de una traducción (.translate).")
    else:
        print("❌ No se encontró ningún 'print()' que imprima una traducción con .translate().")

# Resultado global
    return maketrans_valido and print_con_translate

# Ejecución
pruebas_ok = True
if not validar_maketrans_y_translate():
    pruebas_ok = False

# Versión pytest
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


