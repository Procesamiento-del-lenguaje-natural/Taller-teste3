# Eliminar el archivo antiguo para evitar confusiones
import os
old_path = os.path.join(os.path.dirname(__file__), 'test2.py')
if os.path.exists(old_path):
    os.remove(old_path)
