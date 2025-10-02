# Test 9 - Validación de salida (Funcionalidad)
import re
import os
import nbformat

def test_validacion_salida_ejercicio4():
    
    # Leer notebook
    test_dir = os.path.dirname(__file__)
    notebook_path = os.path.join(test_dir, '..', '..', 'notebooks', 'ejercicio4.ipynb')
    
    with open(os.path.abspath(notebook_path), encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)
    
    # Ejecutar código
    codigo = "\n".join(cell.source for cell in nb.cells if cell.cell_type == "code")
    namespace = {}
    
    try:
        exec(codigo, namespace)
        
        # Verificar variable tweets_procesados
        assert 'tweets_procesados' in namespace, "❌ No se encontró 'tweets_procesados'"
        tweets_procesados = namespace['tweets_procesados']
        
        # Verificar estructura básica
        assert isinstance(tweets_procesados, list), "❌ 'tweets_procesados' debe ser lista"
        assert len(tweets_procesados) == 10, f"❌ Se esperaban 10 tweets, se encontraron {len(tweets_procesados)}"
        
        # Verificar procesamiento correcto
        for i, tweet in enumerate(tweets_procesados):
            assert isinstance(tweet, str), f"❌ Tweet {i+1} no es string"
            assert '\n' not in tweet, f"❌ Tweet {i+1} contiene saltos de línea"
            assert not re.search(r'https?://\S+', tweet), f"❌ Tweet {i+1} contiene URLs"
            assert tweet == tweet.lower(), f"❌ Tweet {i+1} no está en minúsculas"
            
            # Verificar emojis removidos (patrón general en lugar de lista específica)
            assert not re.search(r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U00002702-\U000027B0\U000024C2-\U0001F251]', tweet), f"❌ Tweet {i+1} contiene emojis"
        
        print(f"✅ {len(tweets_procesados)} tweets procesados correctamente")
        
    except Exception as e:
        assert False, f"❌ Error al ejecutar código: {str(e)}"
