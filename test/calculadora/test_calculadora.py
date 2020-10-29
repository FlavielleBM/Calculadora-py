from unittest import TestCase
from src.calculadora.models import Calculadora
class TestCalculadora(TestCase):
    def test_deveInformarOValorInicialParaCalculadora(self):
        calculadora = Calculadora(10)
        self.assertEqual(10, calculadora.valor)

    def test_deveZerarCalculadora(self):
        calculadora = Calculadora(10)
        calculadora.limpar()
        self.assertEqual(0, calculadora.valor)

    def test_deveZerarCalculadoraAposCalculo(self):
        calculadora = Calculadora(10)
        calculadora.somar(10)
        calculadora.limpar()
        self.assertEqual(0, calculadora.valor)