# Test 6 - Validación de la función re.match en ejercicio3 
import os
import nbformat

def test_validacion_test_6():
    """Test que valida el uso correcto de re.match() con patrones regex específicos"""
    
    # Configurar rutas del notebook 
    test_dir = os.path.dirname(__file__)
    notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio3.ipynb')
    
    # Leer y procesar notebook
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Extraer código de todas las celdas de código
    codigo_completo = "\n".join(
        cell.source for cell in nb.cells if cell.cell_type == "code"
    )
    
    # Verificaciones básicas requeridas
    patrones_basicos = [
        ("import re", "Importación del módulo 're'"),
        ("Calle|Carrera", "Patrón regex para direcciones (Calle|Carrera)"),
    ]
    
    for patron, descripcion in patrones_basicos:
        assert patron in codigo_completo, f"❌ {descripcion}"
    
    # Verificaciones específicas de re.match con patrones exactos
    patrones_especificos = [
        ([r"re.match(r'^\d+$'", r're.match(r"^\d+$"'], "re.match() para números (^\d+$)"),
        ([r"re.match(r'^[a-zA-Z]+$'", r're.match(r"^[a-zA-Z]+$"'], "re.match() para letras (^[a-zA-Z]+$)"),
    ]
    
    for variantes, descripcion in patrones_especificos:
        assert any(patron in codigo_completo for patron in variantes), f"❌ {descripcion}"
    
    print("✅ Todos los patrones regex requeridos están presentes en el código")