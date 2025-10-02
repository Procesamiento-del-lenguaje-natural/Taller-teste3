# Test 7 - Validación de las funciones re.search y re.findall en ejercicio3
import re
import os

def test_7():

    import nbformat
    test_dir = os.path.dirname(__file__)
    
    # Intentar primero el notebook ejecutado
    executed_notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio3_out.ipynb')
    original_notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio3.ipynb')
    
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
    
    # Verificar que se use re.search() para buscar correo específico
    assert "re.search(" in codigo_completo, (
        "No se encontró el uso de 're.search()' en el código. "
        "Asegúrate de usar re.search() para buscar el correo 'ventas@empresa.net'."
    )
    
    # Verificar que se busque el correo específico "ventas@empresa.net" 
    assert "ventas@empresa" in codigo_completo, (
        "No se encontró la búsqueda del correo 'ventas@empresa.net' en el código. "
        "Asegúrate de buscar específicamente este correo usando re.search()."
    )
    
    # Verificar que se escape correctamente el punto en el dominio
    patrones_busqueda_email = [
        r"ventas@empresa\.net",  # Con escape del punto 
        r"ventas@empresa\\\.net"  # Con escape doble del punto
    ]
    
    patron_correcto_encontrado = any(patron in codigo_completo for patron in patrones_busqueda_email)
    assert patron_correcto_encontrado, (
        "No se encontró el patrón correcto para buscar 'ventas@empresa.net'. "
        "Recuerda escapar el punto del dominio usando '\\.' en el patrón regex."
    )
    
    # Verificar que se use re.findall() para encontrar todos los correos
    assert "re.findall(" in codigo_completo, (
        "No se encontró el uso de 're.findall()' en el código. "
        "Asegúrate de usar re.findall() para encontrar todas las direcciones de correo válidas."
    )
    
    # Verificar que existe un patrón para validar correos electrónicos
    patrones_email_posibles = [
        r"[\w\.-]+@[\w\.-]+\.\w{2,}",  # Patrón básico para emails
        r"^[\w\.-]+@[\w\.-]+\.\w{2,}$",  # Patrón con anchors
        r"[A-Za-z0-9\.-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+",  # Patrón más específico
    ]
    
    patron_email_encontrado = any(patron in codigo_completo for patron in patrones_email_posibles)
    assert patron_email_encontrado, (
        "No se encontró un patrón regex válido para correos electrónicos. "
        "Asegúrate de incluir un patrón que valide direcciones de correo electrónico."
    )
    
    # Verificar que se use la variable textoCorreos
    assert "textoCorreos" in codigo_completo, (
        "No se encontró el uso de la variable 'textoCorreos' en el código. "
        "Asegúrate de usar esta variable para buscar correos en el texto."
    )