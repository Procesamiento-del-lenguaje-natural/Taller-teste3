# Test 6 - Validación de la función re.match en ejercicio3
import re
import os

def test_validacion_test_6():
    
    import nbformat
    
    test_6_dir = os.path.dirname(__file__)
    
    # Intentar primero el notebook ejecutado
    executed_notebook_path = os.path.join(test_6_dir, '..', '..', 'notebooks', 'ejercicio3_out.ipynb')
    original_notebook_path = os.path.join(test_6_dir, '..', '..', 'notebooks', 'ejercicio3.ipynb')

    # Usar el notebook ejecutado si existe, sino el original
    if os.path.exists(executed_notebook_path):
        notebook_path = executed_notebook_path
    else:
        notebook_path = original_notebook_path
    
    notebook_path = os.path.abspath(notebook_path)
    
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Unir todo el código de las celdas
    codigo_completo = "\n".join(
        cell.source for cell in nb.cells if cell.cell_type == "code"
    )
    
    # Verificar que se use re.match con patrones correctos
    # Patrón para números: ^\d+$
    assert "re.match(" in codigo_completo, (
        "No se encontró el uso de 're.match()' en el código."
    )
    
    assert r"^\d+$" in codigo_completo, (
        "No se encontró el patrón '^\d+$' para validar números."
    )
    
    # Patrón para letras: ^[a-zA-Z]+$ 
    assert r"^[a-zA-Z]+$" in codigo_completo, (
        "No se encontró el patrón '^[a-zA-Z]+$' para validar letras."
    )
    
    # Patrón para direcciones: debe contener (Calle|Carrera)
    assert "Calle|Carrera" in codigo_completo, (
        "No se encontró el patrón '(Calle|Carrera)' para validar direcciones."
    )
    
    # Verificar que se importe el módulo re
    assert "import re" in codigo_completo, (
        "No se encontró 'import re' en el código. "
        "Asegúrate de importar el módulo re al inicio."
    )