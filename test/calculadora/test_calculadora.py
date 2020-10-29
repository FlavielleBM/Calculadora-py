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
    
    def test_deveExecutarUmaSoma(self):
        calculadora = Calculadora(10)
        calculadora.somar(20)
        self.assertEqual(30, calculadora.valor)

    def test_deveExecutarUmaDivisao(self):
        calculadora = Calculadora(10)
        calculadora.dividir(20)
        self.assertEqual(0.5, calculadora.valor)

    def test_deveExecutarUmaDivisaoComResultadoDaSoma(self):
        calculadora = Calculadora(10)
        calculadora.somar(20)
        calculadora.dividir(20)
        self.assertEqual(1.5, calculadora.valor)
