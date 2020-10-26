"""Las pruebas de caja de cristal hacen referencia a aquellas pruebas donde se realiza el test a cada una de las posibles salidas de los loop(for, while, etc) o del codigo hasta su final.

Asumen que conocemos la implementaciones de cada funcion.

Utiles en refression testing cuando se encuentran bugs.
"""

import unittest


def mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class TestDeCristal(unittest.TestCase):

    def test_mayor_de_edad(self):
        edad = 20

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_menor_de_edad(self):
        edad = 17

        resultado = mayor_de_edad(edad)

        self.assertEqual(resultado, False)



if __name__ == '__main__':
    unittest.main()