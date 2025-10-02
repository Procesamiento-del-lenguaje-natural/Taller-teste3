# Test 5 - Validación de la salida del ejercicio2

import os
import nbformat
import re
import pytest

def test_5():
    test_dir = os.path.dirname(__file__)
    
    # Intentar primero el notebook ejecutado
    executed_notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio2_out.ipynb')
    original_notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio2.ipynb')
    
    # Usar el notebook ejecutado si existe, sino el original
    if os.path.exists(executed_notebook_path):
        notebook_path = executed_notebook_path
    else:
        notebook_path = original_notebook_path
    
    notebook_path = os.path.abspath(notebook_path)
    
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

