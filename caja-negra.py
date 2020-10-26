import unittest

"""usamos el MODULO unittest de python para el ejercicio de la caja negra
"""


def suma(num1, num2):
    return abs(num1) + num2
    """Se colo abs para producir un error a drede en el codigo y ver como se comportaba el test"""

class CajaNegraTest(unittest.TestCase):

    def test_de_suma(self):
        num1 = 10
        num2 = 5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, 15)


    def test_de_suma_negativos(self):
        num1 = -3
        num2 = -5

        resultado = suma(num1, num2)

        self.assertEqual(resultado, -8)



if __name__ == '__main__':
    unittest.main()
