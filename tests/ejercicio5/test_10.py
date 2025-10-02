# Test 10 - Validación de funciones SpellChecker en ejercicio5
import os
import nbformat

def test_validacion_test_10():
    
    # Configurar rutas del notebook 
    test_dir = os.path.dirname(__file__)
    notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio5.ipynb')
    
    # Leer y procesar notebook
    with open(notebook_path, encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Extraer código de todas las celdas de código
    codigo_completo = "\n".join(
        cell.source for cell in nb.cells if cell.cell_type == "code"
    )
    
    # Verificaciones básicas requeridas
    patrones_basicos = [
        ("import re", "Importación del módulo 're'")
    ]
    
    for patron, descripcion in patrones_basicos:
        assert patron in codigo_completo, f"❌ {descripcion}"
    
    # Verificaciones específicas de re.findall y SpellChecker
    patrones_especificos = [
        ([r"SpellChecker(language='es')", r'SpellChecker(language="es")'], "recuerde configurar la función SpellChecker () en español"),
        ([r"re.findall(r'[a-záéíóúñü]+'", r're.findall(r"[a-záéíóúñü]+'], "Es necesario dividir el texto en palabras"),
        ([".lower()", "lower()"], "Falta uso de la función para convertir texto a minúsculas"),
        ([".unknown(", "unknown("], "Falta uso de la función para identificar palabras mal escritas"),
        ([".candidates(", "candidates("], "Falta uso de la función para obtener sugerencias de corrección"),
    ]
    
    for item in patrones_especificos:
        if isinstance(item[0], list):  # Si es una lista de variantes
            variantes, descripcion = item
            assert any(patron in codigo_completo for patron in variantes), f"❌ {descripcion}"
        else:  # Si es un patrón simple
            patron, descripcion = item
            assert patron in codigo_completo, f"❌ {descripcion}"
    
    # Verificar funcionamiento
    try:
        namespace = {}
        exec(codigo_completo, namespace)
        
        # Buscar cualquier variable que contenga palabras mal escritas
        variables_spell = [var for var in namespace.values() 
                          if hasattr(var, '__iter__') and not isinstance(var, str) 
                          and len(var) > 0]
        
        # Verificar que al menos una variable tenga palabras detectadas
        palabras_detectadas = 0
        for var in variables_spell:
            try:
                if len(var) >= 5:  # Al menos 5 palabras mal escritas
                    palabras_detectadas = len(var)
                    break
            except:
                continue
        
        assert palabras_detectadas >= 5, f"❌ Se esperaban al menos 5 palabras mal escritas, se encontraron {palabras_detectadas}"
        
        print(f"✅ Funcionalidad correcta: {palabras_detectadas} palabras mal escritas detectadas")
        
    except Exception as e:
        assert False, f"❌ Error al ejecutar el código: {str(e)}"

    print("✅ Todos los patrones requeridos están presentes y el código funciona correctamente")