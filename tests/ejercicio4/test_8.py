# Test 8 - Validación de funciones (Anti-trampa)
import os
import nbformat

def test_8():
    
    # Leer notebook
    test_dir = os.path.dirname(__file__)
    notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio4.ipynb')
    
    with open(os.path.abspath(notebook_path), encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Extraer todo el código del notebook
    codigo_completo = "\n".join(cell.source for cell in nb.cells if cell.cell_type == "code")
    
    # Verificar que existe el loop con tweets
    assert "for " in codigo_completo and "in tweets" in codigo_completo, "❌ Falta loop 'for ... in tweets'"
    
    # Extraer código después del loop
    inicio_loop = codigo_completo.find("for ")
    codigo_despues_loop = codigo_completo[inicio_loop:]
    
    # Verificar USO correcto de funciones (no solo que aparezcan)
    assert "= re.sub(" in codigo_despues_loop, "❌ Falta asignación con re.sub()"
    assert ".lower()" in codigo_despues_loop, "❌ Falta uso de .lower()"
    assert ".append(" in codigo_despues_loop, "❌ Falta uso de .append()"
    assert "emoji_pattern.sub(" in codigo_despues_loop, "❌ Falta uso de emoji_pattern.sub()"
    
    print("✅ Test 8: Funciones correctas encontradas")
