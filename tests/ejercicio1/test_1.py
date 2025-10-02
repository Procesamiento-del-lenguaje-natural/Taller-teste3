# Test 1 - Validación de la no modificación de las variables del ejercicio1 

import sys
import os
import pytest

# Añadir la ruta al directorio 'data' para importar la función   
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data')))

def test_1():
    try:
        from funciones_ejercicio1 import obtener_variables_ejercicio1
        originales = obtener_variables_ejercicio1()
    except Exception as e:
        pytest.fail(f"El archivo funciones_ejercicio1.py. Recuerde no modificar el archivo funciones_ejercicio1.py. Error: {str(e)}")

    referencia = {
        "texto1": 'ESTE TEXTO EN MINUSCULAS',
        "texto2": 'este texto en mayusculas',
        "nombre": 'alejandro jimenez franco',
        "texto3": 'estE texTo capitAlizado',
        "apples": """
The history of apples dates back thousands of years, originating in Central Asia,
particularly in Kazakhstan. The word "apple," derived from the Old English "aeppel,"
has appeared frequently in literature and agriculture, symbolizing knowledge and temptation.
Romans cultivated apples, and by the Middle Ages, they were a staple fruit in Europe.
When European settlers brought apples to North America in the 17th century,
they became ingrained in American culture, epitomized by the legendary figure Johnny Appleseed.
Today, apples remain one of the most popular fruits globally,
and the word "apple" continues to represent both tradition and innovation.""",
        "formateo": 'My name is {name}, I\'m {age}',
        "palabras": ("Hello", "World", "!"),
        "texto4": "     programar     ",
        "texto5": "Jhon loves programming",
        "texto6": "Hello_World,_today_is_a_great_day",
        "texto7": 'El pingüino es un ave no voladora que habita principalmente en el hemisferio sur. Con su plumaje blanco y negro, es un gran nadador y cazador de peces y krill. Viven en colonias y son muy sociables, formando lazos fuertes durante la crianza de sus crías. Su hábitat enfrenta amenazas por el cambio climático y la contaminación.',
        "texto8": 'El examen era mañana y yo aún tenía mucho que estudiar. Me tomé un vaso de leche con azúcar, dejé de mirar el césped por la ventana de la habitación y, aunque era difícil, me puse a estudiar como nunca antes había hecho.'
    }

    for var, valor_ref in referencia.items():
        if var not in originales:
            pytest.fail(f"La variable '{var}' no fue encontrada en funciones_ejercicio1.py.")
        valor_actual = originales[var]
        assert valor_actual == valor_ref, f"La variable '{var}' fue modificada. Valor esperado: {valor_ref!r}, valor encontrado: {valor_actual!r}"
        