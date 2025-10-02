# Test 5 - Validación de la salida del ejercicio2

import os
import nbformat
import re
import pytest

def test_5():
    # Asumir que el notebook siempre está en la ruta esperada y no ha sido renombrado
    notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio2_out.ipynb'))
    if not os.path.exists(notebook_path):
        notebook_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'notebooks', 'ejercicio2.ipynb'))

    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Unir todo el código de las celdas
    codigo = "\n".join(cell.source for cell in nb.cells if cell.cell_type == 'code')

    # Verificar que hay un print con translate
    assert ("print(" in codigo and ".translate(" in codigo), (
        "No se encontró ningún 'print()' que imprima una traducción con .translate().")

    # Buscar variables relevantes 
    relevantes = re.findall(r"([a-zA-Z0-9_]+)\s*=.*", codigo)
    relevantes = [v for v in relevantes if any(p in v for p in ["traducido", "restaurado", "decode", "mensaje", "encoded", "decoded"])]

    assert relevantes, (
        f"No se encontraron variables tipo string relevantes en el código. Variables encontradas: {relevantes}. "
        "Usa nombres descriptivos como 'mensaje_traducido', 'encoded_message', 'decoded_message'.")

