# PU_desviacion_est.py

import unittest
from calculadora import calcular_media, calcular_desviacion_estandar, NoSePuedeCalcular  # Asegúrate de importar todo lo necesario

class TestCalculos(unittest.TestCase):
    # Aquí tus pruebas como las definimos antes
    def test_media_un_elemento(self):
        self.assertEqual(calcular_media([5]), 5)

    # Resto de las pruebas...

if __name__ == '__main__':
    unittest.main()