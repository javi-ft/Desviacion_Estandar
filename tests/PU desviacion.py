# PU_desviacion_est.py

import math
import unittest


# Definición de funciones
class NoSePuedeCalcular(Exception):
    pass


def calcular_media(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular con una lista vacía.")
    if not all(isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")
    return sum(elementos) / len(elementos)


def calcular_desviacion_estandar(elementos):
    if not elementos:
        raise NoSePuedeCalcular("No se puede calcular con una lista vacía.")
    if not all(isinstance(x, (int, float)) for x in elementos):
        raise TypeError("Todos los elementos deben ser numéricos.")

    media = calcular_media(elementos)
    varianza = sum((x - media) ** 2 for x in elementos) / len(elementos)
    return math.sqrt(varianza)


# Definición de pruebas
class TestCalculos(unittest.TestCase):

    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([5]), 5)

    def test_desviacion_elementos_no_numericos(self):
        with self.assertRaises(TypeError):
            calcular_desviacion_estandar([1, 2, "a", 4])

    # Más pruebas...


if __name__ == '__main__':
    unittest.main()
