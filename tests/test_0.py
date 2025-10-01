# Test 0 - Verificación de estructura del proyecto
import os

def test_estructura_proyecto():
    """
    Test para verificar que la estructura del proyecto sea correcta
    y que todos los archivos necesarios existan.
    """
    
    test_dir = os.path.dirname(__file__)
    project_root = os.path.join(test_dir, '..', '..')
    project_root = os.path.abspath(project_root)
    
    # Archivos y carpetas que deben existir
    estructura_requerida = [
        # Notebooks
        'notebooks/ejercicio1.ipynb',
        'notebooks/ejercicio2.ipynb', 
        'notebooks/ejercicio3.ipynb',
        
        # Tests
        'tests/ejercicio1/test_1.py',
        'tests/ejercicio1/test_2.py',
        'tests/ejercicio2/test_4.py',
        'tests/ejercicio2/test_5.py',
        'tests/ejercicio3/test_6.py',
        'tests/ejercicio3/test_7.py',
        
        # Archivos de configuración
        'requirements.txt',
        'README.md',
        
        # Carpeta data (si aplica)
        'data/funciones_ejercicio1.py',
    ]
    
    # Verificar cada archivo/carpeta
    archivos_faltantes = []
    for archivo in estructura_requerida:
        ruta_completa = os.path.join(project_root, archivo)
        if not os.path.exists(ruta_completa):
            archivos_faltantes.append(archivo)
    
    assert not archivos_faltantes, (
        f"Faltan los siguientes archivos en la estructura del proyecto: {archivos_faltantes}. "
        f"Asegúrate de mantener la estructura original del proyecto."
    )
    
    # Verificar específicamente el ejercicio3.ipynb
    ejercicio3_path = os.path.join(project_root, 'notebooks', 'ejercicio3.ipynb')
    assert os.path.exists(ejercicio3_path), (
        f"No se encontró el archivo ejercicio3.ipynb en: {ejercicio3_path}. "
        f"Este archivo es requerido para el ejercicio 3."
    )