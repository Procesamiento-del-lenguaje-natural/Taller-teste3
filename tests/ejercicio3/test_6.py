# Test 6 - Validación de la función re.match en ejercicio3
import re
import os
import nbformat

def test_validacion_test_6():
    """Test que valida el uso correcto de re.match() con patrones regex específicos"""
    
    # Configurar rutas del notebook 
    test_dir = os.path.dirname(__file__)
    notebook_paths = [
        os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio3_out.ipynb'),  # Ejecutado
        os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio3.ipynb')       # Original
    ]
    
    # Usar el primer notebook que exista
    notebook_path = next((path for path in notebook_paths if os.path.exists(path)), None)
    assert notebook_path, "No se encontró el archivo ejercicio3.ipynb"
    
    # Leer y procesar notebook
    with open(os.path.abspath(notebook_path), encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Extraer código de todas las celdas de código
    codigo_completo = "\n".join(
        cell.source for cell in nb.cells if cell.cell_type == "code"
    )
    
    # Definir patrones requeridos y sus descripciones
    patrones_requeridos = [
        ("import re", "Importación del módulo 're'"),
        ("re.match(", "Uso de la función 're.match()'"),
        (r"^\d+$", "Patrón regex para validar números (^\d+$)"),
        (r"^[a-zA-Z]+$", "Patrón regex para validar letras (^[a-zA-Z]+$)"),
        ("Calle|Carrera", "Patrón regex para validar direcciones con (Calle|Carrera)"),
    ]
    
    # Verificar cada patrón requerido
    for patron, descripcion in patrones_requeridos:
        assert patron in codigo_completo, (
            f"❌ No se encontró: {descripcion}\n"
            f"Asegúrate de incluir '{patron}' en tu código."
        )
    
    # Verificaciones adicionales más específicas
    # Verificar que se use re.match específicamente con los patrones de números y letras
    assert any(patron in codigo_completo for patron in [r"re.match(r'^\d+$'", r're.match(r"^\d+$"']), (
        "❌ No se encontró re.match() usado específicamente para validar números.\n"
        "Ejemplo esperado: re.match(r'^\d+$', texto)"
    )
    
    assert any(patron in codigo_completo for patron in [r"re.match(r'^[a-zA-Z]+$'", r're.match(r"^[a-zA-Z]+$"']), (
        "❌ No se encontró re.match() usado específicamente para validar letras.\n"
        "Ejemplo esperado: re.match(r'^[a-zA-Z]+$', texto)"
    )
    
    print("✅ Todos los patrones regex requeridos están presentes en el código")