
import os
import nbformat
import re
import pytest

def test_traduccion_correcta():
    # Ruta relativa al notebook
    test_dir = os.path.dirname(__file__)
    notebook_path = os.path.join(test_dir, '..', '..', '..', 'notebooks', 'ejercicio1.ipynb')
    notebook_path = os.path.abspath(notebook_path)
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    # Unir todo el código de las celdas
    codigo = "\n".join(cell['source'] for cell in nb.cells if cell['cell_type'] == 'code')
    # Verificar que hay un print con translate
    assert ("print(" in codigo and ".translate(" in codigo), (
        "No se encontró ningún 'print()' que imprima una traducción con .translate().")
    # Buscar variables relevantes
    relevantes = re.findall(r"([a-zA-Z0-9_]+)\s*=.*", codigo)
    relevantes = [v for v in relevantes if any(p in v for p in ["traducido", "restaurado", "decode", "mensaje"])]
    assert relevantes, (
        "No se encontraron variables tipo string relevantes en el código. Usa nombres descriptivos como 'mensaje_traducido'.")
    # Opcional: podrías intentar ejecutar el notebook y comparar valores, pero esto requiere más setup

