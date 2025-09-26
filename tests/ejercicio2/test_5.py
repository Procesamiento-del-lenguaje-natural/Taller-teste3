# Importación de librerias
from IPython import get_ipython


def validar_traduccion_correcta():
    shell = get_ipython()
    history = shell.history_manager.get_range()

    # Verificar que hay un print con translate ---
    print_con_translate = any(
        "print(" in code and ".translate(" in code
        for _, _, code in history

    )

    if print_con_translate:
        print("✅ Se detectó un 'print()' que imprime el resultado de una traducción (.translate).")
    else:
        print("❌ No se encontró ningún 'print()' que imprima una traducción con .translate().")
        return False

    # Verificar que la decodificación fue correcta ---
    namespace = globals()

    # Filtrar solo variables string relevantes por nombre
    variables_texto = {k: v for k, v in namespace.items() if isinstance(v, str) and ("traducido" in k or "restaurado" in k or "decode" in k or "mensaje" in k)}

    if not variables_texto:
        print("⚠️ No se encontraron variables tipo string relevantes en el entorno. Usa nombres descriptivos como 'mensaje_traducido'.")
        return False

    for nombre1, valor1 in variables_texto.items():
        for nombre2, valor2 in variables_texto.items():
            if nombre1 == nombre2:
                continue

            if not isinstance(valor1, str) or not isinstance(valor2, str):
                print(f"⚠️ La variable '{nombre1}' o '{nombre2}' no es de tipo string.")
                continue

            if valor1.strip() == valor2.strip() and len(valor1) > 0:
                print(f"✅ Traducción exitosa detectada entre '{nombre1}' y '{nombre2}'")
                print(f"   Ejemplo del texto restaurado: '{valor1[:40]}'")
                return True

    print("❌ No se encontró coincidencia entre el mensaje original y el decodificado relevante.")

    return False

# Uso

if not validar_traduccion_correcta():

    pruebas_ok = False

