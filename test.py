"""Unittest para la función suma"""
import unittest
from main import suma

class TestPrueba(unittest.TestCase):
    """Clase de pruebas para main"""
    def test_suma(self):
        """Prueba para función suma"""
        self.assertEqual(suma(2,3), 5)

if __name__== "__main__":
    unittest.main()
