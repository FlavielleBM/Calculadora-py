from unittest import TestCase
from src.calculadora.models import Calculadora
class TestCalculadora(TestCase):
    def test_deveInformarOValorInicialParaCalculadora(self):
        calculadora = Calculadora(10)
        self.assertEqual(11, calculadora.valor)